def input_builder(instruksi, teks_uji):
    """
    Menggabungkan instruksi dan teks uji menjadi prompt untuk di kirim ke fungsi api_handler
    """
    prompt = instruksi + "\n" + teks_uji
    return prompt


if __name__ == "__main__":
    intruksi ="buatkan saya json tanpa ada tambahan teks di luar json "  
    teks_uji =  """json chema contoh """
    hasil = input_builder(intruksi, teks_uji)
    print(hasil)