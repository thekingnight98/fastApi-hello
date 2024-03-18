from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class User(BaseModel):
    username : str
    password : str
    level:Union[str] = "normal"



@app.get("/")
def read_root():
    return {"Hello": "World"}

# http://127.0.0.1:8000/hi?name=Arm&reply=1234
@app.get("/hi")
def hi(name:str , reply: Union[str, None] = None):
    return {"Hi": name , "reply" : reply}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# method post ใช้ผ่าน docs เท่านั้น ปกติต้อง test on postman
# http://127.0.0.1:3000/docs#/
@app.post("/login}")
def login(user: User):
    return {"echo": user}