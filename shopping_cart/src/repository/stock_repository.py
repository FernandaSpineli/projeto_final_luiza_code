from bd import get_collection


STOCK_COLLECTION = get_collection("STOCKS")


async def update_product_quantity_on_bd(product_id: str, sum: dict):
    stock = await STOCK_COLLECTION.find_one({"product_id": product_id})
    quantity = stock["stock"] + sum["stock"]
    print(quantity)
    await STOCK_COLLECTION.update_one(
        {"product_id": product_id}, {"$set": {"stock": quantity}}
    )


async def update_stock_on_bd(product_id: str, quantity: dict):
    new_quantity = quantity["stock"]
    await STOCK_COLLECTION.update_one(
        {"product_id": product_id}, {"$set": {"stock": new_quantity}}
    )
