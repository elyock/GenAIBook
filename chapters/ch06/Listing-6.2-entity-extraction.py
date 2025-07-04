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

# Sample input from Chapter 1:
#Hello. My name is Amit Bahree. I’m calling from Acme Insurance, Bellevue, WA. My colleague mentioned that you are interested in learning about our comprehensive benefits policy. Could you give me a call back at (555) 111-2222 when you get a chance so we can go over the benefits? I can be reached Monday to Friday during normal business hours of PST. If you want you can also try and reach me on emails at aweomseinsrance@acme.com. Thanks, Amit.

conversation=[{"role": "system", "content": "You are an AI assistant that extracts entities from text as JSON. \nHere is an example of your output format:\n{  \n   \"the_name\": \"\",\n   \"the_company\": \"\",\n   \"a_phone_number\": \"\"\n}"}]
print("Please enter what you want to talk about:")

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
