from pydantic import BaseModel, Field

class Product(BaseModel):
    id: str = Field(None, min_length = 1)
    name: str = Field(None, min_length = 20, max_length = 100)
    description: str = Field (None, min_leght = 100, max_lenght = 500)
    category: str = Field(None, max_length = 30)
    subcategory: str = Field(None, max_length = 30)
    brand: str = Field(None, max_length = 30)
    color: str = Field(None, max_length = 20)
    fabric: str = Field(None, max_length = 100)
    dimensions: str = Field(None, max_length = 30)
    items_quantity: int = Field (None, ge = 1)
    price: float = Field (None, ge = 0)