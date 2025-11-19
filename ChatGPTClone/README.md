# ChatGPT API Chatbot

A simple command-line chatbot that interacts with OpenAI's API, available in two versions.

## Versions

### `Version 1`: Basic Conversation (Simple)
- Uses the **Chat Completions API**
- Maintains conversation history in memory
- Supports `exit` and `new` commands
- No persistent thread IDs
- Ideal for simple, single-session chats

### `Version 2`: Threaded Conversation (Advanced)
- Uses the **Assistants API**
- Creates and tracks real `thread_id`s
- Stores thread IDs in `threads` list for future use
- Fully supports switching or resuming conversations
- Best for advanced use with persistent context

## Features
- Type `exit` to end the program
- Type `new` to start a fresh conversation thread
- Conversation history preserved within each session

## Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install openai python-dotenv
```

## Setup
1. Create a `.env` file in your project directory
2. Add your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

## Usage
Run either script:
```bash
python chatbot_basic.py
# or
python chatbot_threaded.py
```

## Requirements
- Python 3.6+
- `openai` (v1.0+)
- `python-dotenv`

## License
MIT
