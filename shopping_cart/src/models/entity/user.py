from typing import List
from pydantic import BaseModel

from shopping_cart.src.models.entity.address import Address
from shopping_cart.src.models.entity.shopping_cart import ShoppingCart
from shopping_cart.src.models.entity.transaction_history import TransactionHistory


class User(BaseModel):
    name: str
    email: str
    password: str
    addresses: List[Address] = []
    shopping_cart: ShoppingCart = None
    transaction_history: TransactionHistory = None

class UserResponse(BaseModel):
    name: str
    email: str
