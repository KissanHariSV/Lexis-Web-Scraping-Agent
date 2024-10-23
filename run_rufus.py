from src.rufus_client import RufusClient
import os

# Example use of RufusClient
def main():
    # Simulate API key for now
    api_key = "sk-kJeUcKv6C0ulA8F19mU7Nx5H3ayoNKQVIRd0FQ70DYT3BlbkFJPUawK34PIBF-jAAZsxom5CehcwD2xpfWYovZxiFe8A"

    # Create the Rufus client
    client = RufusClient(api_key=api_key)

    # Define the prompt and target URL
    instructions = "Find FAQs and product features."
    url = "https://example.com"  # Replace with the URL you want to scrape

    # Run Rufus to scrape and extract the relevant data
    documents = client.scrape(url, instructions)

    # Print the extracted structured documents
    print(documents)

if __name__ == "__main__":
    main()
