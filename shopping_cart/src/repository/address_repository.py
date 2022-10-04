from src.models.address import Address

async def  add_address(user_email, newaddress: Address):
    ...

async def get_user_addresses(user_email):
    ...
    
async def get_address_by_cep(user_email, address_cep):
    ...
 
async def get_addresses_delivery(user_email):
    ...

async def update_address(user_email, address_cep, address: Address):
    ...

async def delete_address(user_email, address_cep):
    try:
        address = await get_address_by_cep("ludomagalu@gmail.com")
        address = await addresses_collection.delete_one(
            {'_cep': address_cep}
        )
    except Exception as e:
        print(f'delete_address.error: {e}')
    
