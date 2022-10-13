from shopping_cart.bd import get_collection

SHOPPING_CART_COLLECTION = get_collection("shopping-cart")
PRODUCTS_COLLECTION = get_collection("products")
USERS_COLLECTION = get_collection("users")

# adicionar função definir endereço de entrega
# adicionar função de fechar compra


async def add_product_to_cart_on_bd(user_email: str, cart_product: dict):
    shopping_cart = await SHOPPING_CART_COLLECTION.find_one({'user_email': user_email}, {"_id": 0})
    product = await PRODUCTS_COLLECTION.find_one({"code": cart_product["product_id"]}, {"_id": 0})
    quantity = cart_product["quantity"]
    cart_products_list = shopping_cart["products"]
    new_product = False
    for item in cart_products_list:
        if item["product_id"] == cart_product["product_id"]:
            item["quantity"] += cart_product["quantity"]
            new_product = True
    if not new_product:
        cart_products_list.append(cart_product)

    price_credit_total = shopping_cart["price_credit"] + \
        product["price"] * quantity
    price_debit = price_credit_total * 0.9
    total_items = shopping_cart["number_of_items"] + quantity

    cart = await SHOPPING_CART_COLLECTION.update_one(
        {'user_email': user_email},
        {"$set":
         {"products": cart_products_list,
          "price_credit": price_credit_total,
          "price_debit": price_debit,
          "number_of_items": total_items}
         })

    await USERS_COLLECTION.update_one(
        {'email': user_email},
        {"$set":
         {"shopping_cart": {"products": cart_products_list, "price_credit": price_credit_total, "price_debit": price_debit, "number_of_items": total_items}}})

    return await find_cart_on_bd(user_email)


async def find_product_on_cart_on_bd(user_email: str, product_id: str):
    shopping_cart = await SHOPPING_CART_COLLECTION.find_one({'user_email': user_email}, {"_id": 0})
    cart_products_list = shopping_cart["products"]
    for product in cart_products_list:
        if product["product_id"] == product_id:
            return product
    return False


async def find_cart_products_on_bd(user_email: str):
    shopping_cart = await SHOPPING_CART_COLLECTION.find_one({'user_email': user_email}, {"_id": 0})
    return shopping_cart["products"]


async def find_cart_on_bd(user_email: str):
    return await SHOPPING_CART_COLLECTION.find_one({'user_email': user_email}, {"_id": 0})


async def remove_product_from_cart_on_bd(user_email: str, product_id: str):
    shopping_cart = await SHOPPING_CART_COLLECTION.find_one({'user_email': user_email}, {"_id": 0})
    product = await PRODUCTS_COLLECTION.find_one({"code": product_id}, {"_id": 0})
    cart_products_list = shopping_cart["products"]
    for cart_product in cart_products_list:
        if cart_product["product_id"] == product_id:
            quantity = cart_product["quantity"]
            cart_products_list.remove(cart_product)
            price_credit_total = shopping_cart["price_credit"] - \
                (product["price"] * quantity)
            price_debit = price_credit_total * 0.9
            total_items = shopping_cart["number_of_items"] - quantity

            cart = await SHOPPING_CART_COLLECTION.update_one(
                {'user_email': user_email},
                {"$set":
                 {"products": cart_products_list,
                  "price_credit": price_credit_total,
                  "price_debit": price_debit,
                  "number_of_items": total_items}
                 })

            await USERS_COLLECTION.update_one(
                {'email': user_email},
                {"$set":
                 {"shopping_cart":
                  {"products": cart_products_list,
                   "price_credit": price_credit_total,
                   "price_debit": price_debit,
                   "number_of_items": total_items}
                  }})
            return cart.modified_count == 1
    return False


async def clear_cart_on_bd(user_email: str):
    cart = await SHOPPING_CART_COLLECTION.update_one({'user_email': user_email}, {"$set": {"products": [], "price_credit": 0.0, "price_debit": 0.0, "number_of_items": 0}})
    return cart.modified_count == 1


async def update_product_on_cart_on_bd(user_email, cart_product: dict):
    shopping_cart = await SHOPPING_CART_COLLECTION.find_one({'user_email': user_email}, {"_id": 0})
    product = await PRODUCTS_COLLECTION.find_one({"code": cart_product["product_id"]}, {"_id": 0})
    cart_products_list = shopping_cart["products"]
    updated_product = None
    for item in cart_products_list:
        if item["product_id"] == cart_product["product_id"]:
            if cart_product["quantity"] <= 0:
                return await remove_product_from_cart_on_bd(user_email, item["product_id"])

            quantity = cart_product["quantity"] - item["quantity"]

            item["quantity"] += quantity
            price_credit_total = shopping_cart["price_credit"] + \
                (product["price"] * quantity)
            price_debit = price_credit_total * 0.9
            total_items = shopping_cart["number_of_items"] + quantity

            cart = await SHOPPING_CART_COLLECTION.update_one(
                {'user_email': user_email},
                {"$set":
                 {"products": cart_products_list,
                  "price_credit": price_credit_total,
                  "price_debit": price_debit,
                  "number_of_items": total_items}
                 })
            await USERS_COLLECTION.update_one(
                {'email': user_email},
                {"$set":
                 {"shopping_cart":
                  {"products": cart_products_list,
                   "price_credit": price_credit_total,
                   "price_debit": price_debit,
                   "number_of_items": total_items}
                  }})
            if cart.matched_count == 1:
              updated_product = item
    return updated_product