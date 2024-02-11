# Importing the requests library to make HTTP requests
import requests

# Importing the Beautiful Soup class from the bs4 module for HTML parsing
from bs4 import BeautifulSoup

# Function to download content from a given URL
def download_content(url):
    try:
        # Sending a GET request to the URL and storing the response
        response = requests.get(url)
        
        # Raising an exception for HTTP errors
        response.raise_for_status()
        
        # Returning the text content of the response
        return response.text
    
    # Catching any Request Exceptions
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch URL: {url}")
        return None

# Function to extact text content from HTML
def extract_text(html_content):
    # Parsing the HTML content using Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Finding all paragraph elements in the HTML
    paragraphs = soup.find_all('p')
    
    # Extracting text content from each paragraph and joining them into a single string
    text_content = ' '.join([paragraph.get_text() for paragraph in paragraphs])
    
    # Returning the extacted text content
    return text_content

# Read the URLs from the text file
with open('links.txt', 'r') as file:
    urls = file.read().splitlines()

# Iterate through each URL and download/copy/scrape the content
for idx, url in enumerate(urls):
    # Printing a message indicating the URL being processed
    print(f"\nProcessing URL {idx + 1}: {url}")
    
    # Downloading content from the current URL
    html_content = download_content(url)

    # Checking if content was successfully downloaded
    if html_content:
        # Extract and clean the text content from the HTML
        text_content = extract_text(html_content)

        # Save the content to a file
        with open(f'news_article_{idx + 1}.txt', 'w', encoding='utf-8') as article_file:
            article_file.write(text_content)

# Printing a message indicating successful download of all news articles
print("\nAll news articles downloaded successfully.")