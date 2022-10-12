from fastapi import APIRouter

from shopping_cart.src.business.stock_business import update_product_quantity, update_stock

STOCK_ROUTE = APIRouter(prefix="/magaluJA/stocks")


@STOCK_ROUTE.put("/{product_id}")
async def update_products(product_id: str, sum: dict):
    return await update_product_quantity(product_id, sum)


@STOCK_ROUTE.put("/redefine/{product_id}")
async def update_stocks(product_id: str, sum: dict):
    return await update_stock(product_id, sum)
