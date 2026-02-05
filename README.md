# AI Chat CLI

A simple command-line interface for chatting with AI using OpenAI-compatible APIs.

## Features

- Interactive chat with AI (with persistent conversation history)
- Save chat sessions to JSON files
- Load previous chat sessions
- Clear conversation history
- View current chat history
- Support for any OpenAI-compatible API

## Prerequisites
- Python 3.7 or higher
- An OpenAI-compatible API key

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-chat-cli.git
cd ai-chat-cli
```

### 2. Install dependencies

```bash
pip install openai
```

### 3. Configure your API credentials

Edit the following line to ur needs

```python
API_URL=https://your-api-url.com/v1
API_KEY=your-api-key-here
MODEL_NAME=your-model-name
```

## Usage

Run the program:

```bash
python main.py
```

### Available Commands

| Command | Description |
|---------|-------------|
| `/quit` | Exit the program |
| `/clear` | Clear current chat history |
| `/save` | Save current chat to a JSON file |
| `/list` | List all saved chat files |
| `/load <number>` | Load a saved chat by number (use `/list` to see available chats) |
| `/history` | Display current chat history in JSON format |

### Example Session

```
> Hello, how are you?
AI: Hello! I'm doing well, thank you for asking. How can I help you today?

> /save
Chat saved! You can safely close this terminal now.

> /list
This is the chat list!
['chat_2026-02-05_14-20.json', 'chat_2026-02-05_15-30.json']

> /load 1
Chat loaded!

> /history (Still using the good old 'pretty print')
Here is the history of the chat:
[
  {
    "role": "user",
    "content": "Hello, how are you?"
  },
  {
    "role": "assistant",
    "content": "Hello! I'm doing well..."
  }
]
```

```

