import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

aoai_endpoint = os.getenv("AOAI_GPT-35-TURBO_ENDPOINT")
aoai_key = os.getenv("AOAI_GPT-35-TURBO_KEY")

if aoai_endpoint is None or aoai_key is None:
    raise ValueError("AOAI environment variables must be set.")

client = AzureOpenAI(
    azure_endpoint= aoai_endpoint,
    api_version="2024-12-01-preview",
    api_key=aoai_key
)

GPT_MODEL = "gpt-35-turbo"

prompt_startphrase = "Definition: A \"whatpu\" is a small, furry animal native to Tanzania. \nExample: We were traveling in Africa and we saw these very cute whatpus.\n\nDefinition: To do a \"farduddle\" means to jump up and down really fast. \nExample: One day when I was playing tag with my little sister, she got really excited and she started doing these crazy farduddles.\n\nDefinition: A \"yalubalu\" is a type of vegetable that looks like a big pumpkin. \nExample:"

response = client.chat.completions.create(
    model=GPT_MODEL,
    messages=[
        {"role": "user", "content": prompt_startphrase}
    ],
    temperature=0.8,
    max_tokens=100)
responsetext = response.choices[0].message.content

print("Prompt:" + prompt_startphrase + "\nResponse:" + (responsetext or ""))
