def cleaning(datas):
    clean_raw = []
    for i in datas:
        clean_raw.append(i.strip().title())
    teks_final = "\n".join(clean_raw)
    return teks_final


with open("raw_names.txt", "r") as file:
    data = file.readlines()

teks_final = cleaning(data)
    
with open("clean_names.txt","w") as file:
    file.write(teks_final)