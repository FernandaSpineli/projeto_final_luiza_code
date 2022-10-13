from shopping_cart.bd import get_collection

USERS_COLLECTION = get_collection("users")
TRANSACTION_HISTORY_COLLECTION = get_collection("transaction-history")


async def create_new_purchase_on_bd(user_email: str, purchase: dict):
    transaction_history = await TRANSACTION_HISTORY_COLLECTION.find_one({'user_email': user_email}, {"_id": 0})
    purchase_list = transaction_history["transaction_history"]
    purchase_list.append(purchase)
    check = await TRANSACTION_HISTORY_COLLECTION.update_one({'user_email': user_email}, {"$set": {"transaction_history": purchase_list}})

    await USERS_COLLECTION.update_one({'email': user_email}, {"$set": {"transaction_history": purchase_list}})

    if check.modified_count == 1:
        return True


async def find_purchase_by_id_on_bd(user_email: str, purchase_id: str):
    transaction_history = await TRANSACTION_HISTORY_COLLECTION.find_one({'user_email': user_email}, {"_id": 0})
    purchase_list = transaction_history["transaction_history"]
    for purchase in purchase_list:
        if purchase["id"] == purchase_id:
            return purchase
    return False


async def find_transaction_history_on_bd(user_email: str):
    return await TRANSACTION_HISTORY_COLLECTION.find_one({'user_email': user_email}, {"_id": 0})
