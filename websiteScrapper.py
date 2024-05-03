# This program contains the class ScrapeArticle which uses programs from modules 1,2, and 3
# Inside the first with open function you're going to place your text file containing the aritcles
# This will go through each web article url in the file and create a ScrapeArticle object.
# Then run the scrape_article function on each object. 

try:
    from module_1 import scrapper as websiteScrap
    from module_2 import file_handling as fileHandler
    from module_3 import ai_processor as aiProcessor 
except ImportError as e:
    print(f"Error importing module: {e}")

class ScrapeArticle:
    def __init__(self,url):
        self.url = url

    def scrape_article(self):
        # Checking if articles are scrapped correctly
        try:
            # This first part is using the python program form module 1
            # Takes in a url and then extracts the article text from the website
            file = websiteScrap.BeautifulSoupScrapper()
            file.requestURL(self.url)
            article_text = file.extract()
            
            # This uses module 2 to write the newly processed article text to a new file inside the processed folder were its just the single string of the article text
            filehandler = fileHandler.FileHandling(article_text,self.url)
            filehandler.writeToProcessed()

            # This uses module 3 to send the single string containing the article text and sends it over to a LLM using the openai API
            # This will return a new string containg a concised version of the article with a new title
            concise = aiProcessor.LLMConciser(article_text)
            concised_article_text = concise.generate_concise_description()

            # This uses module 2 again to write the concised article to a new file inside the concised folder
            filehandler.getArticle(concised_article_text)
            filehandler.writeToConcised()
        except Exception as e:
            print(f"Error scraping article from {self.url}: {e}")
#Test if the articles.text file was read in correctly
try:
    # This is where you will put your article text file, the Data/raw/ is there because you should save your article text file inside the raw folder
    with open('Data/raw/articles.text', 'r') as file:
        urls = file.readlines()
except IOError as e:
    print(f"Error reading file: {e}")

for url in urls:
    article = ScrapeArticle(url.strip())
    article.scrape_article()