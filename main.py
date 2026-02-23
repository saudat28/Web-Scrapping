# main.py
from web_scraper import WebScraper
from text_processor import TextProcessor
from sentiment_analyzer import SentimentAnalyzer  # Ensure you have this module
from visualizer import Visualizer  # Ensure you have this module

# URL to scrape
url = 'https://en.wikipedia.org/wiki/Main_Page'

urls = [
    'https://en.wikipedia.org/wiki/Main_Page',
    'http://books.toscrape.com',
]

#Create an instance of WebScraper
scraper = WebScraper(url)

#Download HTML and extract content
scraper.download_html()
scraper.extract_content()
scraper.save_text()

#Scraping multiple pages
scraper.scrape_multiple_pages(urls)
keyword_counts = scraper.keyword_search("search", urls)
print("Keyword search results saved to keyword_counts.txt")

#Aggregate text from multiple files
file_names = [f'article{i}.txt' for i in range(1, len(urls) + 1)]
aggregated_text = TextProcessor.aggregate_texts(file_names)

#Creating object for TextProcessor and clean the extracted paragraphs
processor = TextProcessor()
cleaned_paragraphs = processor.clean_text(scraper.paragraphs)
print("Cleaned Paragraphs:", cleaned_paragraphs)

#Creating  an object for SentimentAnalyzer and call the functions
analyzer = SentimentAnalyzer()
analyzer.analyze_sentiment()  

analyzer.count_sentiments(analyzer.paragraphs_sentiment) 
analyzer.summarize_sentiment() 

#Creating an object for Visualizer and call plot_sentiment function
visualizer = Visualizer()
visualizer.plot_sentiment(analyzer.sentiment_counts) 

