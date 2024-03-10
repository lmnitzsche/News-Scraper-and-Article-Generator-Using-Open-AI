# run.py
# This script is the main entry point for downloading and processing using this news scraper

# Importing the content_down function from content_downloader.py file in module1 folder
from module_1.content_downloader import content_down

# Importing the extract_text function from text_extractor.py file in the module1 folder
from module_2.text_extractor import extract_text

def main():
    # Read the URLs from the text file
    with open('Data/raw/links.txt', 'r') as file:
        urls = file.read().splitlines()

    # Iterate through each URL and download/copy/scrape the content
    for idx, url in enumerate(urls):
        print("\nProcessing URL {}: {}".format(idx + 1, url))
        
        # Downloading content from the current URL
        html_content = content_down(url)
        
        # Checking if content was successfully downloaded
        if html_content:
            # Extract and clean the text content from the HTML
            text_content = extract_text(html_content)
            
            # Save the content inside a text file in the Data folder and processed subfolder
            with open('Data/processed/news_article_{}.txt'.format(idx + 1), 'w', encoding='utf-8') as article_file:
                article_file.write(text_content)

    print("\nAll news articles downloaded successfully.")

if __name__ == "__main__":
    main()
