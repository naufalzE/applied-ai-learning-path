# buat fungsi  kelulusan (nilai)
def kelulusan(nilai1, nilai2, nilai3,nama):
    """menghitung rata-rata nilai dan menentukan status kelulusan serta mengembalikan nama"""
    total_nilai = nilai1 + nilai2 + nilai3
    mean_nilai = total_nilai / 3
    if mean_nilai >= 75:
        status = "lulus"
    else:
        status = "tidak lulus"
    return status,nama,mean_nilai

status,nama,mean_nilai = kelulusan(80, 70, 90, "Budi")

print("Nama:", nama)
print("Nilai rata-rata:", mean_nilai)
print("Status kelulusan:", status)
