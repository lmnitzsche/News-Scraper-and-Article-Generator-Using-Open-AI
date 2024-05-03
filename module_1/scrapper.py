# This is a python program containg the Scrapper class which will use a function to take in a given url
# With the url it will send a http request and retrive the contents of the url
# The html elements will then be parsed into a beautifulSoup object where the function extractSoup will
# return a soup object with the uneccessary elements extracted so only the article remains

# I choice the SOLID principle Open-Closed Principle (OCP) to open the possibilities to different web drivers to scrap other than beautiful soup

# Requests is an HTTP library for python that allows to send 
#  HTTP requests 
import requests

# This is a Python library for pulling data out of HTML 
#  and XML files.
from bs4 import BeautifulSoup

# Importing the abc classs to allow for the abstract method
from abc import ABC, abstractmethod

# Class for News Scraper utilizing the abstract method
class Scrapper:
    @abstractmethod
    def requestURL(self,url):
        pass
    def extract(self):
        pass

# Class for News Scraper utilizing beautiful soup
class BeautifulSoupScrapper(Scrapper):
    # Initializing the class url and soup to none
    def __init__(self):
        self.url = None
        self.soup = None

    #  Sends an HTTP GET request to the specified URL, the response
    #  variable will contain the server's reponse to the HTTP request
    def requestURL(self,url):
        self.url = url
    
    # Return a single string of the article text
    
    def extract(self):
        #Checks if the URL is not valid or if there are other issues (such as network problems), you might receive an exception.
        try:
            response = requests.get(self.url)
        except requests.exceptions.RequestException as e:
            # If there's any error making the request, consider the URL invalid
            print("Error:", e)

        #  When you parse HTML content using BeautifulSoup, it creats
        #  a parse tree, which is a hierachical representation of the
        #  HTML structure of the webpage. The line is parsing the HTML
        #  content of the 'reponse' object and creates a BeautifulSoup
        #  object 'soup' that represents the parsed HTML content of the
        #  webpage
        self.soup = BeautifulSoup(response.content, 'html.parser')

        #  This line utilizes BeautifulSoup's find_all() method to locate
        #  all HTML elements listed
        for elem in self.soup.find_all(['script','style','iframe','a','header','footer']):
            # Once these elements are located, the extract() method is
            # called on each of them. The extract() method removes the
            # the element from the parse tree 
            elem.extract()
        for elem in self.soup.find_all(['p','div']):
            if elem.name == 'div' and 'info' in elem.get('class', []):
                elem.extract()
            if elem.name == 'div' and 'user-input' in elem.get('class',[]):
                elem.extract()
        
        # Find the main content of the article by searching the <article> tag
        article_content = self.soup.find('article')

        # Will check if article_content contains anything
        if article_content:
            # It extracts all the text from the HTML element and its children
            # stripping away any HTML tags and stores it int a single string
            # Then it is stored into variable article_text
            article_text = article_content.get_text()
            
            return article_text
        else:
            print(f"No article content found on {self.url}.")
            exit(1)        