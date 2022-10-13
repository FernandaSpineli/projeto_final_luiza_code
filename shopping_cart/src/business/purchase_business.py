from shopping_cart.src.models.entity.purchase import Purchase
from shopping_cart.src.models.exceptions.exceptions import Duplicated_Exception, Not_Found_Exception, Server_Exception
from shopping_cart.src.repository.purchase_repository import (
    create_new_purchase_on_bd,
    find_purchase_by_id_on_bd,
    find_transaction_history_on_bd
)
from shopping_cart.src.repository.user_repository import find_user_by_email

async def create_new_purchase(user_email: str, purchase: Purchase):
    found_user = await find_user_by_email(user_email)
    if found_user:
        duplicated_purchase = await find_purchase_by_id_on_bd(user_email, purchase.id)
        if duplicated_purchase:
            raise Duplicated_Exception('Já existe uma compra cadastrada para o ID informado')
        
        purchase_dict = purchase.dict()
        purchase_created = await create_new_purchase_on_bd(user_email, purchase_dict)
        if purchase_created:
            updated = await find_purchase_by_id_on_bd(user_email, purchase.id)
            if updated:
                response = Purchase(
                    id= purchase.id,
                    products= purchase.products,
                    price= purchase.price,
                    number_of_items= purchase.number_of_items,
                    delivery_adress_id= purchase.delivery_adress_id,
                    payment_method= purchase.payment_method
                )
                return response
        raise Server_Exception('Erro ao cadastrar purchase')
    raise Not_Found_Exception('Usuário não cadastrado')


async def find_purchase_by_id(user_email: str, purchase_id: str):
        user = await find_user_by_email(user_email)
        if user:
            purchase = await find_purchase_by_id_on_bd(user_email, purchase_id)
            if purchase:
                response = Purchase(
                id= purchase['id'],
                products= purchase['products'],
                price= purchase['price'],
                number_of_items= purchase['number_of_items'],
                delivery_adress_id= purchase['delivery_adress_id'],
                payment_method= purchase['payment_method']
                )
                return response
            raise Not_Found_Exception("Nenhuma compra cadastrada com o ID informado") 
        raise Not_Found_Exception('Usuário não cadastrado')

async def find_transaction_history(user_email: str):
        user = await find_user_by_email(user_email)
        if user:
            transaction_history = await find_transaction_history_on_bd(user_email)
            if transaction_history["transaction_history"]:
                return transaction_history
            raise Not_Found_Exception("O usuário não possui nenhuma compra")
        raise Not_Found_Exception('Usuário não cadastrado')

