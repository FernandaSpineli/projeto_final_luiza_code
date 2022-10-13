from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from shopping_cart.src.models.entity.user import User
from shopping_cart.src.business.user_business import (
    insert_user,
    get_user_by_email,
    delete_user_by_email,
    update_user_by_email
)
from shopping_cart.src.models.exceptions.exceptions import Bad_Request_Exception
USER_ROUTE = APIRouter(prefix="/magaluJA/users")


@USER_ROUTE.post("/")
async def creat_user(user: User):
    if "@" not in user.email or len(user.email) < 4:
        raise Bad_Request_Exception('E-mail inválido')
    
    new_user = await insert_user(user)
    result = jsonable_encoder(new_user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)

@USER_ROUTE.get("/{user_email}", response_model= User)
async def get_user(user_email: str):
    user = await get_user_by_email(user_email)
    result = jsonable_encoder(user)
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)

@USER_ROUTE.put("/{user_email}", status_code=status.HTTP_204_NO_CONTENT)
async def update_user(user_email: str, fields: dict):
    user = await update_user_by_email(user_email, fields)  

@USER_ROUTE.delete("/{email}")
async def delete_user(user_email: str):
    try:
        removed_quantity = await delete_user_by_email(user_email)
        return removed_quantity
    except Exception as e:
        return "Erro"
    
