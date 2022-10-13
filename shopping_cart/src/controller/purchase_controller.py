from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from shopping_cart.src.models.entity.purchase import Purchase
from shopping_cart.src.business.purchase_business import (
    create_new_purchase,
    find_purchase_by_id,
    find_transaction_history
)


TRANSACTION_HISTORY_ROUTE = APIRouter(
    prefix="/magaluJA/transaction-history/{user_email}")


@TRANSACTION_HISTORY_ROUTE.post("/")
async def post_purchase(user_email: str, purchase: Purchase):
    new_purchase = await create_new_purchase(user_email, purchase)
    result = jsonable_encoder(new_purchase)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)

@TRANSACTION_HISTORY_ROUTE.get("/")
async def get_transaction_history(user_email: str):
    user_history = await find_transaction_history(user_email)
    result = jsonable_encoder(user_history)
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)

@TRANSACTION_HISTORY_ROUTE.get("/{purchase_id}")
async def get_purchase_by_id(user_email: str, purchase_id: str):
    purchase = await find_purchase_by_id(user_email, purchase_id)
    result = jsonable_encoder(purchase)
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)
