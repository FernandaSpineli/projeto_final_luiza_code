from shopping_cart.bd import obter_colecao
from shopping_cart.src.controller.user_controller import User


USERS_COLLECTION = obter_colecao("users")


async def find_user_by_id(user_id: str):
    try:
        user = await USERS_COLLECTION.find_one({"id": user_id})
        return user
    except Exception as e:
        print(e)

async def set_new_user(user_email, new_user: User):
    try:
        USERS_COLLECTION.insert_one(new_user)
        return new_user
    except Exception as e:
        print(e)

async def find_user_by_email(user_email):
    try:
        user = USERS_COLLECTION.find_one(user_email)
        return user
    except Exception as e:
        print(e)

async def find_user_by_name(user_name):
    try:
        user = USERS_COLLECTION.find_one(user_name)
        return user
    except Exception as e:
        print(e)

async def remove_user_by_email(user_email):
    try:
        user = await USERS_COLLECTION.delete_one({"email": user_email})
        return user
    except Exception as e:
        print(e)

async def set_user_by_email(user_email):
    try:
        ...
    except Exception as e:
        print(e)
