# ChatGPT API Chatbot

A simple command-line chatbot that interacts with OpenAI's `gpt-3.5-turbo` model using the Chat Completions API.

## Description
This script enables a continuous conversation with OpenAI's language model by maintaining message history locally. It reads your API key from environment variables and allows real-time chat in the terminal.

## Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install requests python-dotenv
```

## Setup
1. Create a `.env` file in your project directory
2. Add your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

## Usage
Run the script:
```bash
python local_chatbot.py
```
Then type your messages and press Enter to chat.

## Requirements
- Python 3.6+
- `requests`
- `python-dotenv`

## License
MIT

