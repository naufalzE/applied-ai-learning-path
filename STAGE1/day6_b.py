# scores.txt
#       ↓
# readlines()
#       ↓
# List of String
#       ↓
# split(",")
#       ↓
# Nama + Nilai
#       ↓
# Hitung Statistik
#       ↓
# Buat String Laporan
#       ↓
# write()
#       ↓
# report.txt
def cleaning(datas):
    data = []
    for i in datas:
        raw = i.title().strip().split(",")
        data.append(raw)
    clean_data = dict(data)
    return clean_data

def perhitungan(datas):
    total = 0
    a = 0
    for i in datas.values():
        total += int(i)
        a+=1
    rata_rata = total/a
    return total,rata_rata

def status(datas):
    tertinggi = 0
    terendah = 100
    for i in datas.values():
        nilai = int(i)
        if nilai > tertinggi:
            tertinggi = nilai
        if nilai < terendah:
            terendah = nilai
    return tertinggi,terendah

with open("scores.txt","r") as file:
    data = file.readlines()

raw_raport = cleaning(data)
tertinggi,terendah = status(raw_raport)

total,rata_rata = perhitungan(raw_raport)
raw_raport.update({
    "total_nilai":total,
    "rata_rata":rata_rata,
    "nilai tertinggi": tertinggi,
    "nilai terendah":terendah
})



with open("report.txt","w") as file:
    for k,v in raw_raport.items():
        file.write(f"{k} : {v}\n")


