from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
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
# adicionar função de fechar compra

SHOPPING_CART_ROUTE = APIRouter(prefix="/magaluJA/shopping-cart/{user_email}")


@SHOPPING_CART_ROUTE.post("/")
async def post_product_on_cart(user_email: str, cart_product: CartProduct):
    cart = await add_product_to_cart(user_email, cart_product)
    result = jsonable_encoder(cart)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)


@SHOPPING_CART_ROUTE.get("/products/{product_id}")
async def get_product_on_cart(user_email: str, product_id: str):
    product = await find_product_on_cart(user_email, product_id)
    result = jsonable_encoder(product)
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)


@SHOPPING_CART_ROUTE.get("/products")
async def get_cart_products(user_email: str):
    products = await find_cart_products(user_email)
    return JSONResponse(status_code=status.HTTP_200_OK, content=products)


@SHOPPING_CART_ROUTE.get("/")
async def get_cart(user_email: str):
    cart = await find_cart(user_email)
    result = jsonable_encoder(cart)
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)


@SHOPPING_CART_ROUTE.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product_from_cart(user_email: str, product_id: str):
    return await remove_product_from_cart(user_email, product_id)


@SHOPPING_CART_ROUTE.delete("/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_cart(user_email: str):
    return await clear_cart(user_email)


@SHOPPING_CART_ROUTE.put("/", status_code=status.HTTP_204_NO_CONTENT)
async def post_product_on_cart(user_email: str, cart_product: CartProduct):
    return await update_product_on_cart(user_email, cart_product)