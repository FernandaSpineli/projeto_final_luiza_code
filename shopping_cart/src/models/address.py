from pydantic import BaseModel

class Address(BaseModel):
    cep = str
    cidade = str
    estado = str
    logradouro = str
    numero = int