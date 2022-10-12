from typing import List
from pydantic import BaseModel

from shopping_cart.src.models.entity.address import Address
from shopping_cart.src.models.entity.shopping_cart import ShoppingCart
from shopping_cart.src.models.entity.transaction_history import TransactionHistory


class User(BaseModel):
    id: str
    name: str
    email: str
    password: str = None
    addresses: List[Address] = []
    shopping_cart: ShoppingCart
    transaction_history: TransactionHistory
 #   shopping_cart: ShoppingCart
 #   transaction_history: List[Purchase] = []

class UserResponse(BaseModel):
    name: str
    email: str
