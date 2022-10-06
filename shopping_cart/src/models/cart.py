# sugestão de mudança dessas models
from pydantic import BaseModel
from typing import List
from address import Address


class CartProduct:
    product_id: str
    amount: int


class ShoppingCart(BaseModel):
    user_id: str
    products: List[CartProduct] = []
    price_credit: float = 0.0
    price_debit: float = price_credit * 0.9
    number_of_items: int = 0
    delivery_address_id: str = ""


class Purchase(BaseModel):
    id: str
    products: List[CartProduct]
    price: float
    number_of_items: int
    delivery_adress_id: str = ""
    payment_method: str
