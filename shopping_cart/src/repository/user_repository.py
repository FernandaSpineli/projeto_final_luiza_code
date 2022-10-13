from shopping_cart.bd import get_collection
from shopping_cart.src.repository.shopping_cart_repository import SHOPPING_CART_COLLECTION

USERS_COLLECTION = get_collection("users")
SHOPPING_CART_COLLECTION = get_collection("shopping-cart")
TRANSACTION_HISTORY_COLLECTION = get_collection("transaction-history")


async def insert_new_user(new_user: dict):
    user_cart = {"user_email": new_user["email"], "products": [], "price_credit": 0.0,
                 "price_debit": 0.0, "number_of_items": 0, "delivery_address_id": ""}
    await SHOPPING_CART_COLLECTION.insert_one(user_cart)
    transaction_history = {
        "user_email": new_user["email"], "transaction_history": []}
    await TRANSACTION_HISTORY_COLLECTION.insert_one(transaction_history)
    return await USERS_COLLECTION.insert_one(new_user)

async def find_user_by_email(email: str):
    return await USERS_COLLECTION.find_one({"email": email})

async def remove_user_by_email(user_email: str):
    user = await USERS_COLLECTION.delete_one({"email": user_email})
    await SHOPPING_CART_COLLECTION.delete_one({"user_email": user_email})
    await TRANSACTION_HISTORY_COLLECTION.delete_one({"user_email": user_email})
    return user.deleted_count == 1

async def update_user(email: str, features: dict):
    user = await USERS_COLLECTION.update_one({'email': email}, {"$set": features})
    return user.modified_count == 1
