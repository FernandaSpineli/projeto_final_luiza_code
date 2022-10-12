from shopping_cart.bd import get_collection


STOCKS_COLLECTION = get_collection("stocks")


async def get_stock_on_bd(product_id: str):
    return await STOCKS_COLLECTION.find_one({"product_id": product_id})


async def update_product_quantity_on_bd(product_id: str, sum: dict):
    stock = await get_stock_on_bd(product_id)
    sum["stock"] += stock["stock"]
    await update_stock_on_bd(product_id, sum)


async def update_stock_on_bd(product_id: str, quantity: dict):
    result = await STOCKS_COLLECTION.update_one({"product_id": product_id}, {"$set": quantity})
    return result.modified_count == 1
