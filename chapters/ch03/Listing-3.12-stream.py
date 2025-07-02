import os
import sys
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

azure_endpoint = os.getenv("AOAI_GPT-35-TURBO_ENDPOINT")
api_key = os.getenv("AOAI_GPT-35-TURBO_KEY")

if not azure_endpoint or not api_key:
    raise ValueError("AOAI environment variables must be set.")

client = AzureOpenAI(
    azure_endpoint=azure_endpoint,
    api_version="2024-12-01-preview",
    api_key=api_key)

# This model name is what you chose when you deployed the model in Azure OpenAI
GPT_MODEL = "gpt-35-turbo"

prompt_startphrase = "Suggest three names and a tagline which is at least 3 sentences for a new pet salon business. The generated name ideas should evoke positive emotions and the following key features: Professional, friendly, Personalized Service."

for response in client.chat.completions.create(
    model=GPT_MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt_startphrase}
    ],
    temperature=0.8,
    max_tokens=500,
    n=1,
    stream=True,
    stop=None):
    for choice in response.choices:
        sys.stdout.write(str(choice.delta.content or "") + "\n")
        sys.stdout.flush()
