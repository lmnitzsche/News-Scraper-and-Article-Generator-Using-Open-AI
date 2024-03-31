import os
import openai

# Set your OpenAI API key
openai.api_key = "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"

# Function to send prompt and receive concise article
def generate_concise_article(prompt):
    # Send prompt to OpenAI model and receive concise article
    response = openai.Completion.create(
        engine="text-davinci-003",  # You can change the engine as per your choice
        prompt=prompt,
        max_tokens=50,  # Maximum tokens for the concise article
        temperature=0.5,  # Control randomness of the generated text
        stop="\n"  # Stop generating after a newline character
    )
    concise_article = response.choices[0].text.strip()
    return concise_article

# Function to save results
def save_results(title, concise_article):
    with open("results.txt", "a") as file:
        file.write(f"Title: {title}\n")
        file.write(f"Concise Article: {concise_article}\n\n")

if __name__ == "__main__":
    # List files in the processed data directory
    processed_data_dir = "Data/processed"
    processed_files = os.listdir(processed_data_dir)

    # Iterate over each file
    for file_name in processed_files:
        # Read content from the file
        with open(os.path.join(processed_data_dir, file_name), "r") as file:
            content = file.read()

        # Prompt for the OpenAI model
        prompt = f"Please make the article concise, up to 50 words, the article is \"{content}\""

        # Generate concise article
        concise_article = generate_concise_article(prompt)

        # Save results
        save_results(file_name, concise_article)
