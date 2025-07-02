import os
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

prompt_startphrase = "Suggest three names for a new pet salon business. The generated name ideas should evoke positive emotions and the following key features: Professional, friendly, Personalized Service."

response = client.chat.completions.create(
    model=GPT_MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt_startphrase}
    ],
    temperature=0.8,
    max_tokens=100,
    logit_bias={
        "30026": -100,
        "81": -100,
        "9330": -100,
        "808": -100,
        "42114": -100,
        "1308": -100,
        "3808": -100,
        "502": -100,
        "322": -100}
    )  
  
responsetext = response.choices[0].message.content
print(responsetext)