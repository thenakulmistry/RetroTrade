import os
import json
import time
from dotenv import load_dotenv
from polygon import RESTClient
from langchain_community.document_loaders import JSONLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

# --- 1. Configuration and Setup ---
# Load environment variables from .env file
load_dotenv()

# Define constants
STOCK_SYMBOL = "AAPL" # Example: Apple Inc.
START_DATE = "2019-01-02"
END_DATE = "2025-07-31"
NEWS_FILE_PATH = f"./{STOCK_SYMBOL}_news_full.json"
CHROMA_DB_PATH = "./chroma_db_full" # Path to store the vector database

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

    # Load the raw JSON data
    # The 'jq_schema' helps extract the relevant text content from each article.
    loader = JSONLoader(
        file_path=NEWS_FILE_PATH,
        jq_schema='.[].description', # Extracts the 'description' field from each article object
        text_content=False
    )
    documents = loader.load()
    print(f"Loaded {len(documents)} documents from JSON.")

    # Filter out any documents that might have empty descriptions
    documents = [doc for doc in documents if doc.page_content]
    if not documents:
        print("No valid content found in the news file to ingest.")
        return

    # Split documents into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = text_splitter.split_documents(documents)
    print(f"Split documents into {len(docs)} chunks.")

    # Initialize the embedding model from Google
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    print("Initialized Google embedding model.")

    # Create and persist the ChromaDB vector store
    # This will create a 'chroma_db' directory if it doesn't exist.
    print("Creating and persisting vector store... This may take a few minutes.")
    Chroma.from_documents(
        documents=docs, 
        embedding=embeddings, 
        persist_directory=CHROMA_DB_PATH
    )
    print("Data ingestion complete. Vector store created at './chroma_db'.")

# --- Main Execution ---
if __name__ == "__main__":
    fetch_and_save_news()
    ingest_data()