// ============================================================
// SUBSYSTEM 1 — INPUT HANDLER
// ============================================================

FUNCTION input_handler(user_input):

    // 1. Validasi panjang
    IF LENGTH(user_input.text) > 1000 THEN
        RETURN { "valid": False, "rejection_reason": "too_long" }
    END IF

    IF LENGTH(user_input.text) < 3 THEN
        RETURN { "valid": False, "rejection_reason": "too_short" }
    END IF

    // 2. Deteksi konten berbahaya
    IF DETECT_HARMFUL_CONTENT(user_input.text) THEN
        RETURN { "valid": False, "rejection_reason": "toxic" }
    END IF

    IF POLITICAL_SENSITIVITY_CHECK(user_input.text) THEN
        RETURN { "valid": False, "rejection_reason": "political" }
    END IF

    IF DETECT_PROMPT_INJECTION(user_input.text) THEN
        RETURN { "valid": False, "rejection_reason": "injection" }
    END IF

    // 3. Simpan chat history
    SAVE_TO_HISTORY(
        session_id : user_input.session_id,
        user_id    : user_input.user_id,
        text       : user_input.text
    )

    // 4. Return valid
    RETURN {
        "valid"        : True,
        "cleaned_text" : user_input.text,
        "user_id"      : user_input.user_id,
        "session_id"   : user_input.session_id
    }

END FUNCTION


// ============================================================
// SUBSYSTEM 2 — LLM ENGINE
// ============================================================

FUNCTION llm_engine(validated_input):

    // 1. Ambil chat history
    SET chat_history = GET_CHAT_HISTORY(validated_input.session_id)

    // 2. Konstruksi system prompt
    SET system_prompt = BUILD_SYSTEM_PROMPT(
        role     : "CS assistant toko online",
        domain   : "status pesanan, pengembalian, jadwal pengiriman",
        format   : "JSON {status, message, action_required}",
        language : "Bahasa Indonesia formal"
    )

    // 3. Gabungkan system prompt + history + input
    SET combined_input = [system_prompt] + chat_history + [
        {
            "role"    : "user",
            "content" : validated_input.cleaned_text
        }
    ]

    // 4. Panggil API model
    SET raw_response = CALL_LLM_API(
        model : "mimo-v2.5-pro",
        input : combined_input
    )

    // 5. Handle API error
    IF raw_response IS NULL THEN
        RETURN { "success": False, "error": "api_timeout" }
    END IF

    // 6. Simpan response model ke history
    SAVE_TO_HISTORY(
        session_id : validated_input.session_id,
        user_id    : "model",
        text       : raw_response.text
    )

    // 7. Return
    RETURN {
        "success" : True,
        "raw_text": raw_response.text
    }

END FUNCTION


// ============================================================
// SUBSYSTEM 3 — OUTPUT VALIDATOR
// ============================================================

FUNCTION output_validator(raw_response, validated_input):

    // 0. Inisialisasi retry
    SET retry_count = 0
    SET max_retry   = 3

    WHILE retry_count < max_retry:

        // 1. Auto clean
        SET json_clean_str = AUTO_CLEAN(raw_response)

        // 2. Parse JSON
        IF NOT IS_VALID_JSON(json_clean_str) THEN
            SET correction_prompt = BUILD_CORRECTION_PROMPT(
                type   : "invalid_json",
                broken : json_clean_str
            )
            SET raw_response = CALL_LLM_API(
                model : "mimo-v2.5-pro",
                input : correction_prompt
            )
            SET retry_count  = retry_count + 1
            CONTINUE
        END IF

        // 3. Validasi schema
        IF NOT VALIDATE_SCHEMA(json_clean_str, expected_schema) THEN
            SET correction_prompt = BUILD_CORRECTION_PROMPT(
                type   : "invalid_schema",
                data   : json_clean_str,
                schema : expected_schema
            )
            SET raw_response = CALL_LLM_API(
                model : "mimo-v2.5-pro",
                input : correction_prompt
            )
            SET retry_count  = retry_count + 1
            CONTINUE
        END IF

        // 4. Semantic check
        IF NOT SEMANTIC_CHECK(json_clean_str, validated_input) THEN
            SET correction_prompt = BUILD_CORRECTION_PROMPT(
                type   : "invalid_semantic",
                input  : validated_input.cleaned_text,
                output : json_clean_str
            )
            SET raw_response = CALL_LLM_API(
                model : "mimo-v2.5-pro",
                input : correction_prompt
            )
            SET retry_count  = retry_count + 1
            CONTINUE
        END IF

        // 5. Return success
        RETURN {
            "valid" : True,
            "data"  : PARSE_JSON(json_clean_str)
        }

    END WHILE

    // 6. Retry habis — trigger fallback
    RETURN {
        "valid" : False,
        "data"  : None
    }

END FUNCTION


// ============================================================
// SUBSYSTEM 4 — FALLBACK HANDLER
// ============================================================

FUNCTION fallback_handler(reason):

    IF reason IS "too_short" THEN
        RETURN {
            "status"          : "fallback",
            "message"         : "Pesan terlalu pendek. Mohon masukkan pesan yang lebih jelas.",
            "action_required" : "user"
        }
    END IF

    IF reason IS "too_long" THEN
        RETURN {
            "status"          : "fallback",
            "message"         : "Pesan terlalu panjang. Mohon masukkan pesan dengan maksimal 1000 karakter.",
            "action_required" : "user"
        }
    END IF

    IF reason IS "toxic" THEN
        RETURN {
            "status"          : "fallback",
            "message"         : "Pesan mengandung konten berbahaya. Mohon hindari bahasa yang kasar atau menyerang.",
            "action_required" : "user"
        }
    END IF

    IF reason IS "political" THEN
        RETURN {
            "status"          : "fallback",
            "message"         : "Pesan mengandung konten sensitif politik. Mohon hindari topik politik.",
            "action_required" : "user"
        }
    END IF

    IF reason IS "injection" THEN
        RETURN {
            "status"          : "fallback",
            "message"         : "Pesan terdeteksi mengandung upaya prompt injection. Mohon hindari pola yang mencurigakan.",
            "action_required" : "user"
        }
    END IF

    IF reason IS "api_timeout" THEN
        RETURN {
            "status"          : "fallback",
            "message"         : "Maaf, terjadi gangguan pada layanan. Silakan coba lagi nanti.",
            "action_required" : "system"
        }
    END IF

    IF reason IS "max_retry" THEN
        RETURN {
            "status"          : "fallback",
            "message"         : "Maaf, kami mengalami kesulitan memproses permintaan Anda. Silakan coba lagi nanti.",
            "action_required" : "system"
        }
    END IF

    // Default — reason tidak dikenal
    RETURN {
        "status"          : "fallback",
        "message"         : "Terjadi kesalahan: " + reason + ". Silakan coba lagi.",
        "action_required" : "system"
    }

END FUNCTION


// ============================================================
// SUBSYSTEM 5 — RESPONSE BUILDER
// ============================================================

FUNCTION response_builder(output):

    IF output.action_required IS "system" THEN
        RETURN {
            "http_status" : 503,
            "body"        : output
        }
    ELSE
        RETURN {
            "http_status" : 200,
            "body"        : output
        }
    END IF

END FUNCTION


// ============================================================
// MAIN — ORCHESTRATOR
// ============================================================

FUNCTION main(user_input):

    // 1. Jalankan input_handler
    SET validated_input = input_handler(user_input)

    // 2. Cek validasi input
    IF NOT validated_input.valid THEN
        SET fallback_output = fallback_handler(validated_input.rejection_reason)
        RETURN response_builder(fallback_output)
    END IF

    // 3. Jalankan llm_engine
    SET llm_output = llm_engine(validated_input)

    // 4. Cek hasil llm_engine
    IF NOT llm_output.success THEN
        SET fallback_output = fallback_handler(llm_output.error)
        RETURN response_builder(fallback_output)
    END IF

    // 5. Jalankan output_validator
    SET validation_output = output_validator(llm_output.raw_text, validated_input)

    // 6. Cek hasil output_validator
    IF NOT validation_output.valid THEN
        SET fallback_output = fallback_handler("max_retry")
        RETURN response_builder(fallback_output)
    END IF

    // 7. Return success
    RETURN response_builder({
        "status"          : "success",
        "message"         : validation_output.data.message,
        "action_required" : "none"
    })

END FUNCTION