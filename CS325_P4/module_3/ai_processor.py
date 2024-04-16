# The program contains the LLMConciser class. The class is initialized with an article text
# The class as the function generate_concise_description which will take in an article text
# and put it into a prompt variable where it will ask to make the article concise
#  and give it a title. Using the openai api it will use your api key to send it over
# to chat gpt and generate a response back. The response is saved inot concise_description
#  and is then returned. 

# Importing openai api to allow for text generation based on the data found in "processed"
from openai import OpenAI, ApiError
# Implemnenting "dotenv" to allow for use of api key without making the key public
from dotenv import load_dotenv
# Implementing "os" to allow for use of operating system functionality
import os

# Loading the api key from "dotenv"
load_dotenv()

# Opening OpenAI client
try:
    client = OpenAI(
        # Enter API Key here
        api_key= os.getenv("OPENAI_API_KEY"),
    )
#If there's an error related to the API key (e.g., invalid API key), it catches the ApiError and prints the error message.
except ApiError as e:
        print("API key is invalid:", e)
# If there's any other unexpected error, it catches it using the generic Exception class and prints the error message.
except Exception as e:
     print("An unexpected error occurred:", e)

# Class for generation of new article based on data from the "processed" file in "Data"
class LLMConciser:
    def __init__(self,article_text):
        self.article_text = article_text

    # Generating a consise summary of the article in "processed" that is up to 50 words with a title
    def generate_concise_description(self):
        prompt = f"Generate a title along with the concise descripton up to 50 words of this article: \"{self.article_text}\""

       #Check if the there are any errors when getting the response
        try:
            # This uses openai's completions api to send over the prompt
            response = client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=prompt,
                temperature=1,
                max_tokens=200,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
        except Exception as e:
             print("An error occurred while getting the response:", e)
        # Returns the summary generated using the OpenAI api to the "concised" folder in "Data"
        concise_description = response.choices[0].text
        return concise_description