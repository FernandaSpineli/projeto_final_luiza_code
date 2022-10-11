from typing import Optional

from shopping_cart.bd import get_collection


USERS_COLLECTION = get_collection("users")


async def insert_new_user(new_user: dict) -> dict:
    user = await USERS_COLLECTION.insert_one(new_user)
    return user


async def find_user_by_id(id: str) -> Optional[dict]:
    user = await USERS_COLLECTION.find_one({"id": id})
    return user


async def find_user_by_email(user_email: str) -> Optional[dict]:
    user = await USERS_COLLECTION.find_one({"email": user_email})
    return user


async def find_user_by_name(user_name: str):
    users_found = await USERS_COLLECTION.count_documents({"name": {"$regex": user_name}})
    search = []
    if users_found:
        async for user in USERS_COLLECTION.find({"name": {"$regex": user_name}}):
            search.append(user)
    return search


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
