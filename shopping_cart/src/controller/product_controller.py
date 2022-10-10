from typing import List

from fastapi import APIRouter

from shopping_cart.src.models.entity.product import Product
from shopping_cart.src.business.product_business import(
    insert_new_product,
    find_product_by_id,
    find_product_by_name,
    update_product_by_id,
    remove_product_by_id
)


PRODUCT_ROUTE = APIRouter(prefix="/magaluJA/products")

 
# Cadastrar produto
@PRODUCT_ROUTE.post("/")
async def create_product(product: Product):
    await insert_new_product(product)
    return "Produto cadastrado com sucesso"
    
 # Atualizar dados do produto
@PRODUCT_ROUTE.put("/{product_id}")
async def update_product(product_id: str, features: dict):
    await update_product_by_id(product_id, features)    

# Pesquisar produto pelo código
@PRODUCT_ROUTE.get("/{product_id}", response_model= Product)
async def get_product_by_id(product_id: str):
    product = await find_product_by_id(product_id)
    return product
    
# Pesquisar produto pelo nome
@PRODUCT_ROUTE.get("/{product_name}", response_model = List[Product])
async def get_product_by_name(product_name: str):
    product = await find_product_by_name(product_name)
    return product 
    
# Remover um produto
@PRODUCT_ROUTE.delete("/{product_id}")
async def delete_product(product_id: str):
    removed_quantity = await remove_product_by_id(product_id)
    return removed_quantity
    