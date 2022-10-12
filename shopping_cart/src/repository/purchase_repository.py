# # ESTA FUNÇÃO ESTA CAGADA
# async def cart_to_purchase(user_id: str, payment_method: str, delivery_address_id: str):
#     # try:
#     #     user = await get_user_by_id(user_id)
#     #     validate_user(user)

#     #     user = await USERS_COLLECTION.find_one({"user_id": user_id}, {"_id": 0})

#     #     user_addresses = user["addresses"] #lista de Address
#     #     user_shopping_cart = user["shopping_cart"] #ShoppingCart
#     #     user_transaction_history = user["transaction_history"] #lista de Purchase

#     #     for address in user_addresses:
#     #         if address["id"] == delivery_address_id:
#     #             delivery_address = address #####################################################

#     # #     for item in product_list:
#     # #         if item["product_id"] == cart_product.product_id:
#     # #             item["quantity"] += cart_product.quantity
#     # #             new_product = False

#     # #     if new_product:
#     # #         product_list.append(cart_product)

#     # #     price_credit = user_cart["price_credit"] + product.price * cart_product.quantity
#     # #     price_debit = price_credit * 0.9
#     # #     number_of_items = user_cart["number_of_items"] + cart_product.quantity

#     # #     cart = await CARTS_COLLECTION.update_one(
#     # #         {"user_id": user_id},
#     # #         {
#     # #             "$set": {
#     # #                 "products": product_list,
#     # #                 "price_credit": price_credit,
#     # #                 "price_debit": price_debit,
#     # #                 "number_of_items": number_of_items,
#     # #             }
#     # #         },
#     # #     )

#     # #     if cart.modified_count:
#     # #         return STATUS_OK

#     # # except Exception as e:
#     # #     return f"add_product_cart.error: {e}"
#     # #     # aqui vamos criar uma instancia de purchase com as informações passadas
#     # # # e adicionar a lista transaction_history do usuário
#     # # # e chamar a função clear_cart() para zerar o carrinho
#     return "OK"


# async def get_purchase_by_id(user_id: str, purchase_id: str):
#     try:
#         user = await find_user_by_id(user_id)
#         # validate_user(user)

#         user = await USERS_COLLECTION.find_one({"user_id": user_id}, {"_id": 0})
#         user_transaction_history = user["transaction_history"]

#         for purchase in user_transaction_history:
#             if purchase["id"] == purchase_id:
#                 return purchase

#     except Exception as e:
#         return f"find_purchase_by_id.error: {e}"


# async def transaction_history(user_id: str):
#     try:
#         user = await find_user_by_id(user_id)
#         # validate_user(user)

#         user = await USERS_COLLECTION.find_one({"user_id": user_id}, {"_id": 0})
#         user_transaction_history = user["transaction_history"]

#         return user_transaction_history

#     except Exception as e:
#         return f"transaction_history.error: {e}"
