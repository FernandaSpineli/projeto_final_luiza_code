from decimal import Decimal
from shopping_cart.src.models.user_models import User
from shopping_cart.src.models.product_models import Product
from shopping_cart.src.models.address import Address
from pydantic import BaseModel, Field
from typing import List, Optional


class CartItemSchema(BaseModel):
    id: str
    cart_id: int
    product: Product
    quantity: int = Field(default=0)
    total: Decimal = Field(max_digits=10, decimal_places=2)


class CartSchema(BaseModel):
    id: str
    user: User
    status: Optional[str] = Field(default='opened')
    items_quantity: int = Field(default=0)
    total: Optional[Decimal] = Field(
        default=0, max_digits=10, decimal_places=2)
    order_number: Optional[str]
