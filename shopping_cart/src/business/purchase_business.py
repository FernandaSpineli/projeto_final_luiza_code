from shopping_cart.src.models.entity.purchase import Purchase
from shopping_cart.src.repository.purchase_repository import (
    create_new_purchase_on_bd,
    find_purchase_by_id_on_bd,
    find_transaction_history_on_bd
)
from shopping_cart.src.repository.user_repository import find_user_by_email


async def create_new_purchase(user_email: str, purchase: Purchase):
    try:
        user = await find_user_by_email(user_email)
        if user:
            duplicated_purchase = await find_purchase_by_id_on_bd(user_email, purchase.id)
            if duplicated_purchase:
                return "Já existe uma compra cadastrada para o ID informado."
            purchase_dict = purchase.dict()
            check = await create_new_purchase_on_bd(user_email, purchase_dict)
            if check:
                return "Compra finalizada com sucesso."
            return "Falha ao fechar a compra."
        return "Nenhum usuário cadastrado com o e-mail informado."
    except Exception as e:
        print(e)


async def find_purchase_by_id(user_email: str, purchase_id: str):
    try:
        user = await find_user_by_email(user_email)
        if user:
            purchase = await find_purchase_by_id_on_bd(user_email, purchase_id)
            if purchase:
                return purchase
            return "Nenhuma compra cadastrada com o ID informado."
        return "Nenhum usuário cadastrado com o e-mail informado."
    except Exception as e:
        print(e)


async def find_transaction_history(user_email: str):
    try:
        user = await find_user_by_email(user_email)
        if user:
            transaction_history = await find_transaction_history_on_bd(user_email)
            if transaction_history["transaction_history"]:
                return transaction_history
            return "O usuário não possui nenhuma compra."
        return "Nenhum usuário cadastrado com o e-mail informado."
    except Exception as e:
        print(e)
