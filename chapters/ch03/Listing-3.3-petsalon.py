import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

aoai_endpoint = os.getenv("AOAI_GPT-35-TURBO_ENDPOINT")
aoai_key = os.getenv("AOAI_GPT-35-TURBO_KEY")

if aoai_endpoint is None or aoai_key is None:
    raise ValueError("AOAI environment variables must be set.")

client = AzureOpenAI(
    azure_endpoint=aoai_endpoint,
    api_version="2024-12-01-preview",
    api_key=aoai_key
)

GPT_MODEL = "gpt-35-turbo"

prompt_startphrase = "Suggest three names for a new pet salon business. The generated name ideas should evoke positive emotions and the following key features: Professional, friendly, Personalized Service."

response = client.chat.completions.create(
    model=GPT_MODEL,
    messages=[
        {"role": "user", "content": prompt_startphrase}
    ],
    temperature=0.7,
    max_tokens=100,
    #best_of=5,
    n=3,
    stop=None)

responsetext = response.choices[0].message.content
print("Prompt:", prompt_startphrase, "\nResponse:", responsetext)
