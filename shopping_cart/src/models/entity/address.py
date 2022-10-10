from xxlimited import Str
from pydantic import BaseModel

class Address(BaseModel):
    user_email: str
    nickname: str
    street: str
    house_number: int
    zipcode: str
    city: str
    state: Str
