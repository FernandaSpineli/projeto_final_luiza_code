from typing import List, Optional

from shopping_cart.bd import get_collection


PRODUCTS_COLLECTION = get_collection("products")
STOCK_COLLECTION = get_collection("stocks")


async def insert_new_product(new_product: dict) -> dict:
    try:
        product = await PRODUCTS_COLLECTION.insert_one(new_product)
        stock = {"product_id": new_product["id"], "stock": 0}
        await STOCK_COLLECTION.insert_one(stock)
        return product
    except Exception as e:
        print(e)
        
async def update_product_by_id(product_id: str, fields: dict) -> bool:
    try:
        result = await PRODUCTS_COLLECTION.update_one({'id': product_id}, {"$set": fields})
        return result.modified_count == 1
    except Exception as e:
        print(e)
        
async def find_product_by_id(id: str) -> Optional[dict]:
    try:
        product = await PRODUCTS_COLLECTION.find_one({'id': id })
        return product
    except Exception as e:
        print(e)
        
async def find_product_by_name(product_name: str) -> List[dict]:
    try:
        products_found = await PRODUCTS_COLLECTION.count_documents(
        {"name": {"$regex": product_name}}
        )
        search = []
        if products_found:
            async for product in PRODUCTS_COLLECTION.find({"name": {"$regex": product_name}}):
                search.append(product)
        return search
    except Exception as e:
        print(e)
        
async def remove_product_by_id(product_id: str) -> bool:
    try:
        product = await PRODUCTS_COLLECTION.delete_one({'id': product_id})
        await STOCK_COLLECTION.delete_one({"product_id": product_id})
        removed_quantity = product.deleted_count > 0
        return removed_quantity
    except Exception as e:
        print(e)