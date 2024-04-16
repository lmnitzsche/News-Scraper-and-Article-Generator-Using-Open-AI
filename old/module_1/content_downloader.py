# module1/content_downloader.py
# This module provides a function to download content from a given URL using the requests library.

# This module benefits from the Single Responsibility SOLID principle
## According to the SRP, a class or module should have only one reason to change (a single responsibility).
### The content_down function has a single responsibilty: to download text from a given URL using the reqeusts library.
#### By following the SRP, my code is not only more modular and maintainable, but it will also make my code easier to understand, test, or modify in the future.

# Input:
    # The given URL to download content from pulled from a text file

# Output:
    # The downloaded content as text, or a print message indicating failure if the download fails


# Importing the requests library to make HTTP requests
import requests

# Function to download content from a given URL
def content_down(url):
    try:
        # Sending a GET request to the URL and store the response
        response = requests.get(url)
        
        # Raising an exception for HTTP errors
        response.raise_for_status()
        # Returning the text content of the response
        return response.text
    
    # Catching any Request Exceptions
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch URL: {url}")
        return None