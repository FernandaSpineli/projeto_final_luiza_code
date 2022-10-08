from shopping_cart.src.models.entity.user import User
from fastapi import FastAPI, APIRouter

from typing import List

user_route = APIRouter(
    prefix="/api/users"
    )

app = FastAPI


@user_route.post("/")
async def creat_user(user: User):
#    await creat_user_validation(user)
    return "usuário criado"

@user_route.get("/{email}")
async def return_user(email):
#    await list_email_validation(email)
    return email

@user_route.get("/{name}")
async def return_name(name):
#    await list_user_validation(name)
    return name

@user_route.delete("/{email}")
async def delete_user(email):
#    await delete_email_validation(email)
    return "usuário excluído"

@user_route.put("/{email}")
async def put_user(email):
#    await update_user_validation(email)
    return "usuário atualizado"
    