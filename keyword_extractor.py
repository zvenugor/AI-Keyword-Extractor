import openai
import os
from dotenv import load_dotenv

# Load API key from the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_keywords(text):
    prompt = f"Extract a list of key topics or keywords from the following text:\n\n{text}\n\nKeywords:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert keyword extractor."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=60
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    input_text = input("Enter text: ")
    keywords = extract_keywords(input_text)
    print("Extracted Keywords:", keywords)
