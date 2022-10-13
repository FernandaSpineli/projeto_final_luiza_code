from pydantic import BaseModel


class Address(BaseModel):
    id: str
    nickname: str
    street: str
    house_number: str
    zipcode: str
    city: str
    state: str
