from uuid import uuid4
from shopping_cart.src.service.cart_service import validate_cart, validate_open_cart, validate_product, validate_user, validate_user_address
from shopping_cart.bd import obter_colecao

CARTS_COLLECTION = obter_colecao("carts")
USERS_COLLECTION = obter_colecao("users")
PRODUCTS_COLLECTION = obter_colecao("products")
CART_ITEMS_COLLECTION = obter_colecao("cart_items")
STATUS_OK = "OK"
STATUS_FAIL = "FAIL"


async def get_user_by_id(id: str):
    user = await USERS_COLLECTION.find_one({'id': id}, {'_id': 0})
    return user


async def get_opened_user_cart(user_id: str):
    cart = await CARTS_COLLECTION.find_one(
        {'user.id': user_id, 'status': 'opened'}, {'_id': 0})
    return cart


async def get_product_by_id(id: str):
    product = await PRODUCTS_COLLECTION.find_one({'id': id}, {'_id': 0})
    return product


async def create_cart(user_id: str):
    try:
        user = await get_user_by_id(user_id)
        validate_user(user)

        user_cart = await get_opened_user_cart(user["id"])
        validate_open_cart(user_cart)

        cart = {
            "user": user,
            "status": "opened",
            "items_quantity": 0,
            "total": 0,
            "id": str(uuid4())
        }

        if user_cart is None:
            cart = await CARTS_COLLECTION.insert_one(cart)
            if cart.inserted_id:
                return STATUS_OK
        else:
            raise TypeError("Carrinho já existe para este cliente")
    except Exception as e:
        return f'create_cart.error: {e}'


async def find_item(cart_id: str, product_id: str):
    item = await CART_ITEMS_COLLECTION.find_one({"cart_id": cart_id, "product.id": product_id}, {'_id': 0})
    return item


async def add_product_cart(user_id, product_id):
    try:
        user = await get_user_by_id(user_id)
        validate_user(user)

        cart = await get_opened_user_cart(user_id)
        if cart is None:
            cart = await create_cart(user_id)
            cart = await get_opened_user_cart(user_id)

        product = await get_product_by_id(product_id)
        validate_product(product)

        item = await find_item(cart["id"], product_id)

        if item is None:
            item = await CART_ITEMS_COLLECTION.insert_one({
                "cart_id": cart["id"],
                "product": product,
                "quantity": 1,
                "total": product["price"],
                "id": str(uuid4())

            })
        else:
            quantity = item["quantity"] + 1
            total = item["total"] + item["product"]["price"]

            item = await CART_ITEMS_COLLECTION.update_one(
                {'id': item["id"]},
                {'$set': {
                    "quantity": quantity,
                    "total": total
                }}
            )

        cart_items_quantity = cart["items_quantity"] + 1
        cart_total = cart["total"] + product["price"]
        cart = await CARTS_COLLECTION.update_one(
            {'id': cart["id"]},
            {'$set': {
                "items_quantity": cart_items_quantity,
                "total": cart_total
            }}
        )

        if cart.modified_count:
            return STATUS_OK
    except Exception as e:
        return f'add_product_cart.error: {e}'


async def close_user_cart(user_id: str):
    try:
        user = await get_user_by_id(user_id)
        validate_user(user)
        validate_user_address(user["addresses"])
        cart = await get_opened_user_cart(user["id"])
        validate_cart(cart)

        cart = await CARTS_COLLECTION.update_one(
            {'id': cart["id"]},
            {'$set': {
                "status": "closed",
            }}
        )

        if cart.modified_count:
            return STATUS_OK
    except Exception as e:
        return f'close_user_cart.error: {e}'


async def find_cart_items(cart_id: str):
    items = CART_ITEMS_COLLECTION.find({"cart_id": cart_id}, {'_id': 0})
    all_items = []

    async for item in items:
        all_items.append(item)
    return all_items


async def get_user_cart(user_id):
    cart = await get_opened_user_cart(user_id)
    cart_items = await find_cart_items(cart["id"])

    return {
        "cart": cart,
        "cart_items": cart_items
    }
