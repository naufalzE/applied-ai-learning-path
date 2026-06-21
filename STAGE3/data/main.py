def cleaning(nama):
    raw_name = nama.split()
    jumlah_kata = len(raw_name)
    clean_name = " ".join(raw_name)
    display_name = clean_name.lower().title()
    print_name = clean_name.upper()
    return display_name,print_name,jumlah_kata
def cleaning_text(teks):
    data = [",","!","+"]
    unik_keys = 0
    teks_bersih = teks
    for i in data:
        teks_bersih = teks_bersih.replace(i,"")
        unik_keys+=1
    return unik_keys
cia = "Python, JAVA, C++, Python, AI!!!"   
display_name,print_name,jumlah_kata = cleaning(cia)
unik_keys = cleaning_text(display_name)
print(unik_keys)
print(jumlah_kata)