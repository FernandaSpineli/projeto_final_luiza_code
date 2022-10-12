from shopping_cart.src.models.entity.cart_product import CartProduct

from pydantic import BaseModel
from typing import List


class Purchase(BaseModel):
    id: str
    products: List[CartProduct] = []
    price: float = 0.0
    number_of_items: int = 0
    delivery_adress_id: str = ""
    payment_method: str = ""
