# News Scraper and Article Generator in Python

The News Scraper and Article Generator is a Python script that allows one to scrape text content from news articles on the web. It utilizes the `requests` library to fetch HTML content from specified URLs, the `BeautifulSoup` library for HTML parsing, and the OpenAI API (`openai`) for generating concise summaries of news articles. This script can be particularly useful for tasks such as data analysis, building intelligent agents, or simply staying up-to-date with news articles without having to scroll through advertisements.

## How to Use Software

Follow these steps to run the News Scraper:

1. **Clone the Repository**: 
   Clone the repository containing the News Scraper script to your local machine.

2. **Initialize the Virtual Environment**:
   - Open a terminal and navigate to the directory where the News Scraper script is located.
   - Create a virtual environment named "venv" by running:
     ```
     python3 -m venv venv
     ```

3. **Activate the Virtual Environment**:
   - Activate the virtual environment by running:
     - On macOS/Linux:
       ```
       source venv/bin/activate
       ```
     - On Windows:
       ```
       .\venv\Scripts\activate
       ```

4. **Install Dependencies from requirements.yml**:
   - Install dependencies from a requirements.yml file:
     ```
     conda install -n lnitzsc --file requirements.yml
     ```
   - Or install packages by manually (preferred method):
   ```
     pip install requests beautifulsoup4 openai
     ```

5. **Run the Script**:
   - Execute the Python script by running:
     ```
     python3 run.py
     ```
   - (Optional) Create AI-generated Summaries of scraped articles
     ```
     python3 ai.py
     ```

6. **Deactivate the Environment**:
   - Once you're done using the script, deactivate the virtual environment by running:
     ```
     deactivate
     ```

## How to Generate OpenAI API Key

1. **Sign Up for an Account on OpenAI**:
   - Visit the [OpenAI website](https://openai.com) and sign up for an account.

2. **Choose API Module**:
   - After creating an account with OpenAI, you will be prompted with an option to choose between navigating to "ChatGPT" or "API"; choose "API".
   ![Intructions I](images/SETI.png)

3. **Generate an API Key**:
   - After signing up, navigate to the API section in your account settings.
   - Generate an API key that will allow you to make API calls to the OpenAI API.
   ![Intructions II](images/SETII.png)

4. **Use the API Key**:
   - Once you have your API key, you can use it in line 5 of the `ai.py` script to access the OpenAI API for generating concise summaries of news articles.

## Output
Upon successful execution, the script will download the text content from the news articles specified in the 'links.txt' file located in the folder 'Data' and subfolder 'raw'. Furthermore, each article's content will be saved to separate text files named 'news_article_1.txt', 'news_article_2.txt', and so on, to the folder 'Data' and subfolder 'processed'. Additionally, the extracted content from each article will be used to generate summaries using the `openai` API, and these summaries will be saved to separate text files named 'generated_article_1.txt', 'generated_article_2.txt', and so on, to the folder 'Data' and subfolder 'generated'.

By following these steps, you can easily scrape news articles, extract text content, generate summaries using AI, and save the processed data for further analysis or consumption. Ensure to provide valid URLs in the 'links.txt' file for the script to fetch the content properly.
