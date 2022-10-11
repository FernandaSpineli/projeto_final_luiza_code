from typing import List
from pydantic import BaseModel, Field

from shopping_cart.src.models.entity.address import Address
#from shopping_cart.src.models.entity.cart_product import ShoppingCart, Purchase


class User(BaseModel):
    name: str
    email: str
    password: str
    addresses: List[Address] = []
 #   shopping_cart: ShoppingCart
 #   transaction_history: List[Purchase] = []
