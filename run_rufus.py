from src.rufus_client import RufusClient
import os

def main():
    # Simulate API key retrieval
    api_key = os.getenv('RUFUS_API_KEY', 'fake-api-key')

    # Create the Rufus client
    client = RufusClient(api_key=api_key)

    # Define the prompt and target URL
    instructions = "Find FAQs and product features."
    url = "https://example.com"  # Replace with the actual URL you want to scrape

    # Run Rufus to scrape and extract the relevant data
    documents = client.scrape(url, instructions)

    # Print the extracted structured documents
    print(documents)

if __name__ == "__main__":
    main()
