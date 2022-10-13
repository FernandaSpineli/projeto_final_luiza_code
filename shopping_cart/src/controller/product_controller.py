from fastapi import APIRouter

from shopping_cart.src.models.entity.product import Product
from shopping_cart.src.business.product_business import (
    create_new_product,
    find_product_by_id,
    find_product_by_name,
    update_product_by_id,
    delete_product_by_id,
)

PRODUCT_ROUTE = APIRouter(prefix="/magaluJA/products")


@PRODUCT_ROUTE.post("/")
async def post_product(product: Product):
    return await create_new_product(product)


@PRODUCT_ROUTE.get("/{id}")
async def get_product_by_id(id: str):
    return await find_product_by_id(id)


@PRODUCT_ROUTE.get("/search/{name}")
async def get_product_by_name(name: str):
    return await find_product_by_name(name)


@PRODUCT_ROUTE.delete("/{id}")
async def delete_product(id: str):
    return await delete_product_by_id(id)


@PRODUCT_ROUTE.put("/{id}")
async def update_product(id: str, features: dict):
    return await update_product_by_id(id, features)
