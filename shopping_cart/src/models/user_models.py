from shopping_cart.src.models.address import Address
from typing import List
from pydantic import BaseModel

# Classe dos dados do cliente


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    addresses: List[Address] = []
