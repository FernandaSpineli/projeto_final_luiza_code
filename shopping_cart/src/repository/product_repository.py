from typing import List, Optional
from shopping_cart.bd import obter_colecao

products_collection = obter_colecao("products")

# Insere um produto no banco de dados
async def insert_new_product(new_product: dict) -> dict:
    await products_collection.insert_one(new_product)
    return new_product

# Atualiza um produto pelo código no banco de dados
async def update_by_id(product_id: str, features: dict) -> bool:
    result = await products_collection.update_one({'id': product_id}, {"$set": features})
    return result.modified_count == 1

# Procura um produto por id no banco de dados
async def search_by_id(product_id: str) -> Optional[dict]:
    product = await products_collection.find_one({'id': product_id })
    return product

# Procura um ou mais produtos por nome no banco de dados
async def search_by_name(product_name: str) -> List[dict]:
    cluster = products_collection.find( {'name': {"$regex": product_name}})

    
    found_products = [
        product
        async for product in cluster
    ]
    return found_products

# Remoção de um produto do banco de dados
async def remove_by_id(product_id: str) -> bool:
    result = await products_collection.delete_one({'id': product_id})
    removed_quantity = result.deleted_count > 0
    return removed_quantity
