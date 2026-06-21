def cleaning(nama):
    raw_name = nama.split()
    jumlah_kata = len(raw_name)
    clean_name = " ".join(raw_name)
    display_name = clean_name.lower().title()
    print_name = clean_name.upper()
    return display_name,print_name,jumlah_kata



def grade(nilai_tugas,nilai_ujian):
    grade = ""
    nilai_akhir = (nilai_tugas *0.4)+(nilai_ujian*0.6)
    if nilai_akhir >= 85:
        grade = "A"
    elif nilai_akhir >= 70:
        grade = "B"
    elif nilai_akhir >= 60:
        grade = "C"
    else:
        grade = "D"
    return grade,nilai_akhir

def hitung_diskon(biaya):
    diskon = biaya*0.1
    return biaya - diskon

def cleaning_text(teks):
    teks_bersih = teks
    for simbol in [",", "!", "+"]:
        teks_bersih = teks_bersih.replace(simbol, "")
    teks_bersih = teks_bersih.lower()
    kata = teks_bersih.split()
    jumlah_kata = len(kata)
    teks_bersih = " ".join(kata)
    return {
        "clean_text": teks_bersih,
        "jumlah_kata": jumlah_kata
    }
nama_peserta = "   muHAMmad      rizKy   "
nilai_tugas = 80
nilai_ujian = 90
biaya_bootcamp = 500000

display_name,print_name,jumlah_kata = cleaning(nama_peserta)
clean_grade,nilai_akhir = grade(nilai_tugas,nilai_ujian)
clean_biaya = hitung_diskon(biaya_bootcamp)

data = {}
data.update({
    "nama": display_name,
    "nama_cetak": print_name,
    "nilai_akhir": nilai_akhir,
    "jumlah kata":jumlah_kata,
    "grade": clean_grade,
    "biaya_setelah_diskon": clean_biaya
}
)

print("=== DATA PESERTA ===")
for i,a in data.items():
    print(f"{i} : {a}")

hasil = cleaning_text(
    "Python, JAVA, C++, Python, AI!!!"
)

print(hasil)

