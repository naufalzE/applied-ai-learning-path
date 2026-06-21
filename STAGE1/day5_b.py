# Soal 2 — If Else + String

# Input nama peserta.

# Aturan:

# Jika panjang nama < 5 karakter → tampilkan "Nama terlalu pendek".
# Jika tidak → tampilkan nama yang sudah dibersihkan.

# Buat IPO dan pseudocode.
# input nama
def cleaner(data):
    kata_kata = data.strip().title().split()
    displayname = " ".join(kata_kata)
    print_name = displayname.upper()
    return displayname, print_name

while True:
    data_peserta = input("MASUKAN NAMA PESERTA   :")
    display_name,print_name = cleaner(data_peserta)
    if len(display_name) < 5:
        print("data peserta kurang dari 5 input ulang kembali")
        continue
    else:
        display_name,print_name = cleaner(data_peserta)
        print(f"display name    : {display_name}")
        print(f"print name      : {print_name}")
        break