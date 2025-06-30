import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_BOOK_KEY"))


def get_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        model="text-embedding-ada-002",
        input=text)
    return response.data[0].embedding

embeddings = get_embedding("I have a white dog named Champ.")
print("Embedding Length:", len(embeddings))
print("Embedding:", embeddings[:5])
