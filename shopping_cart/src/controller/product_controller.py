from fastapi import APIRouter
from typing import List
from shopping_cart.src.models.entity.product import Product
import shopping_cart.src.business.product_business as ps

product_route = APIRouter(
    prefix="/api/product"
    )
 
# Cadastrar produto
@product_route.post("/")
async def create_product(product: Product):
    await ps.insert_product(product)
    return "Produto cadastrado com sucesso"
    
 # Atualizar dados do produto
@product_route.put("/{id}")
async def update_product(id: str, features: dict):
    await ps.update_features_product(id, features)
    

# Pesquisar produto pelo código
@product_route.get("/search_id/{id}", response_model= Product)
async def search_product_by_id(id: str):
    product = await ps.get_product_by_id(id)
    return product
    

# Pesquisar produto pelo nome
@product_route.get("/search_name/{name}", response_model = List[Product])
async def search_product_by_name(name: str):
    product = await ps.get_product_by_name(name)
    return product 
    
    
# Remover um produto
@product_route.delete("/{id}")
async def delete_product(id: str):
    removed_quantity = await ps.remove_product(id)
    return removed_quantity
    
