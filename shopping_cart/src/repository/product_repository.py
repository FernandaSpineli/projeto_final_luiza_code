from typing import List, Optional

from shopping_cart.bd import obter_colecao


PRODUCTS_COLLECTION = obter_colecao("products")


# Insere um produto no banco de dados
async def insert_new_product(new_product: dict) -> dict:
    await PRODUCTS_COLLECTION.insert_one(new_product)
    return new_product

# Atualiza um produto pelo código no banco de dados
async def update_by_id(product_id: str, features: dict) -> bool:
    result = await PRODUCTS_COLLECTION.update_one({'id': product_id}, {"$set": features})
    return result.modified_count == 1

# Procura um produto por id no banco de dados
async def find_product_by_id(id: str) -> Optional[dict]:
    product = await PRODUCTS_COLLECTION.find_one({'id': id })
    return product

# Procura um ou mais produtos por nome no banco de dados
async def find_product_by_name(product_name: str) -> List[dict]:
    cluster = PRODUCTS_COLLECTION.find( {'name': {"$regex": product_name}})    
    found_products = [
        product
        async for product in cluster
    ]
    return found_products

# Remoção de um produto do banco de dados'
async def remove_product_by_id(product_id: str) -> bool:
    result = await PRODUCTS_COLLECTION.delete_one({'id': product_id})
    removed_quantity = result.deleted_count > 0
    return removed_quantity
