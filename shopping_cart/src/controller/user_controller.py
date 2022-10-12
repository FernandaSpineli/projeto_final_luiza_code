from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from shopping_cart.src.models.entity.user import User
from shopping_cart.src.business.user_business import (
    insert_user,
    find_user_by_email,
    delete_user_by_email
)
USER_ROUTE = APIRouter(prefix="/magaluJA/users")


@USER_ROUTE.post("/")
async def creat_user(user: User):
    new_user = await insert_user(user)
    result = jsonable_encoder(new_user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)

@USER_ROUTE.get("/{email}", response_model= User)
async def get_user(user_email: str):
    user = await find_user_by_email(user_email)
    return JSONResponse(status_code=status.HTTP_200_OK, content=user)

@USER_ROUTE.delete("/{email}")
async def delete_user(user_email: str):
    try:
        removed_quantity = await delete_user_by_email(user_email)
        return removed_quantity
    except Exception as e:
        return "Erro"
    
