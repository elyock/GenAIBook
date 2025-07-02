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

response = client.chat.completions.create(
    model=GPT_MODEL,
    messages = [
        {"role":"system","content":"You are an AI assistant that helps people find information."},
        {"role":"user","content":"Hello world"},
        {"role":"assistant","content":"Hello! How can I assist you today?"},
        {"role":"user","content":"I want to know more about pets and why dogs are good for humans?"}],
    temperature=0.8,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
)

print(response.choices[0].message.content)
