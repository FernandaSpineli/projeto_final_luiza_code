from fastapi import APIRouter, status
from src.repository.cart_repository import (
    add_product_to_cart,
    remove_product_type_from_cart,
    remove_product_from_cart,
    clear_cart,
    get_product_on_cart,
    get_cart_products,
    cart_to_purchase,
    get_purchase_by_id,
    transaction_history,
)

from src.models.cart import CartProduct

cart_route = APIRouter(prefix="/api/users/{user_id}/shopping-cart")
purchases_route = APIRouter(prefix="/api/users/{user_id}/transaction-history")

#adicionar produto no carrinho
@cart_route.post("/products/", status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(user_id: str, cart_product: CartProduct):
    return await add_product_to_cart(user_id, cart_product)

# buscar produto no carrinho
@cart_route.get("/products/{product_id}/", status_code=status.HTTP_200_OK)
async def get_product_on_cart(user_id: str, product_id: str):
    return await get_product_on_cart(user_id, product_id)

#mostrar 
@cart_route.get("/", status_code=status.HTTP_200_OK)
async def get_cart_products(user_id: str):
    return await get_cart_products(user_id)

#remover???
@cart_route.delete("/products/{product_id}/", status_code=status.HTTP_200_OK)
async def remove_product_type_from_cart(user_id: str, product_id: str):
    return await remove_product_type_from_cart(user_id, product_id)

# remover produto do carrinho
@cart_route.delete("/products/", status_code=status.HTTP_200_OK)
async def remove_product_from_cart_route(user_id: str, cart_product: CartProduct):
    return await remove_product_from_cart(user_id, cart_product)

# limpar carrinho
@cart_route.delete("/", status_code=status.HTTP_200_OK)
async def clear_cart(user_id: str):
    return await clear_cart(user_id)

@purchases_route.post("/", status_code=status.HTTP_201_CREATED)
async def cart_to_purchase(
    user_id: str, payment_method: str, delivery_address_id
):
    return await cart_to_purchase(user_id, payment_method, delivery_address_id)

@purchases_route.get("/{purchase_id}", status_code=status.HTTP_200_OK)
async def find_purchase_by_id(user_id: str, purchase_id: str):
    return await find_purchase_by_id(user_id, purchase_id)


@purchases_route.get("/", status_code=status.HTTP_200_OK)
async def transaction_history(user_id: str):
    return await transaction_history(user_id)
