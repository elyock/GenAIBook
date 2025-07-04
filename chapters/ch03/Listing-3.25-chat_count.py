import os
from openai import AzureOpenAI
import tiktoken
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

system_message = {"role": "system", "content": "You are a helpful assistant."}
max_response_tokens = 250
token_limit = 4096
conversation: list[dict[str, str]] = []
conversation.append(system_message)

def num_tokens_from_messages(messages: list[dict[str, str]]) -> int:
    encoding= tiktoken.get_encoding("cl100k_base")
    num_tokens = 0
    for message in messages:
        num_tokens += 4           # every message follows <im_start>{role/name}\n{content}<im_end>\n
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":     # if there's a name, the role is omitted
                num_tokens += -1  # role is always required and always 1 token
    num_tokens += 2               # every reply is primed with <im_start>assistant
    return num_tokens

print("I am a helpful assistant. I can talk about pets and salons. What would you like to talk about?")

while True:
    user_input = input("")     
    conversation.append({"role": "user", "content": user_input})
    conv_history_tokens = num_tokens_from_messages(conversation)

    while conv_history_tokens + max_response_tokens >= token_limit:
        del conversation[1] 
        conv_history_tokens = num_tokens_from_messages(conversation)

    response = client.chat.completions.create(
        model=GPT_MODEL,
        messages=conversation, # type: ignore
        temperature=0.8,
        max_tokens=max_response_tokens)

    assistant_content = response.choices[0].message.content or ""
    conversation.append({"role": "assistant", "content": assistant_content})
    print("\n" + assistant_content)
    print("(Tokens used: " + str(response.usage.total_tokens)  + ")") # type: ignore
    
