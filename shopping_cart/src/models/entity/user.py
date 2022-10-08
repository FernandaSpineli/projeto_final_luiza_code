# nome do arquivo simplificado para user.py
from src.models.entity.address import Address
from src.models.entity.cart import ShoppingCart, Purchase
from typing import List
from pydantic import BaseModel


class User(BaseModel):
    id: str
    # mudado o id para str
    name: str
    email: str
    password: str
    addresses: List[Address] = []
    shopping_cart: ShoppingCart
    # adicionado o atributo shopping_cart, o "carrinho aberto"
    transaction_history: List[Purchase] = []
    # adicionado o atributo transaction_history, uma listagem dos "carrinhos fechados"
