from pydantic import BaseModel
from typing import List

from shopping_cart.src.models.entity.cart_product import CartProduct


class ShoppingCart(BaseModel):
    user_email: str
    products: List[CartProduct] = []
    price_credit: float = 0.0
    price_debit: float = 0.0
    number_of_items: int = 0
    delivery_address_id: str = ""
