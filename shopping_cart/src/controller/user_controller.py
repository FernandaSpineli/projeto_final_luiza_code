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
async def create_user(user: User):
    return await insert_user(user)


@USER_ROUTE.get("/{email}")
async def get_user_by_email(email: str):
    return await get_user_email(email)


@USER_ROUTE.delete("/{email}")
async def delete_user(email):
    return await delete_user_by_email(email)

# ------------------------------------------------------------------------------


@USER_ROUTE.put("/{email}")
async def update_user(email: str, features: dict):
    return await update_user_by_email(email, features)
