from typing import List

from fastapi import APIRouter

from shopping_cart.src.models.entity.product import Product
import shopping_cart.src.business.product_business as product_business


product_route = APIRouter(
    prefix="/magaluJA/products"
    )

 
# Cadastrar produto
@product_route.post("/")
async def create_product(product: Product):
    await product_business.insert_product(product)
    return "Produto cadastrado com sucesso"
    
 # Atualizar dados do produto
@product_route.put("/{product_id}")
async def update_product(product_id: str, features: dict):
    await product_business.update_features_product(product_id, features)    

# Pesquisar produto pelo código
@product_route.get("/{product_id}", response_model= Product)
async def search_product_by_id(product_id: str):
    product = await product_business.get_product_by_id(product_id)
    return product
    
# Pesquisar produto pelo nome
@product_route.get("/{product_name}", response_model = List[Product])
async def search_product_by_name(product_name: str):
    product = await product_business.get_product_by_name(product_name)
    return product 
    
# Remover um produto
@product_route.delete("/{product_id}")
async def delete_product(product_id: str):
    removed_quantity = await product_business.remove_product(product_id)
    return removed_quantity
    