import pytest
from src.rufus_agent import RufusAgent

def test_crawl():
    agent = RufusAgent(instructions="Test prompt")
    content = agent.crawl("https://example.com")  # Replace with a real URL
    assert len(content) > 0  # Ensure some content is returned

def test_document_formatting():
    agent = RufusAgent(instructions="Test prompt")
    fake_content = ["<h1>Test Page</h1><p>FAQ: How to use it?</p>"]
    documents = agent.format_as_documents("https://example.com", fake_content)
    assert len(documents) == 1 
    
def crawl(self, url, current_depth=0):
    try:
        response = self.session.get(url)
        response.raise_for_status()  # Raise exception for HTTP errors
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching {url}: {str(e)}")
        return []
      
def test_crawl():
    agent = RufusAgent(instructions="Test prompt")
    content = agent.crawl("https://example.com")
    assert len(content) > 0

def test_document_synthesis():
    agent = RufusAgent(instructions="Test prompt")
    documents = agent.format_as_documents("https://example.com", ["Test summary"])
    assert len(documents) == 1
