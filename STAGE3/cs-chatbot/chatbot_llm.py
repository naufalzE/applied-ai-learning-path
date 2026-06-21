import os
import json
import re
from openai import OpenAI
from dotenv import load_dotenv
from better_profanity import profanity

# SETUP

BASE_URL = "https://api.xiaomimimo.com/v1"

load_dotenv()
client = OpenAI(api_key=os.getenv("MIMO_API_KEY"), base_url=BASE_URL)
profanity.load_censor_words()
chat_histories: dict[str, list] = {}


# SUBSYSTEM 1 — INPUT HANDLER

# FUNCTION input_handler(user_input):
#     IF LENGTH(user_input.text) > 1000 THEN
#         RETURN { "valid": False, "rejection_reason": "too_long" }
#     IF LENGTH(user_input.text) < 3 THEN
#         RETURN { "valid": False, "rejection_reason": "too_short" }
#     IF DETECT_HARMFUL_CONTENT(user_input.text) THEN
#         RETURN { "valid": False, "rejection_reason": "toxic" }
#     IF POLITICAL_SENSITIVITY_CHECK(user_input.text) THEN
#         RETURN { "valid": False, "rejection_reason": "political" }
#     IF DETECT_PROMPT_INJECTION(user_input.text) THEN
#         RETURN { "valid": False, "rejection_reason": "injection" }
#     SAVE_TO_HISTORY(session_id, user_id, text)
#     RETURN { "valid": True, "cleaned_text", "user_id", "session_id" }
# END FUNCTION

POLITICAL_KEYWORDS = [
    "presiden", "parlemen", "partai", "politik", "pemilu", "kampanye"
]

INJECTION_PATTERNS = [
    r"ignore previous instructions",
    r"ignore all instructions",
    r"forget your instructions",
    r"you are now",
    r"act as",
    r"pretend you are",
    r"jangan ikuti instruksi",
    r"abaikan instruksi",
    r"lupakan instruksi"
]


def input_handler(user_input: dict) -> dict:

    text = user_input["text"]

    # 1. Validasi panjang
    if len(text) > 1000:
        return {"valid": False, "rejection_reason": "too_long"}

    if len(text) < 3:
        return {"valid": False, "rejection_reason": "too_short"}

    # 2. Deteksi konten berbahaya
    if profanity.contains_profanity(text):
        return {"valid": False, "rejection_reason": "toxic"}

    # 3. Deteksi konten politik
    text_lower = text.lower()
    if any(keyword in text_lower for keyword in POLITICAL_KEYWORDS):
        return {"valid": False, "rejection_reason": "political"}

    # 4. Deteksi prompt injection
    if any(re.search(pattern, text_lower) for pattern in INJECTION_PATTERNS):
        return {"valid": False, "rejection_reason": "injection"}

    # 5. Simpan ke chat history
    session_id = user_input["session_id"]
    if session_id not in chat_histories:
        chat_histories[session_id] = []

    chat_histories[session_id].append({
        "role"   : "user",
        "content": text
    })

    # 6. Return valid
    return {
        "valid"       : True,
        "cleaned_text": text,
        "user_id"     : user_input["user_id"],
        "session_id"  : session_id
    }


# SUBSYSTEM 2 — LLM ENGINE

# FUNCTION llm_engine(validated_input):
#     SET chat_history = GET_CHAT_HISTORY(validated_input.session_id)
#     SET system_prompt = BUILD_SYSTEM_PROMPT(role, domain, format, language)
#     SET combined_input = [system_prompt] + chat_history + [user_message]
#     SET raw_response = CALL_LLM_API(model, combined_input)
#     IF raw_response IS NULL THEN
#         RETURN { "success": False, "error": "api_timeout" }
#     SAVE_TO_HISTORY(session_id, "model", raw_text)
#     RETURN { "success": True, "raw_text": raw_text }
# END FUNCTION

SYSTEM_PROMPT = """Kamu adalah CS assistant toko online.

Tugasmu hanya membantu pelanggan dengan:
- Status pesanan
- Pengembalian barang
- Jadwal pengiriman

Jangan menjawab pertanyaan di luar topik tersebut.

Jawab dalam Bahasa Indonesia formal.

Output WAJIB dalam format JSON seperti ini:
{
    "status": "success" atau "failed",
    "message": "jawaban kamu di sini",
    "action_required": true atau false
}

Jangan tambahkan teks apapun di luar JSON."""


def llm_engine(validated_input: dict) -> dict:

    session_id = validated_input["session_id"]

    # Ambil chat history
    chat_history = chat_histories.get(session_id, [])

    # User message SUDAH ada di history
    combined_input = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ] + chat_history

    try:

        print("\n PAYLOAD KE MODEL ")
        print(json.dumps(combined_input, indent=2, ensure_ascii=False))
        print("\n")

        raw_response = client.chat.completions.create(
            model="mimo-v2.5-pro",
            messages=combined_input
        )

        raw_text = raw_response.choices[0].message.content

    except Exception as e:

        print(f"Error calling LLM API: {e}")

        return {
            "success": False,
            "error": "api_timeout"
        }

    # Simpan jawaban model ke history
    chat_histories[session_id].append({
        "role": "assistant",
        "content": raw_text
    })

    return {
        "success": True,
        "raw_text": raw_text
    }

# SUBSYSTEM 3 — OUTPUT VALIDATOR

# FUNCTION output_validator(raw_response, validated_input):
#     SET retry_count = 0, max_retry = 3
#     WHILE retry_count < max_retry:
#         SET json_clean_str = AUTO_CLEAN(raw_response)
#         IF NOT IS_VALID_JSON → BUILD_CORRECTION_PROMPT(invalid_json) → retry
#         IF NOT VALIDATE_SCHEMA → BUILD_CORRECTION_PROMPT(invalid_schema) → retry
#         IF NOT SEMANTIC_CHECK → BUILD_CORRECTION_PROMPT(invalid_semantic) → retry
#         RETURN { "valid": True, "data": parsed }
#     RETURN { "valid": False, "data": None }
# END FUNCTION

EXPECTED_SCHEMA    = {"status", "message", "action_required"}
VALID_STATUS_VALUES = {"success", "failed", "fallback"}


def auto_clean(raw_text: str) -> str:
    cleaned = re.sub(r"```json|```", "", raw_text).strip()
    match   = re.search(r"\{.*\}", cleaned, re.DOTALL)
    return match.group(0) if match else cleaned


def call_llm_api(prompt: str) -> str | None:
    try:
        completion = client.chat.completions.create(
            model="mimo-v2.5-pro",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
    except Exception:
        return None


def output_validator(raw_response: str, validated_input: dict) -> dict:

    retry_count = 0
    max_retry   = 3

    while retry_count < max_retry:

        # 1. Auto clean
        json_clean_str = auto_clean(raw_response)

        # 2. Parse JSON
        try:
            parsed = json.loads(json_clean_str)
        except json.JSONDecodeError:
            correction = (
                f"Output sebelumnya bukan JSON valid.\n"
                f"JSON rusak:\n{json_clean_str}\n"
                f"Perbaiki menjadi JSON valid. Hanya output JSON saja."
            )
            raw_response = call_llm_api(correction)
            retry_count += 1
            continue

        # 3. Validasi schema
        if not EXPECTED_SCHEMA.issubset(parsed.keys()):
            missing    = EXPECTED_SCHEMA - parsed.keys()
            correction = (
                f"Output tidak memiliki field yang dibutuhkan: {missing}.\n"
                f"Output saat ini:\n{json_clean_str}\n"
                f"Tambahkan field yang kurang. Hanya output JSON saja."
            )
            raw_response = call_llm_api(correction)
            retry_count += 1
            continue

        # 4. Semantic check
        if parsed["status"] not in VALID_STATUS_VALUES:
            correction = (
                f"Field 'status' memiliki nilai tidak valid: {parsed['status']}.\n"
                f"Nilai yang valid adalah: {VALID_STATUS_VALUES}.\n"
                f"Perbaiki nilai 'status'. Hanya output JSON saja."
            )
            raw_response = call_llm_api(correction)
            retry_count += 1
            continue

        # 5. Return success
        return {
            "valid": True,
            "data" : parsed
        }

    # 6. Retry habis
    return {
        "valid": False,
        "data" : None
    }


# SUBSYSTEM 4 — FALLBACK HANDLER

# FUNCTION fallback_handler(reason):
#     IF reason IS "too_short" → RETURN { status: fallback, action_required: user }
#     IF reason IS "too_long"  → RETURN { status: fallback, action_required: user }
#     IF reason IS "toxic"     → RETURN { status: fallback, action_required: user }
#     IF reason IS "political" → RETURN { status: fallback, action_required: user }
#     IF reason IS "injection" → RETURN { status: fallback, action_required: user }
#     IF reason IS "api_timeout" → RETURN { status: fallback, action_required: system }
#     IF reason IS "max_retry"   → RETURN { status: fallback, action_required: system }
#     DEFAULT → RETURN { status: fallback, action_required: system }
# END FUNCTION

FALLBACK_MESSAGES = {
    "too_short" : ("Pesan terlalu pendek. Mohon masukkan pesan yang lebih jelas.",                          "user"),
    "too_long"  : ("Pesan terlalu panjang. Mohon masukkan pesan dengan maksimal 1000 karakter.",            "user"),
    "toxic"     : ("Pesan mengandung konten berbahaya. Mohon hindari bahasa yang kasar atau menyerang.",    "user"),
    "political" : ("Pesan mengandung konten sensitif politik. Mohon hindari topik politik.",                "user"),
    "injection" : ("Pesan terdeteksi mengandung upaya prompt injection. Mohon hindari pola mencurigakan.", "user"),
    "api_timeout": ("Maaf, terjadi gangguan pada layanan. Silakan coba lagi nanti.",                       "system"),
    "max_retry" : ("Maaf, kami mengalami kesulitan memproses permintaan Anda. Silakan coba lagi nanti.",   "system"),
}


def fallback_handler(reason: str) -> dict:

    message, action_required = FALLBACK_MESSAGES.get(
        reason,
        (f"Terjadi kesalahan: {reason}. Silakan coba lagi.", "system")
    )

    return {
        "status"          : "fallback",
        "message"         : message,
        "action_required" : action_required
    }


# SUBSYSTEM 5 — RESPONSE BUILDER

# FUNCTION response_builder(output):
#     IF output.action_required IS "system" THEN
#         RETURN { "http_status": 503, "body": output }
#     ELSE
#         RETURN { "http_status": 200, "body": output }
#     END IF
# END FUNCTION

def response_builder(output: dict) -> dict:

    http_status = 503 if output.get("action_required") == "system" else 200

    return {
        "http_status": http_status,
        "body"       : output
    }


# MAIN — ORCHESTRATOR

# FUNCTION main(user_input):
#     SET validated_input = input_handler(user_input)
#     IF NOT validated_input.valid → fallback + return
#     SET llm_output = llm_engine(validated_input)
#     IF NOT llm_output.success → fallback + return
#     SET validation_output = output_validator(llm_output.raw_text, validated_input)
#     IF NOT validation_output.valid → fallback + return
#     RETURN response_builder(success output)
# END FUNCTION

def main(user_input: dict) -> dict:

    # Input validation
    validated_input = input_handler(user_input)

    if not validated_input["valid"]:

        fallback_output = fallback_handler(
            validated_input["rejection_reason"]
        )

        return response_builder(fallback_output)

    # LLM Engine
    llm_output = llm_engine(validated_input)

    if not llm_output["success"]:

        fallback_output = fallback_handler(
            llm_output["error"]
        )

        return response_builder(fallback_output)

    # Output Validator
    validation_output = output_validator(
        llm_output["raw_text"],
        validated_input
    )

    if not validation_output["valid"]:

        fallback_output = fallback_handler("max_retry")

        return response_builder(fallback_output)

    # Success
    return response_builder(
        validation_output["data"]
    )

import uuid

def chat_cli():

    print("Chat dimulai.")
    print("Ketik /exit untuk keluar")
    print("Ketik /reset untuk reset history")

    session_id = str(uuid.uuid4())

    while True:

        text = input("You: ").strip()

        if not text:
            continue

        if text == "/exit":

            print("Chat selesai.")
            break

        if text == "/reset":

            chat_histories.pop(session_id, None)

            print("History direset.")
            continue

        user_input = {
            "text": text,
            "user_id": "cli_user",
            "session_id": session_id
        }

        result = main(user_input)

        print(
            json.dumps(
                result["body"],
                indent=2,
                ensure_ascii=False
            )
        )

if __name__ == "__main__":
    chat_cli()
