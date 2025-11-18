import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up API credentials and endpoint
api_key = os.getenv("OPENAI_API_KEY")
url = "https://api.openai.com/v1/chat/completions"

# Initialize conversation history
messages = []
current_thread_id = None  # Not used in OpenAI, but kept for conceptual alignment

while True:
    user_message = input("You: ")
    
    # Add user message to conversation
    messages.append({"role": "user", "content": user_message})
    
    # Send request to OpenAI
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "gpt-3.5-turbo",
        "messages": messages
    }
    
    response = requests.post(url, headers=headers, json=body)
    response_data = response.json()
    
    # Extract assistant's reply
    try:
        latest_message = response_data["choices"][0]["message"]["content"]
    except KeyError:
        print("Error: Unable to retrieve response")
        continue
    
    # Display and store assistant response
    print(f"GPT: {latest_message}")
    messages.append({"role": "assistant", "content": latest_message})   
