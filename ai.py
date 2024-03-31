import os
import openai

# Setting OpenAI API key (Replace with Created Key)
openai.api_key = "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"

# Function to generate summary articles
def generate_article(prompt):
    # Sending response to OpenAI model and receiving concise article
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"user", "content": "Come up with a compelling title then write a consise article (title: article) up to 50 words summarizing the text present:" + prompt}
        ]
    )
    concise_article = response.choices[0].text.strip()
    return concise_article

# Function to save results
def save_results(file_name, concise_article):
    with open(file_name, "w") as file:
        file.write(concise_article)

if __name__ == "__main__":
    # Creating directory if it doesn't exist
    os.makedirs("Data/generated", exist_ok=True)
    
    # Listing files in the processed data directory
    processed_data_dir = "Data/processed"
    processed_files = os.listdir(processed_data_dir)
    
    # Iterating over each text file
    for i, file_name in enumerate(processed_files, start=1):
        # Reading content from each text file
        with open(os.path.join(processed_data_dir, file_name), "r") as file:
            content = file.read()

        # Prompt for the OpenAI model
        prompt = f"Please make the article concise, up to 50 words, the article is \"{content}\""

        # Generating concise article
        concise_article = generate_article(prompt)

        # Saving results
        generated_file_name = f"Data/generated/generated_article_{i}.txt"
        save_results(generated_file_name, concise_article)
