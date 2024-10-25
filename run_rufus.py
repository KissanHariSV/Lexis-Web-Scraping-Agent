from src.rufus_client import RufusClient

def main():
    url = input("Please enter the URL to scrape: ")

    try:
        client = RufusClient()

        print("\nHere are all the links on the page:")
        client.scrape_and_fetch_links(url)  
        
        prompt = input("Enter the number of the link you want to summarize: ")

        filename = input("Enter the filename (without extension) for the summarized file: ")
        file_format = input("Enter the file format to save (json/csv): ").strip().lower()

        client.scrape_and_summarize(url, prompt, file_format, filename)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
