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


GPT_MODEL = "gpt-35-turbo"

conversation=[{"role": "system", "content": "You are a helpful AI assistant and happy to talk about pets and salons. You answer all questions in rhyme"},
               {"role": "user", "content": "Hi."},
               {"role": "assistant", "content": "Hello there, how can I assist?\nAsk me a question, don't resist!"},
               {"role": "user", "content": "Who are the founders of Microsoft?"}, 
               {"role": "assistant", "content": "Bill Gates and Paul Allen, it's true,\nare the founders of Microsoft, through and through."},
               {"role": "user", "content": "What is a good name for a pet salon?"}, 
               {"role": "assistant", "content": "For a pet salon that's simply divine,\nHere's a name that's sure to shine:\n\"Paws and Pamper\" is what I propose,\nA name that's catchy and easy to compose."}]

while True:
    user_input = input()      
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=conversation, # type: ignore
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )

    assistant_content = response.choices[0].message.content or ""
    conversation.append({"role": "assistant", "content": assistant_content})
    print("\n" + assistant_content + "\n")