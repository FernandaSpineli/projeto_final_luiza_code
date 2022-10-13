from pydantic import BaseModel


class Address(BaseModel):
    id: int
    nickname: str
    street: str
    house_number: str
    zipcode: str
    city: str
    state: str

class AdressUpdateRequest(BaseModel):
  id: int
  nickname: str = None
  street: str = None
  house_number: str = None
  zipcode: str = None
  city: str = None
  state: str = None
