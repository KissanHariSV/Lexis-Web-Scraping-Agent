import time
import requests
from requests_html import HTMLSession
from transformers import pipeline

# Retry logic to handle connection issues
def fetch_url(url, retries=3):
    session = HTMLSession()
    for attempt in range(retries):
        try:
            # Fetch the URL with SSL verification disabled
            response = session.get(url, verify=False)
            # Increase the timeout for rendering the page
            response.html.render(timeout=60, sleep=2)  # Render with a longer timeout
            return response
        except Exception as e:
            print(f"Attempt {attempt+1}/{retries} failed: {e}")
            time.sleep(5)  # wait 5 seconds before retrying
    raise Exception(f"Failed to fetch {url} after {retries} attempts")


def main():
    # Initialize the transformer summarizer (you can specify a specific model if needed)
    summarizer = pipeline('summarization', model="google/t5-small", framework="pt")  # Using PyTorch backend

    # Sample URL for demonstration
    url = "https://example.com"

    try:
        # Fetch the URL with retry and extended timeout
        print(f"Fetching URL: {url}")
        response = fetch_url(url)

        # Extract and print specific content from the page (for example, <h1> tags)
        h1_element = response.html.find('h1', first=True)  # Find the first <h1> tag
        if h1_element:
            print(f"H1 Tag: {h1_element.text}")

        # Summarize the content using the transformer summarizer
        summary = summarizer(response.text[:1000])  # Summarize the first 1000 characters of the page
        print(f"Summary: {summary[0]['summary_text']}")

    except requests.exceptions.SSLError as ssl_err:
        print(f"SSL certificate verification failed: {ssl_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Failed to connect to {url}: {conn_err}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
