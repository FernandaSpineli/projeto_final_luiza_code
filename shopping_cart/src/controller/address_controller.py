from typing import List
from fastapi import APIRouter

from shopping_cart.src.models.entity.address import Address
from shopping_cart.src.business.address_business import (
    insert_address,
    get_user_addresses,
    get_address_by_zipcode,
    get_address_by_nickname,
    remove_address,
    update_address_by_zipcode
)


ADDRESSES_ROUTE = APIRouter(
    prefix="/api/users"
)


@ADDRESSES_ROUTE.post("/{user_email}/addresses")
async def add_address(user_email: str, new_address: Address):
    try:
        new_address = await insert_address(user_email, new_address)
        return new_address
    except Exception as e:
        return "erro"

@ADDRESSES_ROUTE.get("/{user_email}/addresses", response_model = List[Address])
async def get_addresses(user_email: str):
    try:
       user_addresses = await get_user_addresses(user_email)
       return user_addresses
    except Exception as e:
        return "lista não encontrada"
    
@ADDRESSES_ROUTE.get("/{user_email}/addresses/{address_zipcode}", response_model= Address)
async def get_user_address_by_nickname(user_email: str, address_nickname: str):
    try:
        address = await get_address_by_nickname(address_nickname)
        return address
    except Exception as e:
        return "endereço não encontrado"

@ADDRESSES_ROUTE.get("/{user_email}/addresses/{address_zipcode}", response_model= Address)
async def get_user_address_by_zipcode(user_email: str, address_zipcode: str):
    try:
        address = await get_address_by_zipcode(address_zipcode)
        return address
    except Exception as e:
        return "endereço não encontrado"
    
@ADDRESSES_ROUTE.put("/{user_email}/addresses/{address_zipcode}")
async def update_address(user_email: str, address_zipcode: str, fields: dict):
    try:
        new_address = await update_address_by_zipcode(address_zipcode, fields)
        return new_address
    except Exception as e:
        return "erro"
    
@ADDRESSES_ROUTE.delete("/{user_email}/addresses/{address_cep}")
async def delete_address(user_email: str, address_zipcode: str):
    try:
        removed_quantity = await remove_address(address_zipcode)
        return removed_quantity
    except Exception as e:
        return "falha"
     