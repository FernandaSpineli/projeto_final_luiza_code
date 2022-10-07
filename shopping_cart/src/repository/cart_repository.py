
from src.models.cart import CartProduct, ShoppingCart

from src.repository.user_repository import get_user_by_id
from src.repository.product_repository import get_product_by_id

from src.service.user_service import validate_user
from src.service.product_service import validate_product

# - talvez precise mexer nesta parte do código, até a linha 16
from bd import obter_colecao

CARTS_COLLECTION = obter_colecao("carts")
USERS_COLLECTION = obter_colecao("users")
PRODUCTS_COLLECTION = obter_colecao("products")
STATUS_OK = "OK"
STATUS_FAIL = "FAIL"
# -


async def add_product_to_cart(user_id: str, cart_product: CartProduct):
    try:
        user = await get_user_by_id(user_id)
        validate_user(user)

        product = await get_product_by_id(cart_product.product_id)
        validate_product(product)

        user_cart = await CARTS_COLLECTION.find_one({"user_id": user_id}, {"_id": 0})
        product_list = user_cart["products"]

        new_product = True

        for item in product_list:
            if item["product_id"] == cart_product.product_id:
                item["amount"] += cart_product.amount
                new_product = False

        if new_product:
            product_list.append(cart_product)

        price_credit = user_cart["price_credit"] + product.price * cart_product.amount
        price_debit = price_credit * 0.9
        number_of_items = user_cart["number_of_items"] + cart_product.amount

        cart = await CARTS_COLLECTION.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "products": product_list,
                    "price_credit": price_credit,
                    "price_debit": price_debit,
                    "number_of_items": number_of_items,
                }
            },
        )

        if cart.modified_count:
            return STATUS_OK

    except Exception as e:
        return f"add_product_cart.error: {e}"


async def remove_product_type_from_cart(user_id: str, product_id: str):
    try:
        user = await get_user_by_id(user_id)
        validate_user(user)

        product = await get_product_by_id(product_id)
        validate_product(product)

        user_cart = await CARTS_COLLECTION.find_one({"user_id": user_id}, {"_id": 0})
        product_list = user_cart["products"]

        for item in product_list:
            if item["product_id"] == product_id:
                # se produto constar no carrinho
                product_list.remove(item)
                price_credit = (
                    user_cart["price_credit"] - product.price * item["amount"]
                )
                price_debit = price_credit * 0.9
                number_of_items = user_cart["number_of_items"] - item["amount"]

        cart = await CARTS_COLLECTION.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "products": product_list,
                    "price_credit": price_credit,
                    "price_debit": price_debit,
                    "number_of_items": number_of_items,
                }
            },
        )

        if cart.modified_count:
            return STATUS_OK

    except Exception as e:
        return f"remove_product_type_from_cart.error: {e}"


async def remove_product_from_cart(user_id: str, cart_product: CartProduct):
    try:
        user = await get_user_by_id(user_id)
        validate_user(user)

        product = await get_product_by_id(cart_product.product_id)
        validate_product(product)

        user_cart = await CARTS_COLLECTION.find_one({"user_id": user_id}, {"_id": 0})
        product_list = user_cart["products"]

        for item in product_list:
            if item["product_id"] == cart_product.product_id:
                if item["amount"] <= cart_product.amount:
                    return remove_product_type_from_cart(
                        user_id, cart_product.product_id
                    )

                item["amount"] -= cart_product.amount
                price_credit = (
                    user_cart["price_credit"] - product.price * cart_product.amount
                )
                price_debit = price_credit * 0.9
                number_of_items = user_cart["number_of_items"] - cart_product.amount

        cart = await CARTS_COLLECTION.update_one(
            {"user_id": user_id},
            {
                "$set": {
                    "products": product_list,
                    "price_credit": price_credit,
                    "price_debit": price_debit,
                    "number_of_items": number_of_items,
                }
            },
        )

        if cart.modified_count:
            return STATUS_OK

    except Exception as e:
        return f"remove_product_from_cart.error: {e}"


async def clear_cart(user_id: str):
    try:
        user = await get_user_by_id(user_id)
        validate_user(user)

        cart = await USERS_COLLECTION.update_one(
            {"id": user_id},
            {"$set": {"shopping_cart": ShoppingCart()}},
        )

        if cart.modified_count:
            return STATUS_OK

    except Exception as e:
        return f"clear_cart: {e}"


async def find_product_on_cart(user_id: str, product_id: str):
    try:
        user = await get_user_by_id(user_id)
        validate_user(user)

        product = await get_product_by_id(product_id)
        validate_product(product)

        user_cart = await CARTS_COLLECTION.find_one({"user_id": user_id}, {"_id": 0})
        product_list = user_cart["products"]

        for item in product_list:
            if item["product_id"] == product_id:
                return item

    except Exception as e:
        return f"find_product_on_cart.error: {e}"


async def show_cart_products(user_id: str):
    try:
        user = await get_user_by_id(user_id)
        validate_user(user)

        user_cart = await CARTS_COLLECTION.find_one({"user_id": user_id}, {"_id": 0})
        product_list = user_cart["products"]

        return product_list

    except Exception as e:
        return f"show_cart_products.error: {e}"


# ESTA FUNÇÃO ESTA CAGADA
async def cart_to_purchase(user_id: str, payment_method: str, delivery_address_id: str):
    # try:
    #     user = await get_user_by_id(user_id)
    #     validate_user(user)

    #     user = await USERS_COLLECTION.find_one({"user_id": user_id}, {"_id": 0})

    #     user_addresses = user["addresses"] #lista de Address
    #     user_shopping_cart = user["shopping_cart"] #ShoppingCart
    #     user_transaction_history = user["transaction_history"] #lista de Purchase

    #     for address in user_addresses:
    #         if address["id"] == delivery_address_id:
    #             delivery_address = address #####################################################

    # #     for item in product_list:
    # #         if item["product_id"] == cart_product.product_id:
    # #             item["amount"] += cart_product.amount
    # #             new_product = False

    # #     if new_product:
    # #         product_list.append(cart_product)

    # #     price_credit = user_cart["price_credit"] + product.price * cart_product.amount
    # #     price_debit = price_credit * 0.9
    # #     number_of_items = user_cart["number_of_items"] + cart_product.amount

    # #     cart = await CARTS_COLLECTION.update_one(
    # #         {"user_id": user_id},
    # #         {
    # #             "$set": {
    # #                 "products": product_list,
    # #                 "price_credit": price_credit,
    # #                 "price_debit": price_debit,
    # #                 "number_of_items": number_of_items,
    # #             }
    # #         },
    # #     )

    # #     if cart.modified_count:
    # #         return STATUS_OK

    # # except Exception as e:
    # #     return f"add_product_cart.error: {e}"
    # #     # aqui vamos criar uma instancia de purchase com as informações passadas
    # # # e adicionar a lista transaction_history do usuário
    # # # e chamar a função clear_cart() para zerar o carrinho
    return "OK"


async def find_purchase_by_id(user_id: str, purchase_id: str):
    try:
        user = await get_user_by_id(user_id)
        validate_user(user)

        user = await USERS_COLLECTION.find_one({"user_id": user_id}, {"_id": 0})
        user_transaction_history = user["transaction_history"]

        for purchase in user_transaction_history:
            if purchase["id"] == purchase_id:
                return purchase

    except Exception as e:
        return f"find_purchase_by_id.error: {e}"


async def transaction_history(user_id: str):
    try:
        user = await get_user_by_id(user_id)
        validate_user(user)

        user = await USERS_COLLECTION.find_one({"user_id": user_id}, {"_id": 0})
        user_transaction_history = user["transaction_history"]

        return user_transaction_history

    except Exception as e:
        return f"transaction_history.error: {e}"
