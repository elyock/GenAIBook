# Make sure the following environment variables are set:
# - AOAI_ENDPOINT
# - AOAI_KEY
# For exanple on Windows: setx AOAI_ENDPOINT "https://your-instance-here.openai.azure.com/"

# Listing: 3.1 - List the models available in Azure OpenAI
import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import json

load_dotenv()

aoai_endpoint = os.getenv("AOAI_ENDPOINT")
aoai_key = os.getenv("AOAI_KEY")

if not aoai_endpoint or not aoai_key:
    raise ValueError("Both AOAI_ENDPOINT and AOAI_KEY environment variables must be set.")

client = AzureOpenAI(
    azure_endpoint=aoai_endpoint,
    api_version="2023-05-15",
    api_key=aoai_key
    )

# Call the models API to retrieve a list of available models
models = client.models.list()

# save to file
# Convert each Model object in models to a dictionary before serializing it to JSON.
with open('azure-oai-models.json', 'w') as file:
    models_dict = [model.__dict__ for model in models]
    json.dump(models_dict, file)
    
# Print out the names of all the available models, and their capabilities
for model in models:
    print("ID:", model.id)
    print("Current status:", model.lifecycle_status) # type: ignore (it's str)
    print("Model capabilities:", model.capabilities) # type: ignore (it's str)
    print("-------------------")