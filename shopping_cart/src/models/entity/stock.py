from pydantic import BaseModel


class Stock(BaseModel):
    product_code: str
    stock: int
