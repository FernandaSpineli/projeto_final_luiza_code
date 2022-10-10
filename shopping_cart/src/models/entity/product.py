from pydantic import BaseModel

class Product(BaseModel):
    id: str
    category: str
    subcategory: str
    name: str
    description: str
    specifications: str
    brand: str
    color: str
    price: float
    picture: str