import cohere
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve Cohere API key from environment variables
cohere_api_key = os.getenv('COHERE_API_KEY')
co = cohere.Client(cohere_api_key)  # Initialize Cohere client

# Function to get advice from chatbot
def get_chatbot_advice(user_goal, message):
    response = co.generate(
        model='command-xlarge-nightly',  # Update the model to an available one
        prompt=f"User Goal: {user_goal}. Question: {message}",
        max_tokens=150,
        temperature=0.5,
    )
    return response.generations[0].text.strip()

