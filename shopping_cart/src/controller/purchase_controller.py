from fastapi import APIRouter

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
    return await create_new_purchase(user_email, purchase)


@TRANSACTION_HISTORY_ROUTE.get("/{purchase_id}")
async def get_purchase_by_id(user_email: str, purchase_id: str):
    return await find_purchase_by_id(user_email, purchase_id)


@TRANSACTION_HISTORY_ROUTE.get("/")
async def get_transaction_history(user_email: str):
    return await find_transaction_history(user_email)
