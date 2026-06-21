# CS Chatbot LLM

Chatbot Customer Service berbasis Large Language Model (LLM) yang berjalan melalui Command Line Interface (CLI). Sistem dirancang untuk menangani pertanyaan pelanggan terkait status pesanan, pengembalian barang, dan jadwal pengiriman.

## Features

* Input validation
* Profanity filtering
* Political content filtering
* Prompt injection detection
* Session-based conversation history
* JSON response validation
* Automatic response correction
* Fallback handling for invalid responses and system errors

## Requirements

* Python 3.11+
* MIMO API Key

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd cs-chatbot
```

### Create Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
MIMO_API_KEY=your_api_key_here
```

Example:

```env
MIMO_API_KEY=xxxxxxxxxxxxxxxx
```

> Do not commit `.env` files to source control.

## Usage

Run the chatbot:

```bash
python chatbot_llm.py
```

Example:

```text
Chat dimulai.
Ketik /exit untuk keluar
Ketik /reset untuk reset history

You: Status pesanan saya bagaimana?
{
  "status": "success",
  "message": "Pesanan Anda sedang diproses.",
  "action_required": false
}
```

## CLI Commands

| Command  | Description                   |
| -------- | ----------------------------- |
| `/exit`  | Exit application              |
| `/reset` | Reset current session history |

## Project Structure

```text
cs-chatbot/
├── chatbot_llm.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

## Response Format

All chatbot responses are returned in JSON format:

```json
{
  "status": "success",
  "message": "Response message",
  "action_required": false
}
```

### Fields

| Field           | Description                                  |
| --------------- | -------------------------------------------- |
| status          | Response status                              |
| message         | Response message                             |
| action_required | Indicates whether further action is required |

## Dependencies

* openai
* python-dotenv
* better-profanity

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Notes

* Conversation history is stored in memory and will be lost when the application stops.
* Responses are restricted to customer service topics.
* Invalid model outputs are automatically corrected up to three attempts.
* If validation fails after all retries, the system returns a fallback response.

## License

All rights reserved.
