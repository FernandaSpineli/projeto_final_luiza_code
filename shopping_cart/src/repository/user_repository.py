from shopping_cart.bd import get_collection

USERS_COLLECTION = get_collection("users")


async def insert_new_user(new_user: dict):
    await USERS_COLLECTION.insert_one(new_user)


async def find_user_by_email(email: str):
    return await USERS_COLLECTION.find_one({"email": email}, {"_id": 0})


async def remove_user_by_email(user_email: str):
    try:
        user = await USERS_COLLECTION.delete_one({"email": user_email})
        return user.deleted_count == 0
    except Exception as e:
        print(e)
# ------------------------------------------------------------------------------


async def update_user(email: str, features: dict):
    try:
        user = await USERS_COLLECTION.update_one({'email': email}, {"$set": features})
        return user.modified_count == 1
    except Exception as e:
        print(e)
