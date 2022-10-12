from shopping_cart.bd import get_collection


STOCK_COLLECTION = get_collection("stocks")


async def get_stock_on_bd(product_id: str):
    return await STOCK_COLLECTION.find_one({"product_id": product_id})


async def update_product_quantity_on_bd(product_id: str, sum: dict):
    stock = await STOCK_COLLECTION.find_one({"product_id": product_id})
    quantity = stock["stock"] + sum["stock"]
    await STOCK_COLLECTION.update_one(
        {"product_id": product_id}, {"$set": {"stock": quantity}}
    )


async def update_stock_on_bd(product_id: str, quantity: dict):
    new_quantity = quantity["stock"]
    await STOCK_COLLECTION.update_one(
        {"product_id": product_id}, {"$set": {"stock": new_quantity}}
    )
