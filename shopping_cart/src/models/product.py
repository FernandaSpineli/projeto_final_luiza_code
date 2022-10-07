from pydantic import BaseModel


class Product(BaseModel):
    id: str
    name: str
    description: str
    category: str
    subcategory: str
    brand: str
    color: str
    fabric: str
    dimensions: str
    items_quantity: int
    price: float


class ProductStock(BaseModel):
    product_id: str
    stock: int
