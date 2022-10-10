from shopping_cart.bd import get_collection
from shopping_cart.src.models.entity.address import Address


USERS_COLLECTION = get_collection("users")
ADDRESSES_COLLECTION = get_collection("addresses")


async def add_new_address(user_email, newaddress: Address):
    try:
            ADDRESSES_COLLECTION.insert_one(newaddress)
            return "endereço adicionado com sucesso"
    except Exception as e:
        print(e)

async def get_user_addresses(user_email):
    try:
        #user = await USERS_COLLECTION.find_one(user_email)
        #if user not in USERS_COLLECTION:
         #   user = await USERS_COLLECTION.insert_one(user) 
        addresses = await ADDRESSES_COLLECTION.find_one(user_email)
        return addresses
    except Exception as e:
        print(e)

async def get_address_by_cep(user_email, address_cep):
    try:
        address = ADDRESSES_COLLECTION.find_one(address_cep)
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
        address = await ADDRESSES_COLLECTION.delete_one({"_cep": address_cep})
    except Exception as e:
        print(e)
