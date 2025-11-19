import os
import time
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Create assistant (do this once; save ID for reuse)
assistant = client.beta.assistants.create(
    name="Chat Assistant",
    instructions="You are a helpful assistant.",
    model="gpt-3.5-turbo",
)
assistant_id = assistant.id  # Save this to reuse later

# Initialize
threads = []  # Store thread IDs
current_thread_id = None

print("Welcome! Type your message and press Enter to send.")
print("Type 'exit' to end the program")
print("Type 'new' to start a new conversation thread.")
print("Starting a new thread for you.\n")

while True:
    user_message = input("You: ").strip()

    if user_message.lower() == "exit":
        break
    elif user_message.lower() == "new":
        current_thread_id = None
        print("Started a new conversation thread.\n")
        continue

    # Create or use existing thread
    if current_thread_id is None:
        thread = client.beta.threads.create()
        current_thread_id = thread.id
        if current_thread_id not in threads:
            threads.append(current_thread_id)

    # Add message to thread
    client.beta.threads.messages.create(
        thread_id=current_thread_id,
        role="user",
        content=user_message
    )

    # Run assistant
    run = client.beta.threads.runs.create_and_poll(
        thread_id=current_thread_id,
        assistant_id=assistant_id
    )

    # Wait for completion
    while run.status != "completed":
        time.sleep(0.5)
        run = client.beta.threads.runs.retrieve(thread_id=current_thread_id, run_id=run.id)

    # Get and display response
    messages = client.beta.threads.messages.list(thread_id=current_thread_id, order="asc")
    for msg in messages:
        if msg.role == "assistant":
            print(f"GPT: {msg.content[0].text.value}")
            break   
