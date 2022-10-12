from pydantic import BaseModel

class Product(BaseModel):
    code: str 
    name: str
    description: str
    category: str
    price: float
    subcategory: str = None
    specifications: str = None
    brand: str = None 
    color: str = None
    picture: str = None
    
class ProductResponse(BaseModel):
    code: str 
    name: str
    description: str
    category: str
    price: float