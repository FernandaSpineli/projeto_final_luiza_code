from fastapi import FastAPI


app = FastAPI()


user = {
    "user_id": "001",
    "nome": "Lu",
    "email": "ludomagalu@gmail.com",
    "password": "123lu#",
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


@app.get("/{user_id}/addresses")
async def listar_enderecos(user_id):
    return addresses
    
@app.post("/{user_id}/addresses")
async def adicionar_endereco(user_id):
    return "endereço adicionado"
    
@app.delete("/{user_id}/addresses/{address_id}")
async def deletar_endereco(user_id, address_id):
     return "deletado"