import json
from jsonschema import validate, ValidationError
import json
from api_handler import api_handler
from logger import logger

# =====================================
# AUTO CLEAN
# =====================================
def auto_clean(raw_response):
    """
    Membersihkan response model
    TANPA memanggil API lagi
    """

    if not raw_response:
        return None

    raw_response = raw_response.replace("```json", "")
    raw_response = raw_response.replace("```", "")

    start = raw_response.find("{")
    end = raw_response.rfind("}")

    if start == -1 or end == -1:
        return None

    return raw_response[start:end + 1]


# =====================================
# SEMANTIC VALIDATION
# =====================================
def cek_halusinasi(data):

    allowed_sentiment = [
        "positif",
        "negatif",
        "netral"
    ]

    if data["sentiment"] not in allowed_sentiment:
        return True

    if not (0 <= data["score"] <= 100):
        return True

    return False


# =====================================
# VALIDATOR
# =====================================
def validator(raw_response, schema, prompt, max_retry=3):

    retry_count = 0
    last_error = None

    while retry_count < max_retry:

        # =====================================
        # 1. AUTO CLEAN
        # =====================================
        json_clean_str = auto_clean(raw_response)

        if not json_clean_str:

            # AUTO CLEAN TIDAK RETRY API
            return {
                "status": "gagal",
                "alasan": "JSON tidak ditemukan"
            }

        # =====================================
        # 2. PARSE JSON
        # =====================================
        try:

            parsed_json = json.loads(json_clean_str)

        except json.JSONDecodeError as e:

            last_error = f"Invalid JSON: {str(e)}"

            prompt_koreksi = f"""
Output sebelumnya invalid JSON.

JSON Rusak:
{json_clean_str}

Perbaiki agar menjadi JSON valid.
Hanya output JSON saja.
"""

            raw_response = api_handler(prompt_koreksi)

            retry_count += 1

            continue

        # =====================================
        # 3. VALIDASI SCHEMA
        # =====================================
        try:

            validate(
                instance=parsed_json,
                schema=schema
            )

        except ValidationError as e:

            last_error = f"Invalid Schema: {str(e)}"

            prompt_koreksi = f"""
JSON berikut tidak sesuai schema.

JSON:
{json.dumps(parsed_json, indent=2)}

Schema:
{json.dumps(schema, indent=2)}

Error:
{str(e)}

Perbaiki JSON agar sesuai schema.
Hanya output JSON saja.
"""

            raw_response = api_handler(prompt_koreksi)

            retry_count += 1

            continue

        # =====================================
        # 4. HALUSINASI / SEMANTIC CHECK
        # =====================================
        if cek_halusinasi(parsed_json):

            last_error = "Halusinasi terdeteksi"

            prompt_koreksi = f"""
Output berikut mengandung nilai tidak valid.

JSON:
{json.dumps(parsed_json, indent=2)}

Rules:
- sentiment hanya boleh:
  positif / negatif / netral
- score harus antara 0 sampai 100

Perbaiki JSON.
Hanya output JSON saja.
"""

            raw_response = api_handler(prompt_koreksi)

            retry_count += 1

            continue

        # =====================================
        # SUCCESS
        # =====================================
        return {
            "status": "sukses",
            "data": parsed_json
        }

    # =====================================
    # MAX RETRY
    # =====================================
    return {
        "status": "gagal",
        "alasan": last_error,
        "retry": retry_count
    }
import json


if __name__ == "__main__":
    # test dengan data sukses
    test_hasil = {
        "status": "sukses",
        "data": {"sentiment": "positif", "score": 9},
        "retry": 1,
        "alasan": None
    }
    
    report = logger(test_hasil)
    print(report)