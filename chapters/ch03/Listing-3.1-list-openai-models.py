# Variant of Listing 3.1 - list models available in OpenAI for the current organization

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_BOOK_KEY"))

# Call the models API to retrieve a list of available models
models = client.models.list()

# debug output - show response
# print(models)

# save to file
with open('oai-models.json', 'w') as file:
    file.write(str(models))

# Print out the organization that owns the models
for model in models.data:
    print("ID:", model.id)
    print("Model owned by:", model.owned_by)
    print("-------------------")