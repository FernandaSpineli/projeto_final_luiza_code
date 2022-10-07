from fastapi import APIRouter, status


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

@route_addresses.get("/{user_email}/addresses")
async def get_addresses(user_email):
    return addresses
    
@route_addresses.post("/{user_email}/addresses")
async def add_address(user_email):
    return "endereço adicionado"

@route_addresses.get("/{user_email}/addresses/{address_cep}")
async def get_address_by_cep(user_email, address_cep):
    return "endereço encontrado!"    

@route_addresses.put("/{user_email}/addresses/{address_cep}")
async def update_address(user_email, address_cep):
    return "endereço atualizado com sucesso!"

@route_addresses.delete("/{user_email}/addresses/{address_cep}")
async def delete_address(user_email, address_cep):
     return "deletado"