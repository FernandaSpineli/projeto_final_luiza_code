from fastapi import APIRouter
from shopping_cart.src.models.entity.cart_product import CartProduct
from shopping_cart.src.business.shopping_cart_business import (
    add_product_to_cart,
    find_product_on_cart,
    find_cart_products,
    find_cart,
    remove_product_from_cart,
    clear_cart,
    update_product_on_cart
)
# adicionar função definir endereço de entrega

SHOPPING_CART_ROUTE = APIRouter(prefix="/magaluJA/shopping-cart/{user_email}")


@SHOPPING_CART_ROUTE.post("/")
async def post_product_on_cart(user_email: str, cart_product: CartProduct):
    return await add_product_to_cart(user_email, cart_product)


@SHOPPING_CART_ROUTE.get("/products/{product_id}")
async def get_product_on_cart(user_email: str, product_id: str):
    return await find_product_on_cart(user_email, product_id)


@SHOPPING_CART_ROUTE.get("/products")
async def get_cart_products(user_email: str):
    return await find_cart_products(user_email)


@SHOPPING_CART_ROUTE.get("/")
async def get_cart(user_email: str):
    return await find_cart(user_email)


@SHOPPING_CART_ROUTE.delete("/{product_id}")
async def delete_product_from_cart(user_email: str, product_id: str):
    return await remove_product_from_cart(user_email, product_id)


@SHOPPING_CART_ROUTE.delete("/")
async def delete_cart(user_email: str):
    return await clear_cart(user_email)


@SHOPPING_CART_ROUTE.put("/")
async def post_product_on_cart(user_email: str, cart_product: CartProduct):
    return await update_product_on_cart(user_email, cart_product)
