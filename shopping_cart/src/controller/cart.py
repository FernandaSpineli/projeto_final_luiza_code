from fastapi import APIRouter, status
from repository.cart import (
    add_product_to_cart,
    remove_product_type_from_cart,
    remove_product_from_cart,
    clear_cart,
    find_product_on_cart,
    show_cart_products,
    cart_to_purchase,
    find_purchase_by_id,
    transaction_history,
)

from models.cart import CartProduct

cart_route = APIRouter(prefix="/user/{user_id}/shopping-cart")
transaction_history_route = APIRouter(prefix="/user/{user_id}/transaction-history")


@cart_route.post("/product/", status_code=status.HTTP_201_CREATED)
async def add_product_to_cart_route(user_id: str, cart_product: CartProduct):
    return await add_product_to_cart(user_id, cart_product)


@cart_route.delete("/product/{product_id}/", status_code=status.HTTP_200_OK)
async def remove_product_type_from_cart_route(user_id: str, product_id: str):
    return await remove_product_type_from_cart(user_id, product_id)


@cart_route.delete("/product/", status_code=status.HTTP_200_OK)
async def remove_product_from_cart_route(user_id: str, cart_product: CartProduct):
    return await remove_product_from_cart(user_id, cart_product)


@cart_route.delete("/", status_code=status.HTTP_200_OK)
async def clear_cart_route(user_id: str):
    return await clear_cart(user_id)


@cart_route.get("/product/{product_id}/", status_code=status.HTTP_200_OK)
async def find_product_on_cart_route(user_id: str, product_id: str):
    return await find_product_on_cart(user_id, product_id)


@cart_route.get("/", status_code=status.HTTP_200_OK)
async def show_cart_products_route(user_id: str):
    return await show_cart_products(user_id)


@transaction_history_route.post("/", status_code=status.HTTP_201_CREATED)
async def cart_to_purchase_route(
    user_id: str, payment_method: str, delivery_address_id
):
    return await cart_to_purchase(user_id, payment_method, delivery_address_id)


@transaction_history_route.get("/{purchase_id}", status_code=status.HTTP_200_OK)
async def find_purchase_by_id_route(user_id: str, purchase_id: str):
    return await find_purchase_by_id(user_id, purchase_id)


@transaction_history_route.get("/", status_code=status.HTTP_200_OK)
async def transaction_history_route(user_id: str):
    return await transaction_history(user_id)
