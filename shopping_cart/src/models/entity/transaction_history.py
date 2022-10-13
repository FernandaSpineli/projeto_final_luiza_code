from shopping_cart.src.models.entity.purchase import Purchase

from pydantic import BaseModel
from typing import List


class TransactionHistory(BaseModel):
    user_email: str
    transaction_history: List[Purchase] = []
