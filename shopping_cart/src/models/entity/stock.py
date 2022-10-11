from pydantic import BaseModel


class Stock(BaseModel):
    product_id: str
    stock: int
