from shopping_cart.src.models.entity.address import Address

from shopping_cart.src.repository.address_repository import(
    insert_new_address,
    find_address_by_zipcode,
    find_user_addresses,
    find_address_by_nickname,
    update_address,
    remove_address
)

async def insert_address(new_address: Address):
    try:
        duplicated_address = await find_address_by_zipcode(new_address.zipcode)
        if duplicated_address:
            return "O Endereço informado já está sendo usado. Verifique os dados e tente novamente."
        address_dict = new_address.dict()
        await insert_new_address(address_dict)
        return "Endereço cadastrado com sucesso."
    except Exception as e:
        print(e)
        
async def get_user_addresses(user_email):
    try:
        addresses = await find_user_addresses(user_email)
        if not addresses:
            return "Lista de endereços não encontrada."
        return addresses
    except Exception as e:
        print(e)

async def get_address_by_zipcode(address_zipcode):
    try:
        address = await find_address_by_zipcode(address_zipcode)
        if not address:
            return "Endereço não encontrado"
        return address
    except Exception as e:
        print(e)
        
async def get_address_by_nickname(address_nickname):
    try:
        address = await find_address_by_nickname(address_nickname)
        if not address:
            return "Endereço não encontrado"
        return address
    except Exception as e:
        print(e)
        
async def delete_address_by_zipcode(address_zipcode):
    try:
        address = await get_address_by_zipcode(address_zipcode)
        address_deleted = await remove_address(address.zipcode)
        return address_deleted
    except Exception as e:
        print(e)
        
async def update_address_by_zipcode(address_zipcode, fields):
    try:
        address = await get_address_by_zipcode(address_zipcode)
        address_to_update = await update_address(address.zipcode, fields)
        address_updated = await get_address_by_zipcode(address_to_update.zipcode)
        return address_updated
    except Exception as e:
        print(e)