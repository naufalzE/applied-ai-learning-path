def get_total_stock(products):
    total_stock = 0
    for data in products:
        total_stock+= data["stock"]
    return total_stock

def get_most_expensive_product(products):
    expensive = 0
    expensive_name= ""
    for data in products:
        if expensive < data["price"]:
            expensive = data["price"]
            expensive_name = data["name"]
            
    return expensive,expensive_name
            
# def show_product_status(products):
#     for stock in products:
#         if stock["stock"] > 0:
#             print(stock["name"],"available")
#         else:
#             print(stock["name"],"out of stock")

def show_product_status(products):
    status = ""
    ketersediaan = []

    for stock in products:
        if stock["stock"] > 0:
            status = "available"  
        else:
            status = "out of stock"
        ketersediaan.append({"names":stock["name"],"status":status})   
    return ketersediaan


def get_inventory_value(products):
    total = 0
    for data in products:
        total += data["price"] * data["stock"]
    return total


products = [
    {"name": "Laptop", "price": 1000, "stock": 5},
    {"name": "Mouse", "price": 20, "stock": 15},
    {"name": "Keyboard", "price": 50, "stock": 8},
    {"name": "Monitor", "price": 300, "stock": 0}
]

total_stock = get_total_stock(products)
print("total stock: ",total_stock)
mahal,barang = get_most_expensive_product(products)
print("most expensive: ",barang," harga: ",mahal)

data = show_product_status(products)
for i in data:
    name_produk = i["names"]
    status = i["status"]
    print(name_produk,status)
print("total :",get_inventory_value(products))

