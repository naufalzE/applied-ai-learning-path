# INPUT nama

# Hapus spasi awal/akhir

# Normalisasi spasi

# Buat Title Case

# Buat UPPERCASE

# Tampilkan hasil

def cleaner(data):
    kata_kata = data.strip().title().split()
    print(kata_kata)
    displayname = " ".join(kata_kata)
    print(displayname)
    print_name = displayname.upper()
    return displayname, print_name

data_nama = input("masukan nama : ")
display_name,print_name = cleaner(data_nama)
print(f"display name    : {display_name}")
print(f"print name    : {print_name}")