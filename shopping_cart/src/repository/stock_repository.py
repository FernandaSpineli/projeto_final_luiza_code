from bd import get_collection


STOCK_COLLECTION = get_collection("STOCKS")


async def update_product_amount_on_bd(product_id: str, sum: dict):
    stock = await STOCK_COLLECTION.find_one({"product_id": product_id})
    amount = stock["stock"] + sum["stock"]
    print(amount)
    await STOCK_COLLECTION.update_one(
        {"product_id": product_id}, {"$set": {"stock": amount}}
    )


async def update_stock_on_bd(product_id: str, amount: dict):
    new_amount = amount["stock"]
    await STOCK_COLLECTION.update_one(
        {"product_id": product_id}, {"$set": {"stock": new_amount}}
    )
