from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int
app = FastAPI()


@app.get("/users/{user_id}")
def get_user(
    user_id: int,
    active: bool,
    limit: int
):
    return {}
@app.get("/products")
def get_products(category:str, limit:int):
    return {
        "category": category,
        "category_type": str(type(category)),
        "limit": limit,
        "limit_type": str(type(limit))
    }
@app.post("/users")
def create_user(user: User):

    print(user.name)
    print(user.email)
    print(user.age)

    return {
        "message": "OK"
    }