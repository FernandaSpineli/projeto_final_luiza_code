from shopping_cart.bd import get_collection


PRODUCTS_COLLECTION = get_collection("products")
STOCK_COLLECTION = get_collection("stocks")


async def insert_new_product(new_product: dict):
    stock = {"product_id": new_product["id"], "stock": 0}
    await STOCK_COLLECTION.insert_one(stock)
    return await PRODUCTS_COLLECTION.insert_one(new_product)


async def find_product_by_id_on_bd(id: str):
    return await PRODUCTS_COLLECTION.find_one({'id': id}, {"_id": 0})


async def find_product_by_name_on_bd(product_name: str):
    products_found = await PRODUCTS_COLLECTION.count_documents(
        {"name": {"$regex": product_name, '$options': 'i'}}
    )
    search = []
    if products_found:
        async for product in PRODUCTS_COLLECTION.find({"name": {"$regex": product_name, '$options': 'i'}}):
            product.pop("_id")
            search.append(product)
    return search


async def remove_product_by_id(product_id: str):
    product = await PRODUCTS_COLLECTION.delete_one({'id': product_id})
    await STOCK_COLLECTION.delete_one({"product_id": product_id})
    return product.deleted_count > 0


async def update_product_by_id_on_bd(product_id: str, fields: dict):
    result = await PRODUCTS_COLLECTION.update_one({'id': product_id}, {"$set": fields})
    return result.modified_count == 1
