import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# LangChain components
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma 
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser

# --- Add Logging Configuration ---
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- 1. Load Configuration and Initialize Models ---
load_dotenv()

# Check for API Key
if not os.getenv("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Define constants
CHROMA_DB_PATH = "./chroma_db_full"

# Initialize the LLM (Gemini Pro) and the embedding model
# llm = ChatGoogleGenerativeAI(model="gemma-3n-e4b-it", temperature=0)
llm = ChatOllama(model = "gemma3:1b")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Connect to the existing ChromaDB vector store
vectorstore = Chroma(persist_directory=CHROMA_DB_PATH, embedding_function=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 5}) # Retrieve top 5 most relevant news chunks

# --- 2. Define the RAG Prompt and Chain ---
# PROMPT 1: For when we are NOT in a position. Focus is on finding a strong entry signal.
# ENTRY_TEMPLATE = """
# You are a sophisticated quantitative trading analyst. Your task is to identify potential entry points based on news catalysts.
# Your goal is to determine if the news provides a clear positive signal that could lead to a near-term increase in the stock price.

# - If the news is clearly positive and forward-looking (e.g., beating earnings estimates, announcing a strategic partnership, a successful product launch, or receiving a significant analyst upgrade), output BUY.
# - If the news is neutral, mixed, or simply recaps past events without providing new insight, output HOLD.
# - Do not generate a SELL signal.

# Your response MUST be a single word: BUY or HOLD.

# CONTEXT:
# {context}
# QUESTION: What is the signal for {symbol} on {date}, given that we are currently NOT holding a position?
# ANSWER:
# """

# # FIX: Replace the overly strict EXIT_TEMPLATE with a more balanced one.
# EXIT_TEMPLATE = """
# You are a pragmatic risk manager for a trading desk, currently holding a position in a stock. Your primary task is to protect capital by exiting positions when the outlook for the stock deteriorates.

# - If the news indicates a clear negative shift in the company's fundamentals or outlook (e.g., missing earnings estimates, guiding future revenue down, facing a new regulatory challenge, or a significant analyst downgrade), output SELL.
# - If the news is neutral, slightly negative but not fundamental, or is just market noise, output HOLD. The default action is to maintain the position unless there is a clear reason to exit.
# - Do not generate a BUY signal.

# Your response MUST be a single word: SELL or HOLD.

# CONTEXT:
# {context}
# QUESTION: What is the signal for {symbol} on {date}, given that we ARE currently holding a position?
# ANSWER:
# """

ENTRY_TEMPLATE = """
You are an aggressive momentum trader. Your goal is to enter a position on any sign of positive news.

- If the news context contains any positive sentiment, good news, or optimistic language (e.g., 'up', 'beats', 'strong', 'growth', 'new product'), output BUY.
- Only if the news is explicitly negative or completely neutral, output HOLD.
- Do not generate a SELL signal.

Your response MUST be a single word: BUY or HOLD.

CONTEXT:
{context}
QUESTION: What is the signal for {symbol} on {date}, given that we are currently NOT holding a position?
ANSWER:
"""

# FIX: Made the EXIT_TEMPLATE very generous to encourage SELL signals for testing.
EXIT_TEMPLATE = """
You are a very cautious trader managing an existing position. Your goal is to exit the position on any sign of trouble to protect capital.

- If the news context contains any negative sentiment, bad news, or uncertain language (e.g., 'down', 'misses', 'weak', 'concern', 'investigation'), output SELL.
- Only if the news is explicitly and strongly positive, output HOLD.
- Do not generate a BUY signal.

Your response MUST be a single word: SELL or HOLD.

CONTEXT:
{context}
QUESTION: What is the signal for {symbol} on {date}, given that we ARE currently holding a position?
ANSWER:
"""

ENTRY_PROMPT = ChatPromptTemplate.from_template(ENTRY_TEMPLATE)
EXIT_PROMPT = ChatPromptTemplate.from_template(EXIT_TEMPLATE)

# This function formats the retrieved documents into a single string.
def format_docs(docs):
    return "\n\n---\n\n".join([d.page_content for d in docs])

# --- 3. Create the FastAPI Application ---
app = FastAPI(
    title="RetroTrade RAG Signal Generator",
    description="An API to get trading signals from financial news using Local LLM.",
    version="1.0.0",
)

# Define the request and response models for type safety
class SignalRequest(BaseModel):
    symbol: str
    date: str # e.g., "YYYY-MM-DD"
    is_in_position: bool # True if we are currently holding the stock

class SignalResponse(BaseModel):
    symbol: str
    date: str
    signal: str # Will be "BUY", "SELL", or "HOLD"

# --- 4. Define the API Endpoint ---
@app.post("/generate_signal", response_model=SignalResponse)
def generate_signal(request: SignalRequest):
    """
    Accepts a stock symbol and date, retrieves relevant news,
    and generates a trading signal using the RAG chain.
    """
    logger.info(f"Received request for {request.symbol} on {request.date}, in_position={request.is_in_position}")
    try:

        if request.is_in_position:
            prompt = EXIT_PROMPT
        else:
            prompt = ENTRY_PROMPT
        
        # Define the chain dynamically with the chosen prompt
        rag_chain = (
            {
                "context": (lambda x: f"Financial news for {x['symbol']} on {x['date']}") | retriever | format_docs,
                "symbol": (lambda x: x["symbol"]),
                "date": (lambda x: x["date"])
            }
            | prompt
            | llm
            | StrOutputParser()
        )

        logger.info("Invoking RAG chain...")
        # Invoke the RAG chain to get the signal
        raw_signal = rag_chain.invoke({"symbol": request.symbol, "date": request.date})
        logger.info(f"RAG chain returned raw signal: '{raw_signal}'")
        
        # Clean up the signal to ensure it's one of the three expected values
        cleaned_signal = raw_signal.strip().upper()
        if cleaned_signal not in ["BUY", "SELL", "HOLD"]:
            logger.warning(f"LLM returned an invalid signal: '{cleaned_signal}'. Defaulting to HOLD.")
            cleaned_signal = "HOLD" # Default to HOLD if the LLM gives a weird response

        logger.info(f"Returning cleaned signal: {cleaned_signal}")
        return SignalResponse(
            symbol=request.symbol,
            date=request.date,
            signal=cleaned_signal
        )
    except Exception as e:
        logger.error(f"An unhandled exception occurred: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error processing the request.")
