from pydantic import BaseModel


class CartProduct(BaseModel):
    product_id: str
    amount: int
