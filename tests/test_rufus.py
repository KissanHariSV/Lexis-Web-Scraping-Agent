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
