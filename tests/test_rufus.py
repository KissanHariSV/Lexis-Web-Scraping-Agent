import pytest
from src.rufus_agent import RufusAgent

def test_crawl():
    agent = RufusAgent(instructions="Test prompt")
    content = agent.crawl("https://example.com")
    assert len(content) > 0 

def test_document_formatting():
    agent = RufusAgent(instructions="Test prompt")
    fake_content = ["<h1>Test Page</h1><p>FAQ: How to use it?</p>"]
    documents = agent.format_as_documents("https://example.com", fake_content)
    assert len(documents) == 1 
