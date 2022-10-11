from typing import Optional

from shopping_cart.bd import get_collection


USERS_COLLECTION = get_collection("users")


async def insert_new_user(new_user: dict) -> dict:
        await USERS_COLLECTION.insert_one(new_user)

async def find_user_by_email(user_email: str) -> Optional[dict]:
        user = await USERS_COLLECTION.find_one({"email": user_email})
        return user

async def remove_user_by_email(user_email: str) -> bool:
    try:
        user = await USERS_COLLECTION.delete_one({"email": user_email})
        removed_quantity = user.deleted_count > 0
        return removed_quantity
    except Exception as e:
        print(e)

async def update_user_by_email(user_email: str, features: dict) -> bool:
    try:
        user = await USERS_COLLECTION.update_one({'email': user_email}, {"$set": features})
        return user.modified_count == 1
    except Exception as e:
        print(e)
