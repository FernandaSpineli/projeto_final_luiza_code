from fastapi import APIRouter
from shopping_cart.src.models.product import Product
import shopping_cart.src.service.product_service as ps

product_route = APIRouter(prefix="/api/product")

# Cadastrar produto
@product_route.post("/")
async def create_product(product: Product):
    await ps.insert_product(product)


# Atualizar dados do produto
@product_route.put("/{id}")
async def update_product(id: str, features: dict):
    await ps.update_features_product(id, features)


# Pesquisar produto pelo código
@product_route.get("/search_id/{id}")
async def search_product_by_id(id: str):
    await ps.get_product_by_id(id)


# Pesquisar produto pelo nome
@product_route.get("/search_name/{name}/")
async def search_product_by_name(name: str):
    await ps.get_product_by_name(name)


# Remover um produto
@product_route.delete("/{id}/")
async def delete_product(id: str):
    await ps.remove_product(id)
