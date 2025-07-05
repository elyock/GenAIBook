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

conversation=[{"role": "system", "content": "You are an AI assistant that helps people find information. You can only talk about pets and nothing else. If you don't know the answer, say, \"Sorry bud, I don't know that.\" And if you cannot answer it, say \"Sorry mate, can't answer that - I am not allowed to\"."}]
print("Please enter what you want to talk about:\n")

while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        break
    
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model = GPT_MODEL,
        messages = conversation) # type: ignore

    assistant_content = response.choices[0].message.content or ""
    conversation.append({"role": "assistant", "content": assistant_content})
    print("\nAI:" + assistant_content + "\n")
