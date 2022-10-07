from bd import obter_colecao

CARTS_COLLECTION = obter_colecao("carts")
USERS_COLLECTION = obter_colecao("users")
PRODUCTS_COLLECTION = obter_colecao("products")
CART_ITEMS_COLLECTION = obter_colecao("cart_items")
STATUS_OK = "OK"
STATUS_FAIL = "FAIL"


async def get_product_by_id(id: str):
    product = await PRODUCTS_COLLECTION.find_one({"id": id}, {"_id": 0})
    return product
