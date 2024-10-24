from .rufus_agent import RufusAgent

class RufusClient:
    def __init__(self):
        self.agent = RufusAgent()

    def scrape_and_summarize(self, url, prompt, file_format='json', filename='summarized_content'):
        try:
          
            response, links = self.agent.fetch_and_list_links(url)

            selected_link_index = int(prompt) - 1
            selected_link = links[selected_link_index]
            print(f"Selected Link: {selected_link}")

            response = self.agent.fetch_url(selected_link)
            full_text = self.agent.extract_filtered_text(response)

            summary = self.agent.summarize_content(full_text)
            optimized_summary = self.agent.clean_and_optimize_text(summary)

            summarized_data = {
                'url': selected_link,
                'summary': optimized_summary
            }

            if file_format == 'json':
                self.agent.save_to_json(summarized_data, filename + '.json')
            elif file_format == 'csv':
                self.agent.save_to_csv(summarized_data, filename + '.csv')
            else:
                print("Invalid file format. Please enter 'json' or 'csv'.")

        except Exception as e:
            print(f"An error occurred: {e}")
