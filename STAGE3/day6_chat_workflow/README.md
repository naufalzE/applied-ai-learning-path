# Chat Workflow dengan LLM

Chat workflow CLI yang memanggil Gemini API dengan menyertakan chat history di setiap request, sehingga percakapan terasa kontekstual dan tidak stateless.

## Requirements

- Python 3.8+
- Google Gemini API key

## Installation

```bash
pip install google-genai python-dotenv
```

Buat file `.env` di folder project:

```
GEMINI_API_KEY=your_api_key_here
```

## Usage

```bash
python chat_workflow.py
```

| Command | Deskripsi |
|---|---|
| `/exit` | Keluar dari program |
| `/reset` | Hapus chat history |

## Project Structure

```
.
├── chat_workflow.py
├── .env
└── README.md
```

## Notes

- History hanya tersimpan di memori dan hilang saat program ditutup
- Maksimal 10 pasang pesan tersimpan di history, pesan lama otomatis dihapus
- Retry otomatis 3x jika API gagal

## Author

NaufalZ