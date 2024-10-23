from requests_html import HTMLSession

from transformers import pipeline

from .document_synthesizer import Document

import json

class RufusAgent:
    def __init__(self, instructions, depth=2):
        self.instructions = instructions
        self.session = HTMLSession()
        self.visited_urls = set()
        self.depth = depth
        self.summarizer = pipeline('summarization')

    def __init__(self, api_key):
        self.api_key = api_key

    def scrape(self, url, instructions):
        rufus = RufusAgent(instructions)
        content = rufus.crawl_and_extract(url)
        documents = rufus.format_as_documents(url, content)
        rufus.save_documents(documents)
        return documents

    def crawl_and_extract(self, url):
        html_content = self.crawl(url)
        summarized_content = self.summarize_content(html_content)
        return summarized_content

    def format_as_documents(self, url, summarized_content):
        return [Document(url=url, summary=summary['summary_text'], headers=[]).dict() for summary in summarized_content]

    def save_documents(self, documents, filename='output.json'):
    with open(filename, 'w') as f:
        json.dump(documents, f, indent=4)

    def summarize_content(self, content):
        summaries = []
        for page in content:
            summary = self.summarizer(page[:1000]) 
            summaries.append(summary)
        return summaries

  from bs4 import BeautifulSoup

def extract_faqs(self, html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    faqs = soup.find_all(text=lambda x: 'FAQ' in x or 'Frequently Asked' in x)
    return faqs
