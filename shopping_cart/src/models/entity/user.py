from typing import List
from pydantic import BaseModel

from shopping_cart.src.models.entity.address import Address
from shopping_cart.src.models.entity.shopping_cart import ShoppingCart


class User(BaseModel):
    name: str
    email: str
    password: str
    addresses: List[Address] = []
    shopping_cart: ShoppingCart
 #   transaction_history: List[Purchase] = []
