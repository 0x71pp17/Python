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
threads = []  # To store thread IDs if extended later

print("Welcome! Type your message and press Enter to send.")
print("Type 'exit' to end the program")
print("Type 'new' to start a new conversation thread.")
print("Starting a new chat session.\n")

while True:
    user_message = input("You: ")
    
    if user_message.lower() == "exit":
        break
    elif user_message.lower() == "new":
        messages = []  # Clear message history for new thread
        print("Started a new conversation thread.")
        continue
    
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
