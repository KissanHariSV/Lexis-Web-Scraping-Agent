from requests_html import HTMLSession

from transformers import pipeline

class RufusAgent:
    def __init__(self, instructions, depth=2):
        self.instructions = instructions
        self.session = HTMLSession()
        self.visited_urls = set()
        self.depth = depth
        # Load a pre-trained summarization model
        self.summarizer = pipeline('summarization')

    def crawl_and_extract(self, url):
        html_content = self.crawl(url)
        summarized_content = self.summarize_content(html_content)
        return summarized_content

    def summarize_content(self, content):
        summaries = []
        for page in content:
            summary = self.summarizer(page[:1000])  # Summarizes the first 1000 tokens
            summaries.append(summary)
        return summaries

  from bs4 import BeautifulSoup

def extract_faqs(self, html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    faqs = soup.find_all(text=lambda x: 'FAQ' in x or 'Frequently Asked' in x)
    return faqs
