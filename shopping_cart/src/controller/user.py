from models.user_models import User
from fastapi import FastAPI
from typing import List

app = FastAPI

@app.post("/user/")
async def creat_user(user: User):
    await creat_user_validation(user)
    return "usuário criado"

@app.get("/user/{email}")
async def return_user(email):
    await list_email_validation(email)
    return email

@app.get("/user/{name}")
async def return_name(name):
    await list_user_validation(name)
    return name

@app.delete("/user/{email}")
async def delete_user(email):
    await delete_email_validation(email)
    return "usuário excluído"

@app.put("/user/{email}")
async def put_user(email):
    await update_user_validation(email)
    return "usuário atualizado"