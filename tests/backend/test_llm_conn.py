# test LLM connection functionality
import pytest
from backend.llm_conn import get_llm_client

def test_llm_connection_success():
    conn = get_llm_client()
    response = conn.invoke("What is the capital of France?")
    assert response is not None
    assert "Paris" in response.text
