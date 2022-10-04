from typing import List
from pydantic import BaseModel
from address import Address

# Classe dos dados do cliente
class User(BaseModel):
    id: int
    name: str
    email: str
    password: str
    addresses: List[Address] = []