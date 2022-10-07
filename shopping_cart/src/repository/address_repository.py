from bd import obter_colecao
from src.models.address import Address


addresses_collection = obter_colecao("addresses")


async def add_address(user_email, newaddress: Address):
    try:
        ...
    except Exception as e:
        print(e)


async def get_user_addresses(user_email):
    user = addresses_collection.find_one(user_email)
    addresses = addresses_collection.find_one(user)
    return addresses


async def get_address_by_cep(user_email, address_cep):
    try:
        addresses = await get_user_addresses(user_email)
        address = addresses_collection.find_one(address_cep)
        return address
    except Exception as e:
        print(e)


async def get_addresses_delivery(user_email):
    try:
        addresses = await get_user_addresses(user_email)
        ...

    except Exception as e:
        print(e)


async def update_address(user_email, address_cep, address: Address):
    try:
        address = await get_address_by_cep(user_email, address_cep)
        ...

    except Exception as e:
        print(e)


async def delete_address(user_email, address_cep):
    try:
        address = await get_address_by_cep(user_email, address_cep)
        address = await addresses_collection.delete_one({"_cep": address_cep})
    except Exception as e:
        print(e)
