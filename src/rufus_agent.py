import time
import json
import csv
from requests_html import HTMLSession
from transformers import pipeline
from urllib.parse import urljoin
import re

class RufusAgent:
    def fetch_url(self, url, retries=3):
        session = HTMLSession()
        for attempt in range(retries):
            try:
                response = session.get(url)
                response.html.render(timeout=120, sleep=3)
                return response
            except Exception as e:
                print(f"Attempt {attempt+1}/{retries} failed: {e}")
                time.sleep(5)
        raise Exception(f"Failed to fetch {url} after {retries} attempts")

    def extract_filtered_text(self, response):
        elements_to_extract = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']
        extracted_text = []

        for tag in elements_to_extract:
            elements = response.html.find(tag)
            for element in elements:
                if element.text and len(element.text.strip()) > 50:
                    extracted_text.append(element.text.strip())

        filtered_text = ' '.join(extracted_text)
        cleaned_text = re.sub(r'[\u00bb\u2026]+', '', filtered_text)
        cleaned_text = re.sub(r'\s{2,}', ' ', cleaned_text)
        return cleaned_text

    def summarize_content(self, text, max_length=500, min_length=150):
        summarizer = pipeline('summarization', model="t5-small", framework="pt")
        chunks = [text[i:i + 1000] for i in range(0, len(text), 1000)]
        summaries = []

        for chunk in chunks:
            input_length = len(chunk.split())
            adjusted_max_length = min(max_length, max(int(input_length * 0.5), min_length))
            summary = summarizer(chunk, max_length=adjusted_max_length, min_length=min_length, do_sample=False)
            summaries.append(summary[0]['summary_text'])

        final_summary = '\n\n'.join(summaries)
        return final_summary

    def clean_and_optimize_text(self, text):
        text = text.replace("\u2019", "'")
        text = text.replace("\u201c", '"').replace("\u201d", '"')
        text = re.sub(r"[\u2013\u2014]", "-", text)
        text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text)
        text = re.sub(r'(\*|_)(.*?)\1', r'\2', text)
        text = re.sub(r'\s{2,}', ' ', text)
        text = re.sub(r'[\n\r]+', ' ', text)
        text = re.sub(r'\b(\w+)( \1\b)+', r'\1', text, flags=re.IGNORECASE)
        text = re.sub(r'\b(the)\s*\b(the)\b', r'\1', text, flags=re.IGNORECASE)

        sentences = re.split(r'(?<=[.!?]) +', text)
        cleaned_text = ' '.join([s.capitalize() for s in sentences if s])

        cleaned_text = re.sub(r'[^\w\s.,!?\'"]+', '', cleaned_text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()

        return cleaned_text

    def fetch_and_list_links(self, url):
        response = self.fetch_url(url)
        links = self.list_links(response, url)
        return response, links

    def list_links(self, response, base_url):
        links = response.html.absolute_links
        filtered_links = []
        for i, link in enumerate(links):
            filtered_link = urljoin(base_url, link)
            filtered_links.append(filtered_link)
            print(f"{i + 1}. {filtered_link}")
        return filtered_links

    def save_to_json(self, data, filename='summarized_content.json'):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")

    def save_to_csv(self, data, filename='summarized_content.csv'):
        with open(filename, 'w', newline='') as output_file:
            writer = csv.writer(output_file)
            writer.writerow(['url', 'summary'])
            writer.writerow([data['url'], data['summary']])
        print(f"Data saved to {filename}")
