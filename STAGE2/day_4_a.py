from fastapi import FastAPI
from pydantic import BaseModel
class Product(BaseModel):
    name:str
    price:float
    stock:int

app = FastAPI()

@app.get("/hello")
def get_hellp():
    return {
    "message": "Hello FastAPI"
}
@app.get("/students/{student_id}")
def get_hellp(student_id:int):
    return {
    "student_id": student_id
}
@app.get("/books")
def get_hellp(category: str,limit: int):
    return {
    "category": category,
    "limit": limit
}
@app.get("/search")
def get_hellp(keyword: str,page: int = 1):
    return {
    "keyword": keyword,
    "page": page
}
@app.post("/products")
def get_hellp(product:Product):
    print(product.name)
    print(product.price)
    print(product.stock)
    return {
    "message":"Product berhasil ditambahkan"
}