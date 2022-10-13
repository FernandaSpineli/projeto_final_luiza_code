from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from shopping_cart.src.business.stock_business import update_product_quantity, update_stock


STOCK_ROUTE = APIRouter(prefix="/magaluJA/stocks")


@STOCK_ROUTE.put("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_products(product_id: str, sum: dict):
    stock =  await update_product_quantity(product_id, sum)

@STOCK_ROUTE.put("/redefine/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_stocks(product_id: str, sum: dict):
    stock = await update_stock(product_id, sum)
   