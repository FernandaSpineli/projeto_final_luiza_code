from pydantic import BaseModel


class Address(BaseModel):
    name: str
    street: str
    house_number: int
    zipcode: str
    city: str
    state: str
