from openai import OpenAI
from dotenv import load_dotenv
import os
import time

# load env
load_dotenv()

api_key = os.getenv("MIMO_API_KEY")

if not api_key:
    raise ValueError("MIMO_API_KEY tidak ditemukan")

# client MiMo
client = OpenAI(
    api_key=os.getenv("MIMO_API_KEY"),
    base_url="https://api.xiaomimimo.com/v1"
)

SYSTEM_PROMPT = (
    "kamu adalah seorang asisten, "
    "bantu saya menjelaskan apa itu python max 10 kata"
)

chat_history = []

MODEL = "mimo-v2.5-pro"


def prompt_builder(system_prompt, chat_history, user_message):
    """
    membangun format messages untuk API
    """
    messages = []

    messages.append({
        "role": "system",
        "content": system_prompt
    })

    messages.extend(chat_history)

    messages.append({
        "role": "user",
        "content": user_message
    })

    return messages


def api_handler(model_name, messages):

    for attempt in range(3):

        try:

            response = client.chat.completions.create(
                model=model_name,
                messages=messages,
                max_completion_tokens=1024,
                temperature=0.7,
                top_p=0.95
            )
            print("\n===== TOKEN USAGE =====")
            print(response.usage)
            print("=======================\n")
            return response.choices[0].message.content

        except Exception as e:

            print(f"Error: {e}")

            if attempt < 2:
                print("Mencoba ulang...")
                time.sleep(2)

    return None


def history_handler(chat_history, user_message, response):

    # simpan user message
    chat_history.append({
        "role": "user",
        "content": user_message
    })

    # simpan response assistant
    chat_history.append({
        "role": "assistant",
        "content": response
    })

    max_history = 10

    # batasi history
    if len(chat_history) > max_history * 2:

        del chat_history[:2]

        print(f"[DEBUG] Panjang history: {len(chat_history)}")


def main():

    print("Chat dimulai.")
    print("Ketik /exit untuk keluar")
    print("Ketik /reset untuk reset history")

    while True:

        user_message = input("You: ").strip()

        if not user_message:

            print("Pesan tidak boleh kosong.")
            continue

        if user_message == "/exit":

            print("Chat selesai.")
            break

        elif user_message == "/reset":

            chat_history.clear()
            print("History direset.")

        else:

            messages = prompt_builder(
                SYSTEM_PROMPT,
                chat_history,
                user_message
            )

            start_time = time.time()

            response = api_handler(
                MODEL,
                messages
            )

            if response is None:

                print(
                    "Gagal mendapatkan respon "
                    "dari model setelah beberapa percobaan."
                )

                continue

            print(f"AI: {response}")

            end_time = time.time()

            print(
                f"Waktu respon: "
                f"{end_time - start_time:.2f} detik"
            )

            history_handler(
                chat_history,
                user_message,
                response
            )


if __name__ == "__main__":
    main()
