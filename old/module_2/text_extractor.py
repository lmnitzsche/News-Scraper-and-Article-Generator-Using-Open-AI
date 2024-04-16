# module2/text_extractor.py
# This module provides a function to extract text content from HTML using Beautiful Soup.

# Input:
    # The HTML content to extract text from (paragraph elements)

# Output:
    # The extracted text content to feed to text file

# Importing the Beautiful Soup class from the bs4 module for HTML parsing
from bs4 import BeautifulSoup

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
