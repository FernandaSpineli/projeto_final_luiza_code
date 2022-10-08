from fastapi import APIRouter
from src.models.entity.product import Product

product_route = APIRouter(prefix="/api/products")

# Cadastrar produto
@product_route.post("/")
async def create_product(product: Product):
    await ps.insert_product(product)


# Atualizar dados do produto
@product_route.put("/{product_id}")
async def update_product(product_id: str, features: dict):
    await ps.update_features_product(product_id, features)


# Pesquisar produto pelo código
@product_route.get("/{product_id}")
async def search_product_by_id(product_id: str):
    await ps.get_product_by_id(product_id)


# Pesquisar produto pelo nome
@product_route.get("/{product_name}/")
async def search_product_by_name(product_name: str):
    await ps.get_product_by_name(product_name)


# Remover um produto
@product_route.delete("/{product_id}/")
async def delete_product(product_id: str):
    await ps.remove_product(product_id)
