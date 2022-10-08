from fastapi import APIRouter, status

from src.models.entity.address import Address
from src.models.repository.address_repository import (
    add_new_address,
    get_address_by_cep,
    get_user_addresses,
    delete_address
)
from src.models.handler_exceptions import(
    not_found_exception,
    conflict_exception
)

route_addresses = APIRouter(
    prefix="/api/users"
)


user = {
    "user_id": "001",
    "nome": "Lu",
    "email": "ludomagalu@gmail.com",
    "password": "123luiza#",
    "addresses": []
}

addresses = [
    {
        "01": {
            "cep": "13402-356",
            "cidade": "São Paulo",
            "estado": "SP",
            "logradouro": "Rua das Cores",
            "numero": 352
        },
        "02": {
            "cep": "11672-482",
            "cidade": "Bauru",
            "estado": "SP",
            "logradouro": "Rua dos Lanches",
            "numero": 90
        }
    }
]

@route_addresses.post("/{user_email}/addresses")
async def add_address(user_email, new_address: Address):
    try:
        address = new_address
        new_address = await add_new_address(user_email, address)
        return "Novo endereço cadastrado com sucesso."
    except Exception as e:
        return "erro"

@route_addresses.get("/{user_email}/addresses")
async def get_addresses(user_email):
    try:
       user_addresses = await get_user_addresses(user_email)
    except Exception as e:
        return not_found_exception.entity_not_found(addresses)
    
@route_addresses.get("/{user_email}/addresses/{address_cep}")
async def get_address_by_cep(user_email, address_cep):
    return "endereço encontrado!"    
@route_addresses.get("/{user_email}/addresses/delivery")
async def get_addresses_delivery(user_email):
    return "endereços que aceitam entrega"
    
@route_addresses.put("/{user_email}/addresses/{address_cep}")
async def update_address(user_email, address_cep):
    return "endereço atualizado com sucesso!"

@route_addresses.delete("/{user_email}/addresses/{address_cep}")
async def delete_address(user_email, address_cep):
     return "deletado"