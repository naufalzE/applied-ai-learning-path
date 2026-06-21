# Input per siswa:

# Nama siswa
# Nilai tugas (bobot 40%)
# Nilai ujian (bobot 60%)

# Proses:

# Hitung nilai akhir dari kedua bobot
# Tentukan grade berdasarkan nilai akhir:

# >= 85  → Grade A  
# >= 75  → Grade B  
# >= 60  → Grade C  
# >= 50  → Grade D  
# < 50   → Grade E
# Output per siswa:
# Nama  : Budi
# Nilai Akhir : 78.0
# Grade : B
# Output ringkasan di akhir:
# Total siswa Grade A: 1
# Total siswa Grade B: 2
# Total siswa Grade C: 1
# Total siswa Grade D: 1
# Total siswa Grade E: 0

siswa = 5
siswa_grade_a = 0
siswa_grade_b = 0
siswa_grade_c = 0
siswa_grade_d = 0
siswa_grade_e = 0
for i in range(siswa):
    nama = input("masukkan nama siswa: ")
    nilai_tugas = float(input("masukkan nilai tugas: "))
    nilai_ujian = float(input("masukkan nilai ujian:"))
    nilai_akhir = ((nilai_tugas * 0.4) + (nilai_ujian*0.6))
    if nilai_tugas < 0 or nilai_tugas > 100 or nilai_ujian < 0 or nilai_ujian > 100:
        print("Nilai tugas dan ujian harus antara 0 dan 100. Silakan masukkan nilai yang valid.")
        continue  # Skip to the next iteration if values are invalid
    if nilai_akhir >=85:
        grade = "A"
        siswa_grade_a += 1
    elif nilai_akhir >= 75:
        grade = "B"
        siswa_grade_b += 1
    elif nilai_akhir >= 60:
        grade = "C"
        siswa_grade_c += 1
    elif nilai_akhir >= 50:
        grade = "D"
        siswa_grade_d += 1
    else:
        grade = "E"
        siswa_grade_e += 1
    print("Nama: ", nama)
    print("Nilai Akhir: ", nilai_akhir)
    print("Grade: ", grade)
  

print("Output ringkasan di akhir:")
print("Total siswa Grade A:", siswa_grade_a)
print("Total siswa Grade B:", siswa_grade_b)
print("Total siswa Grade C:", siswa_grade_c)
print("Total siswa Grade D:", siswa_grade_d)
print("Total siswa Grade E:", siswa_grade_e)


usia = int(input("masukkan usia: "))
film = input("masukkan film: ")

if usia >= 18:
	if film == "dewasa":
		print("status : boleh masuk ")
		print("harga tiket: 75.000")
	elif film == "reguler":
		print("status : boleh masuk ")
		print("harga tiket: 50.000")
else:
	if film == "dewasa":
		print("status : tidak boleh masuk ")

	elif film == "reguler":
		print("status : boleh masuk ")
		print("harga tiket: 35.000")