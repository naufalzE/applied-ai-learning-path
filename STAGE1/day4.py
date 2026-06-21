def ketentuan (data):
    hasil = []
    total = 0
    a = 0
    top = 0
    nama_top = ""
    for i in data:
        a+=1
        total += i["score"]
        if i["score"] > top:
            top =i["score"] 
            nama_top= i["name"]
        if i["score"] >= 75:
            status = "lulus"
        else:
            status = "tidak lulus"
        hasil.append({"name":i["name"],"status":status})
        
        
    print(nama_top,top)
    rata_rata = total/a
    return hasil,rata_rata



students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 70},
    {"name": "Charlie", "score": 92},
    {"name": "David", "score": 60}
]

        
hasil,mean = ketentuan(students)
for i in hasil:
    print(i)
print(mean)
ketentuan(students)
