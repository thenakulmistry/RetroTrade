import os
import json
import time
import shutil
import re
from dotenv import load_dotenv
from polygon import RESTClient
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

# --- 1. Configuration and Setup ---
# Load environment variables from .env file
load_dotenv()

# Define constants
STOCK_SYMBOL = "AAPL" # Example: Apple Inc.
START_DATE = "2019-01-02"
END_DATE = "2025-07-31"
NEWS_FILE_PATH = f"./{STOCK_SYMBOL}_news_full.json"
CHROMA_DB_PATH = "./chroma_db_full" # Path to store the vector database
EMBEDDING_PROVIDER = os.getenv("EMBEDDING_PROVIDER", "google").strip().lower()
EMBEDDING_MODEL = os.getenv("GOOGLE_EMBEDDING_MODEL", "gemini-embedding-001")
OLLAMA_EMBEDDING_MODEL = os.getenv("OLLAMA_EMBEDDING_MODEL", "nomic-embed-text")
INGEST_TICKER_MODE = os.getenv("INGEST_TICKER_MODE", "primary").strip().lower()  # primary | all
ENABLE_TEXT_SPLIT = os.getenv("ENABLE_TEXT_SPLIT", "false").strip().lower() == "true"
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "1000"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "200"))

if EMBEDDING_PROVIDER == "ollama":
    EMBED_BATCH_SIZE = int(os.getenv("EMBED_BATCH_SIZE", "256"))
    EMBED_BATCH_PAUSE_SEC = float(os.getenv("EMBED_BATCH_PAUSE_SEC", "0"))
    EMBED_MAX_RETRIES = int(os.getenv("EMBED_MAX_RETRIES", "3"))
else:
    EMBED_BATCH_SIZE = int(os.getenv("EMBED_BATCH_SIZE", "64"))
    EMBED_BATCH_PAUSE_SEC = float(os.getenv("EMBED_BATCH_PAUSE_SEC", "0.75"))
    EMBED_MAX_RETRIES = int(os.getenv("EMBED_MAX_RETRIES", "8"))


def get_embeddings():
    if EMBEDDING_PROVIDER == "ollama":
        return OllamaEmbeddings(model=OLLAMA_EMBEDDING_MODEL), f"ollama:{OLLAMA_EMBEDDING_MODEL}"

    google_api_key = os.getenv("GOOGLE_API_KEY")
    if not google_api_key:
        raise ValueError("GOOGLE_API_KEY not found in .env file while EMBEDDING_PROVIDER=google")
    return GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL), f"google:{EMBEDDING_MODEL}"


def _extract_retry_seconds(error_text: str, default_seconds: float = 45.0) -> float:
    match = re.search(r"retry in\s+([0-9]+(?:\.[0-9]+)?)s", error_text, re.IGNORECASE)
    if match:
        return float(match.group(1))
    return default_seconds


def _add_batch_with_retry(vectorstore: Chroma, batch_docs, batch_index: int):
    retries = 0
    while True:
        try:
            vectorstore.add_documents(batch_docs)
            return
        except Exception as e:
            message = str(e)
            is_quota_error = "RESOURCE_EXHAUSTED" in message or "429" in message
            if not is_quota_error or retries >= EMBED_MAX_RETRIES:
                raise

            wait_seconds = _extract_retry_seconds(message)
            wait_seconds = max(wait_seconds, 5.0) + 2.0
            retries += 1
            print(
                f"Batch {batch_index}: quota limit hit. Retry {retries}/{EMBED_MAX_RETRIES} in {wait_seconds:.1f}s..."
            )
            time.sleep(wait_seconds)

# --- 2. Fetch News Data (Run only if the file doesn't exist) ---
def fetch_and_save_news():
    """Fetches news from NewsAPI and saves it to a JSON file."""
    if os.path.exists(NEWS_FILE_PATH):
        print(f"News file '{NEWS_FILE_PATH}' already exists. Skipping download.")
        return

    print("Fetching news from NewsAPI...")
    all_articles = []
    article_count = 0
    page_size = 1000
    try:
        # Initialize the Polygon client
        client = RESTClient(api_key=os.getenv("NEWS_API_KEY"))
       # The client handles pagination automatically. We will add a manual delay.
        for article in client.list_ticker_news(
            ticker=STOCK_SYMBOL,
            published_utc_gte=START_DATE,
            published_utc_lte=END_DATE,
            limit=page_size
        ):
            all_articles.append(article.__dict__)
            article_count += 1

            # FIX: After processing a full page of results, pause to respect the rate limit.
            # The free tier allows 5 requests per minute. We will wait a full minute after every 5 requests.
            # Since our page size is 1000, we can approximate this by waiting after every 5 pages (5000 articles).
            # A safer approach is to wait after every single page.
            if article_count % page_size == 0:
                # We have just completed a "page" (one API call).
                print(f"Processed page ending with article {article_count}. Pausing for 13 seconds to respect rate limit...")
                time.sleep(13) # Pause for 13 seconds (allows just under 5 requests per minute)

        if all_articles:
            with open(NEWS_FILE_PATH, 'w', encoding='utf-8') as f:
                # FIX: Use the 'default' parameter in json.dump to handle nested custom objects.
                # This lambda function tells json.dump: "If you find an object you don't recognize,
                # try converting it to a dictionary using its __dict__ attribute."
                json.dump(all_articles, f, ensure_ascii=False, indent=4, default=lambda o: o.__dict__)
            print(f"Successfully saved {len(all_articles)} articles to '{NEWS_FILE_PATH}'.")
        else:
            print("No articles found for the given date range.")

    except Exception as e:
        print(f"An error occurred while calling the Polygon.io API: {e}")

# --- 3. Process and Ingest Data into ChromaDB ---
def ingest_data():
    """Loads, processes, and ingests news data into the vector database."""
    print("Starting data ingestion process...")

    if not os.path.exists(NEWS_FILE_PATH):
        print(f"News file '{NEWS_FILE_PATH}' not found. Run fetch first.")
        return

    with open(NEWS_FILE_PATH, "r", encoding="utf-8") as f:
        raw_articles = json.load(f)

    documents = []
    for article in raw_articles:
        description = article.get("description") or ""
        title = article.get("title") or ""
        if not description.strip():
            continue

        published_utc = article.get("published_utc")
        published_date = published_utc[:10] if isinstance(published_utc, str) and len(published_utc) >= 10 else None
        content = f"Title: {title}\nDescription: {description}" if title else description
        tickers = article.get("tickers") or []
        symbols = [t.upper() for t in tickers if isinstance(t, str) and t.strip()] or [STOCK_SYMBOL]
        symbols = list(dict.fromkeys(symbols))

        target_symbols = [STOCK_SYMBOL] if INGEST_TICKER_MODE != "all" else symbols

        for symbol in target_symbols:
            metadata = {
                "symbol": symbol,
                "tickers": symbols,
                "published_utc": published_utc,
                "published_date": published_date,
                "news_id": article.get("id"),
                "article_url": article.get("article_url"),
                "publisher": (article.get("publisher") or {}).get("name"),
                "title": title,
            }
            documents.append(Document(page_content=content, metadata=metadata))

    print(f"Loaded {len(documents)} documents from JSON.")

    # Filter out any documents that might have empty descriptions
    documents = [doc for doc in documents if doc.page_content]
    if not documents:
        print("No valid content found in the news file to ingest.")
        return

    if ENABLE_TEXT_SPLIT:
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
        docs = text_splitter.split_documents(documents)
        print(f"Split documents into {len(docs)} chunks.")
    else:
        docs = documents
        print(f"Text splitting disabled. Using {len(docs)} documents as chunks.")

    embeddings, embedding_desc = get_embeddings()
    print(f"Initialized embedding provider/model: {embedding_desc}")

    # Create and persist the ChromaDB vector store
    # This will create a 'chroma_db' directory if it doesn't exist.
    print("Creating and persisting vector store... This may take a few minutes.")
    if os.path.exists(CHROMA_DB_PATH):
        shutil.rmtree(CHROMA_DB_PATH)
        print(f"Cleared existing vector store at '{CHROMA_DB_PATH}' to avoid duplicate/stale records.")

    vectorstore = Chroma(
        persist_directory=CHROMA_DB_PATH,
        embedding_function=embeddings
    )

    total_docs = len(docs)
    print(
        f"Starting batched ingestion: {total_docs} chunks, batch_size={EMBED_BATCH_SIZE}, pause={EMBED_BATCH_PAUSE_SEC}s"
    )

    batch_count = (total_docs + EMBED_BATCH_SIZE - 1) // EMBED_BATCH_SIZE
    for batch_index, start in enumerate(range(0, total_docs, EMBED_BATCH_SIZE), start=1):
        end = min(start + EMBED_BATCH_SIZE, total_docs)
        batch_docs = docs[start:end]
        _add_batch_with_retry(vectorstore, batch_docs, batch_index)

        if batch_index % 10 == 0 or batch_index == batch_count:
            print(f"Ingestion progress: batch {batch_index}/{batch_count} ({end}/{total_docs} chunks)")

        if batch_index < batch_count and EMBED_BATCH_PAUSE_SEC > 0:
            time.sleep(EMBED_BATCH_PAUSE_SEC)

    print(f"Data ingestion complete. Vector store created at '{CHROMA_DB_PATH}'.")

# --- Main Execution ---
if __name__ == "__main__":
    fetch_and_save_news()
    ingest_data()