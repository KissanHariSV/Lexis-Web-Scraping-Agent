from .rufus_agent import RufusAgent

class RufusClient:
    def __init__(self, api_key):
        self.api_key = api_key
    def scrape(self, url, instructions):
        rufus = RufusAgent(instructions)
        content = rufus.crawl_and_extract(url)
        documents = rufus.format_as_documents(url, content)
        rufus.save_documents(documents)
        return documents

    def save_documents(self, documents, filename='output.json'):
        import json
        with open(filename, 'w') as f:
            json.dump(documents, f, indent=4)
