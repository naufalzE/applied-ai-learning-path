#soal day 1
nama = "ucok"
nilai_ujian = 90
nilai_tugas = 90
nilai_akhir = (nilai_tugas*0.4) + (nilai_ujian*0.6)
print(nilai_akhir)

#soal day2
nilai = int(input("masukkan nilai : "))
status = ""
if nilai >=85:
    status = "A"
elif nilai >=70:
    status = "B"
elif nilai >=60:
    status = "C"
else:
    status = "D"
print(status)

#day3
def hitung_diskon(harga,diskon):
    total_dis =harga*diskon
    return harga - total_dis

harga= 6000
total = hitung_diskon(harga,0.1)
print(total)

#day4
data = {
    "nama":"ucok",
    "umur":30,
    "jurusan":"TI"
}