from src.models.entity.user import User
from fastapi import FastAPI
from typing import List

user_route = APIRouter(
    prefix="/api/user"
    )

app = FastAPI


@app.post("/users/")
async def creat_user(user: User):
#    await creat_user_validation(user)
    return "usuário criado"

<<<<<<< HEAD
@app.get("/user/{email}")
async def return_user(email):
#    await list_email_validation(email)
    return email

@app.get("/user/{name}")
async def return_name(name):
#    await list_user_validation(name)
    return name

@app.delete("/user/{email}")
async def delete_user(email):
#    await delete_email_validation(email)
    return "usuário excluído"

@app.put("/user/{email}")
async def put_user(email):
    await update_user_validation(email)
#    return "usuário atualizado"
=======

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
>>>>>>> 58a4868d658d8659b760c95fd5ad34bbbfcb769c
