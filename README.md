# Lexis-Web-Scraping-Agent

Rufus is an AI-powered tool designed to intelligently crawl web pages, extract relevant content, and summarize it into structured formats like JSON and CSV. It dynamically handles complex web structures, including JavaScript-rendered content, and provides clean, concise summaries ready for use in machine learning applications, such as Retrieval-Augmented Generation (RAG) pipelines.

Key Features

	•	Web Crawling: Scrapes and extracts content from dynamic web pages.
	•	AI-Powered Summarization: Uses Hugging Face’s transformers library (T5 model) to generate concise summaries based on user-defined prompts.
	•	Text Cleaning & Optimization: Removes unwanted characters, redundant phrases, and ensures sentence coherence.
	•	Structured Output: Saves the cleaned and summarized data in JSON or CSV formats for easy integration.

Installation

Install the required dependencies:

pip install requests-html transformers torch

Usage

	1.	Input the URL to be scraped.
	2.	Select the specific page or content to summarize.
	3.	Save the summarized content as JSON or CSV.
