from pydantic import BaseModel
from typing import List


class CartItemSchema(BaseModel):
    cart_id: int
    product_id: int
    quantity: int
    total: float


class CartSchema(BaseModel):
    user_id: int
    codigo: str
    items: List[CartItemSchema]
    status: str
    items_quantity: int
    total: float
    address_id: int
    nro_pedido: str
