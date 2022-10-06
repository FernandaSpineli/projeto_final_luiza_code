from shopping_cart.bd import obter_colecao

CARTS_COLLECTION = obter_colecao("carts")
USERS_COLLECTION = obter_colecao("users")
PRODUCTS_COLLECTION = obter_colecao("products")
CART_ITEMS_COLLECTION = obter_colecao("cart_items")
STATUS_OK = "OK"
STATUS_FAIL = "FAIL"


async def get_user_by_id(id: str):
    user = await USERS_COLLECTION.find_one({"id": id})
    return user


# from shopping_cart.bd import obter_colecao
# from src.models.user import User

# USERS_COLLECTION = obter_colecao("users")


# async def post_user(user_email, new_user: User):
#     try:
#         get_user_by_email(user_email)
#         USERS_COLLECTION.insert_one(new_user)
#         return new_user
#     except Exception as e:
#         print(e)


# async def get_user_by_email(user_email):
#     try:
#         user = USERS_COLLECTION.find_one(user_email)
#         return user
#     except Exception as e:
#         print(e)


# async def get_user_by_name(user_name):
#     try:
#         user = USERS_COLLECTION.find_one(user_name)
#         return user
#     except Exception as e:
#         print(e)


# async def delete_user_by_email(user_email):
#     try:
#         user = await get_user_by_email(user_email)
#         user = await USERS_COLLECTION.delete_one({"email": user_email})
#     except Exception as e:
#         print(e)


# async def update_user_by_email(user_email):
#     try:
#         user = await get_user_by_email(user_email)
#     except Exception as e:
#         print(e)
