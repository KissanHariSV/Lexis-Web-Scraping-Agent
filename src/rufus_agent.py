from requests_html import HTMLSession
from transformers import pipeline
from bs4 import BeautifulSoup
from .document_synthesizer import Document

class RufusAgent:
    def __init__(self, instructions, depth=2):
        self.instructions = instructions
        self.session = HTMLSession()
        self.visited_urls = set()
        self.depth = depth
        self.summarizer = pipeline('summarization')

    def crawl(self, url, current_depth=0):
        if current_depth > self.depth or url in self.visited_urls:
            return []

        self.visited_urls.add(url)
        try:
            response = self.session.get(url)
            response.html.render()
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return []

        links = response.html.absolute_links
        content = [response.html.html]

        for link in links:
            if self._is_valid_link(link):
                content += self.crawl(link, current_depth + 1)

        return content

    def _is_valid_link(self, url):
        return url.startswith("https://")
    def crawl_and_extract(self, url):
        html_content = self.crawl(url)
        summarized_content = self.summarize_content(html_content)
        return summarized_content

    def summarize_content(self, content):
        summaries = []
        for page in content:
            summary = self.summarizer(page[:1000])
            summaries.append(summary[0]['summary_text'])
        return summaries

    def format_as_documents(self, url, summarized_content):
        return [Document(url=url, summary=summary, headers=[]).dict() for summary in summarized_content]
