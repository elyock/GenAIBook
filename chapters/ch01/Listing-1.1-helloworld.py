# Listing: 1.1 - Basic Hello World example using the OpenAI API

import os
from dotenv import load_dotenv
from openai import OpenAI, api_key

load_dotenv()

# Define the model to use
GPT_MODEL = "gpt-3.5-turbo"

key = os.getenv("OPENAI_API_BOOK_KEY")
client = OpenAI(api_key=key)

# Generate English text
response_english = client.chat.completions.create(
    model=GPT_MODEL,
    messages=[
      {
        "role": "user",
        "content": "Hello, World!"
      }
    ],
    max_tokens=50
)
english_text = response_english.choices[0].message.content.strip()
print(english_text)

# Translate English text to French
response_french = client.chat.completions.create(
    model=GPT_MODEL,
    
    messages=[
      {
        "role": "user",
        "content": "Translate the following English text to French: " + english_text
      }
    ],
    max_tokens=100
)
# This prints the translation to French
print(response_french.choices[0].message.content.strip())
