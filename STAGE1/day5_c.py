def vokal_detect(data):
    vokal = ["A","E","I","O","U"]
    jumlah_vokal = 0

    huruf_vokal = []
    for i in data:
        if i in vokal:
            jumlah_vokal+=1
            huruf_vokal.append(i)
    return huruf_vokal,jumlah_vokal

def cleaner(data):
    kata_kata = data.strip().title().split()
    displayname = " ".join(kata_kata)
    print_name = displayname.upper()
    return displayname, print_name,kata_kata

while True:
    data_peserta = input("MASUKAN NAMA PESERTA   :")
    display_name,print_name,kata_kata = cleaner(data_peserta)
    if len(display_name) < 5:
        print("data peserta kurang dari 5 input ulang kembali")
        continue
    else:
        print(f"display name    : {display_name}")
        print(f"print name      : {print_name}")
        print(f"kata_kata      : {kata_kata}")
        print(f"panjang kata      : {len(kata_kata)}")
        huruf_vokal,jumlah_vokal = vokal_detect(print_name)
        print(f"huruf vokal : {huruf_vokal}")
        print(f"jumlah  vokal : {jumlah_vokal}")
        break







