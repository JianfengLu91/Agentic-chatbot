import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def get_llm_client() -> ChatGoogleGenerativeAI:
    """Initialize and return a ChatGoogleGenerativeAI client with the provided API key."""
    llm_client = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )
    return llm_client
