import os
from openai import AzureOpenAI
from dotenv import load_dotenv

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

prompt_startphrase = "Translate the following to Spanish: I have a small dog called Champ."

response = client.chat.completions.create(
    model=GPT_MODEL,
    messages=[{"role": "user", "content": prompt_startphrase}],
    temperature=0.8,
    max_tokens=100
)

responsetext = response.choices[0].message.content

print("Prompt:" + prompt_startphrase + "\nResponse:" + (responsetext or ""))
