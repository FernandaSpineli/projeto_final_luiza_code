from shopping_cart.bd import get_collection


STOCK_COLLECTION = get_collection("stocks")


async def get_stock_on_bd(product_code: str):
    return await STOCK_COLLECTION.find_one({"product_code": product_code})

async def update_product_quantity_on_bd(product_code: str, sum: dict):
    stock = await STOCK_COLLECTION.find_one({"product_code": product_code})
    quantity = stock["stock"] + sum["stock"]
    updated = await STOCK_COLLECTION.update_one(
        {"product_code": product_code}, {"$set": {"stock": quantity}})
    if updated.modified_count == 1:
        return True

async def update_stock_on_bd(product_code: str, quantity: dict):
    new_quantity = quantity["stock"]
    updated = await STOCK_COLLECTION.update_one(
        {"product_code": product_code}, {"$set": {"stock": new_quantity}})
    if updated.modified_count == 1:
        return True
