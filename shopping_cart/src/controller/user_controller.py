from fastapi import APIRouter

from shopping_cart.src.models.entity.user import User
from shopping_cart.src.business.user_business import (
    insert_user,
    get_user_email,
    delete_user_by_email,
    update_user_by_email,
)


USER_ROUTE = APIRouter(prefix="/magaluJA/users")


@USER_ROUTE.post("/")
async def creat_user(user: User):
    new_user = await insert_user(user)
    return new_user

@USER_ROUTE.get("/{email}", response_model=User)
async def get_user_by_email(email: str):
    try:
        user = await get_user_email(email)
        return user
    except Exception as e:
        return "Usuário não encontrado"

@USER_ROUTE.delete("/{email}")
async def delete_user(email):
    await delete_user_by_email(email)
    return "usuário excluído"

@USER_ROUTE.put("/{email}")
async def update_user(email):
    user = await update_user_by_email(email)
    return user
    