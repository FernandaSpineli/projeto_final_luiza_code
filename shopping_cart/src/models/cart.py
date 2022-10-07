# sugestão de mudança dessas models
from pydantic import BaseModel
from typing import List
from shopping_cart.src.models.address import Address


class CartProduct(BaseModel):
    product_id: str
    amount: int


class ShoppingCart(BaseModel):
    user_id: str
    products: List[CartProduct] = []
    price_credit: float = 0.0
    price_debit: float = 0.0
    number_of_items: int = 0
    delivery_address_id: str = ""


class Purchase(BaseModel):
    id: str
    products: List[CartProduct]
    price: float
    number_of_items: int
    delivery_adress_id: str = ""
    payment_method: str
