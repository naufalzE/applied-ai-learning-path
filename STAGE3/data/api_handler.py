from google import genai
from dotenv import load_dotenv
import os
import time
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY tidak ditemukan")

client = genai.Client(api_key=api_key)

def api_handler(prompt, max_retry=3):
    """
    untuk mengirim request ke model dan menerima response dari model
    """
    retry_count = 0
    while retry_count < max_retry:
        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            raw_response = response.text
            return raw_response
        except Exception as e:
            retry_count += 1
            print(f"Error retry {retry_count}: {e}")
            
            if retry_count >= max_retry:
                print(f"API request failed after {max_retry} retries")
                return None
            time.sleep(35)

