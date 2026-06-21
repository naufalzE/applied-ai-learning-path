


class mahasiswa:
    def __init__(self,name,nim,nilai_tugas,nilai_ujian):
        self.name = name
        self.nim = nim
        self.__nilai_tugas = nilai_tugas
        self.__nilai_ujian = nilai_ujian
    def get_nilai_tugas(self):
        return self.__nilai_tugas
    def get_nilai_ujian(self):
        return self.__nilai_ujian

# 1. Ini method pembantu di dalam class (Helper Method)
    def validasi_nilai(self, nilai):
        return 0 <= nilai <= 100

    # 2. Setter memanfaatkan helper method di atas untuk mengubah nilai
    def set_nilai_tugas(self, nilai_baru):
        if self.validasi_nilai(nilai_baru): # Jika True
            self.__nilai_tugas = nilai_baru
        else:
            print("⚠️ Nilai tugas tidak valid!")

    def set_nilai_ujian(self, nilai_baru):
        if self.validasi_nilai(nilai_baru): # Jika True
            self.__nilai_ujian = nilai_baru
        else:
            print("⚠️ Nilai ujian tidak valid!")
    def hitung_nilai_akhir(self):
        return (self.get_nilai_tugas()*0.4) + (self.get_nilai_ujian()*0.6)
    def grade(self):
        nilai_akhir = self.hitung_nilai_akhir()
        if nilai_akhir >= 85:
            return "A"
        elif nilai_akhir >=70:
            return "B"
        elif nilai_akhir >= 60:
            return "C"
        else:
            return "D" 
    def tampilkan_info(self):
        print(f"Name         : {self.name}")
        print(f"NIM          : {self.nim}")
        print(f"Nilai Akhir  : {self.hitung_nilai_akhir()}")
        print(f"Grade        : {self.grade()}")
data_mentah = [
    ["Ucok", 111, 80, 90],
    ["Baba", 112, 75, 85],
    ["Cia", 113, 90, 95]
]
daftar_mhs = []
for i in data_mentah:
    objek_baru = mahasiswa(name=i[0],nim=i[1],nilai_tugas=i[2],nilai_ujian=i[3])
    daftar_mhs.append(objek_baru)
    
for mhs in daftar_mhs:
    mhs.tampilkan_info()
    print(mhs.get_nilai_tugas())
    print("=========================")



students = []
students = []
while True:
    nama = input("nama  :")
    nim = int(input("NIM    :"))
    
    input_tugas = int(input("nilai_tugas    : "))
    input_ujian = int(input("nilai_ujian    : "))

    # Buat objek awal dengan nilai default 0
    u = mahasiswa(name=nama, nim=nim, nilai_tugas=0, nilai_ujian=0)

    # PERBAIKAN: Memanggil nama setter secara utuh dan benar
    u.set_nilai_tugas(input_tugas)
    u.set_nilai_ujian(input_ujian)

    students.append(u)

    lanjut = input("y/n : ").lower()
    if lanjut == "n":
        break

print("\n=========================")
for i in students:
    i.tampilkan_info()
    print("=========================")