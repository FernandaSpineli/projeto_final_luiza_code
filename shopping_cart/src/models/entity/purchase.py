from shopping_cart.src.models.entity.cart_product import CartProduct

from pydantic import BaseModel
from typing import List, Dict


class Purchase(BaseModel):
    id: str
    products: List[CartProduct] = []
    price: float = 0.0
    number_of_items: int = 0
    delivery_address: Dict = {}
    payment_method: str = ""
