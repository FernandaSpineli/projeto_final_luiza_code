from shopping_cart.src.models.entity.address import Address

from shopping_cart.src.repository.user_repository import find_user_by_email
from shopping_cart.src.repository.address_repository import (
    create_new_address_on_bd,
    find_user_addresses_on_bd,
    find_address_by_id_on_bd,
    remove_user_addresses_on_bd,
    remove_address_by_id_on_bd,
    update_address_by_id_on_bd
)


async def create_new_address(user_email: str, address: Address):
    if not await find_user_by_email(user_email):
        return "Nenhum usuário cadastrado com o e-mail informado."
    if await find_address_by_id_on_bd(user_email, address.id):
        return "O ID de endereço informado já está sendo usado. Verifique os dados e tente novamente."
    address_dict = address.dict()
    if await create_new_address_on_bd(user_email, address_dict):
        return "Endereço cadastrado com sucesso."


async def find_user_addresses(user_email: str):
    if not await find_user_by_email(user_email):
        return "Nenhum usuário cadastrado com o e-mail informado."
    addresses = await find_user_addresses_on_bd(user_email)
    if addresses:
        return addresses
    return "Nenhum endereço cadastrado para este usuário."


async def find_address_by_id(user_email: str, address_id: str):
    if not await find_user_by_email(user_email):
        return "Nenhum usuário cadastrado com o e-mail informado."
    return await find_address_by_id_on_bd(user_email, address_id)


async def remove_user_addresses(user_email: str):
    if await find_user_by_email(user_email):
        if await remove_user_addresses_on_bd(user_email):
            return "Todos os endereços do usuário foram excluidos."
    return "Nenhum usuário cadastrado com o e-mail informado."


async def remove_address_by_id(user_email: str, address_id: str):
    if await find_user_by_email(user_email):
        if await find_address_by_id(user_email, address_id):
            if await remove_address_by_id_on_bd(user_email, address_id):
                return "Endereço excluido com sucesso."
        return "Nenhum endereço cadastrado com o ID informado."
    return "Nenhum usuário cadastrado com o e-mail informado."


async def update_address_by_id(user_email: str, address_id: str, updated_address: Address):
    if await find_user_by_email(user_email):
        if address_id != updated_address.id:
            return "O ID do endereço deve permanecer o mesmo."
        address_dict = updated_address.dict()
        await update_address_by_id_on_bd(user_email, address_id, address_dict)
        return "Endereço atualizado com sucesso."
    return "Nenhum usuário cadastrado com o e-mail informado."
