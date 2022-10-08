from src.models.entity.user import User
from fastapi import FastAPI
from typing import List

app = FastAPI


@app.post("/users/")
async def creat_user(user: User):
    await creat_user_validation(user)
    return "usuário criado"


@app.get("/users/{user_email}")
async def return_user(user_email):
    await list_email_validation(user_email)
    return user_email


@app.get("/users/{user_name}")
async def return_name(user_name):
    await list_user_validation(user_name)
    return user_name


@app.delete("/users/{user_email}")
async def delete_user(user_email):
    await delete_email_validation(user_email)
    return "usuário excluído"


@app.put("/users/{user_email}")
async def put_user(user_email):
    await update_user_validation(user_email)
    return "usuário atualizado"
