# Terima nama pelanggan sebagai input
# Terima harga dan kuantitas untuk 2 barang berbeda
# Hitung subtotal masing-masing barang (harga × kuantitas)
# Hitung total belanja dari kedua subtotal
# Jika total belanja di atas 100.000, berikan diskon 10%
# Hitung harga final setelah diskon
# Terima uang bayar
# Hitung kembalian
# Tampilkan nota yang rapi seperti ini:

# ================================
#        NOTA BELANJA
# ================================
# Pelanggan : Budi
# Barang 1  : Rp 20.000 x 3 = Rp 60.000
# Barang 2  : Rp 15.000 x 4 = Rp 60.000
# --------------------------------
# Total     : Rp 120.000
# Diskon    : Rp 12.000
# Final     : Rp 108.000
# Uang Bayar: Rp 150.000
# Kembalian : Rp 42.000
# ================================

name_customer = input("Masukkan nama pelanggan: ")
harga_barang1 = int(input("Masukkan harga barang 1: "))
kuantitas_barang1 = int(input("masukkan jumlah barang 1: "))

harga_barang2 = int(input("Masukkan harga barang 2: "))
kuantitas_barang2 = int(input("masukkan jumlah barang 2: "))

subtotal_barang1 = harga_barang1* kuantitas_barang1
subtotal_barang2 = harga_barang2* kuantitas_barang2

total_belanja = subtotal_barang1 + subtotal_barang2
uang_bayar = int(input("Masukkan uang bayar: "))
kembalian = uang_bayar - total_belanja
print("===============================")
print("       NOTA BELANJA")
print("===============================")
print("Pelanggan : ", name_customer,sep="")
print("Barang 1  : Rp ", harga_barang1, " x ", kuantitas_barang1, " = Rp ", subtotal_barang1,sep="")
print("Barang 2  : Rp ", harga_barang2, " x ", kuantitas_barang2, " = Rp ", subtotal_barang2,sep="")
print("--------------------------------")
print("Total     : Rp ", total_belanja,sep="")
print("Uang Bayar: Rp ", uang_bayar,sep="")
print("Kembalian : Rp ", kembalian,sep="")
print("===============================")     
