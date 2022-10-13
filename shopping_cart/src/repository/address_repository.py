from shopping_cart.bd import get_collection
from shopping_cart.src.repository.user_repository import find_user_by_email, update_user


async def create_new_address_on_bd(user_email: str, address: dict):
    user = await find_user_by_email(user_email)
    address_list = user["addresses"]
    address_list.append(address)
    return await update_user(user_email, {"addresses": address_list})


async def find_user_addresses_on_bd(user_email: str):
    user = await find_user_by_email(user_email)
    return user["addresses"]


async def find_address_by_id_on_bd(user_email: str, address_id: str):
    user = await find_user_by_email(user_email)
    address_list = user["addresses"]
    for address in address_list:
        if address["id"] == address_id:
            return address
    return False


async def remove_user_addresses_on_bd(user_email: str):
    return await update_user(user_email, {"addresses": []})


async def remove_address_by_id_on_bd(user_email: str, address_id: str):
    user = await find_user_by_email(user_email)
    address_list = user["addresses"]
    for address in address_list:
        if address["id"] == address_id:
            address_list.remove(address)
    return await update_user(user_email, {"addresses": address_list})


async def update_address_by_id_on_bd(user_email: str, address_id: str, updated_address: dict):
    user = await find_user_by_email(user_email)
    address_list = user["addresses"]
    for address in address_list:
        if address["id"] == address_id:
            address_list.remove(address)
    address_list.append(updated_address)
    return await update_user(user_email, {"addresses": address_list})
