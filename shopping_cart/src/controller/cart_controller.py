from fastapi import APIRouter, status
from shopping_cart.src.repository.cart_repository import (
    close_user_cart,
    create_cart,
    add_product_cart,
    get_user_cart,
)

rota_carrinho = APIRouter(
    prefix="/api/carts"
)


@rota_carrinho.post(
    "/{user_id}",
    status_code=status.HTTP_201_CREATED,
)
async def create(user_id: str):
    return await create_cart(user_id)


@rota_carrinho.post(
    "/{user_id}/{product_id}",
    status_code=status.HTTP_201_CREATED,
)
async def add_product(user_id: str, product_id: str):
    return await add_product_cart(user_id, product_id)


@rota_carrinho.get(
    "/{user_id}",
)
async def get_cart(user_id: str):
    return await get_user_cart(user_id)


@rota_carrinho.put(
    "/{user_id}/finish",
    status_code=status.HTTP_202_ACCEPTED
)
async def close_cart(user_id: str):
    return await close_user_cart(user_id)
