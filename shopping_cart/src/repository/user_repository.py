from shopping_cart.bd import get_collection
from shopping_cart.src.repository.shopping_cart_repository import SHOPPING_CART_COLLECTION

USERS_COLLECTION = get_collection("users")
SHOPPING_CART_COLLECTION = get_collection("shopping-cart")


async def insert_new_user(new_user: dict):
    user_cart = new_user["shopping_cart"]
    await SHOPPING_CART_COLLECTION.insert_one(user_cart)
    await USERS_COLLECTION.insert_one(new_user)


async def find_user_by_email(email: str):
    return await USERS_COLLECTION.find_one({"email": email}, {"_id": 0})


async def remove_user_by_email(user_email: str):
    user = await USERS_COLLECTION.delete_one({"email": user_email})
    await SHOPPING_CART_COLLECTION.delete_one({"user_email": user_email})
    return user.deleted_count == 0


async def update_user(email: str, features: dict):
    user = await USERS_COLLECTION.update_one({'email': email}, {"$set": features})
    return user.modified_count == 1
