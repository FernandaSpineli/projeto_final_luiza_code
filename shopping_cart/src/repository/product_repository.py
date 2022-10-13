from typing import List, Optional

from shopping_cart.bd import get_collection


PRODUCTS_COLLECTION = get_collection("products")
STOCK_COLLECTION = get_collection("stocks")


async def insert_new_product(new_product: dict) -> dict:
        product = await PRODUCTS_COLLECTION.insert_one(new_product)
        stock = {"product_code": new_product["code"], "stock": 0}
        await STOCK_COLLECTION.insert_one(stock)
        if product.inserted_id:
            inserted_product = await find_product_by_id(product.inserted_id)
        return inserted_product
        
async def update_product_by_id(product_id, fields: dict) -> bool:
        result = await PRODUCTS_COLLECTION.update_one({'id': product_id}, {"$set": fields})
        return result.modified_count == 1
        
async def find_product_by_code(code) -> Optional[dict]:
    return await PRODUCTS_COLLECTION.find_one({'code': code}, {'_id': 0})
   
async def find_product_by_id(id) -> Optional[dict]:
    return await PRODUCTS_COLLECTION.find_one({'_id': id})
      
async def find_product_by_name(product_name) -> List[dict]:
    products_found = await PRODUCTS_COLLECTION.count_documents(
        {"name": {"$regex": product_name, '$options': 'i'}}
    )
    search = []
    if products_found:
        async for product in PRODUCTS_COLLECTION.find({"name": {"$regex": product_name, '$options': 'i'}}):
            product.pop("_id")
            search.append(product)
    return search

async def update_product_by_code_db(product_code: str, fields: dict):
    result = await PRODUCTS_COLLECTION.update_one({'code': product_code}, {"$set": fields})
    return result.modified_count == 1

async def remove_product_by_id(product_id: str) -> bool:
    product = await PRODUCTS_COLLECTION.delete_one({'id': product_id})
    await STOCK_COLLECTION.delete_one({"product_id": product_id})
    return product.deleted_count > 0
    
