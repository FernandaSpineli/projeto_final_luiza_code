from shopping_cart.bd import obter_colecao

CARTS_COLLECTION = obter_colecao("carts")
USERS_COLLECTION = obter_colecao("users")
PRODUCTS_COLLECTION = obter_colecao("products")
CART_ITEMS_COLLECTION = obter_colecao("cart_items")
STATUS_OK = "OK"
STATUS_FAIL = "FAIL"


async def get_user_by_email(email: str):
    user = await USERS_COLLECTION.find_one({"email": email})
    return user


async def get_user_by_id(id: str):
    user = await USERS_COLLECTION.find_one({"id": id})
    return user
