from pydantic import BaseModel


class Address(BaseModel):
    user_email: str
    nickname: str
    street: str
    house_number: int
    zipcode: str
    city: str
    state: str

class AdressUpdateRequest(BaseModel):
  id: int
  nickname: str = None
  street: str = None
  house_number: int = None
  zipcode: str = None
  city: str = None
  state: str = None
