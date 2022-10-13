from fastapi import APIRouter

from shopping_cart.src.models.entity.address import Address
from shopping_cart.src.business.address_business import (
    create_new_address,
    find_user_addresses,
    find_address_by_id,
    remove_user_addresses,
    remove_address_by_id,
    update_address_by_id
)


ADDRESS_ROUTE = APIRouter(prefix="/magaluJA/{user_email}/addresses")


@ADDRESS_ROUTE.post("/")
async def post_address(user_email: str, address: Address):
    return await create_new_address(user_email, address)


@ADDRESS_ROUTE.get("/")
async def get_user_addresses(user_email: str):
    return await find_user_addresses(user_email)


@ADDRESS_ROUTE.get("/{address_id}")
async def get_address_by_id(user_email: str, address_id: str):
    return await find_address_by_id(user_email, address_id)


@ADDRESS_ROUTE.delete("/")
async def delete_user_addresses(user_email: str):
    return await remove_user_addresses(user_email)


@ADDRESS_ROUTE.delete("/{address_id}")
async def delete_address_by_id(user_email: str, address_id: str):
    return await remove_address_by_id(user_email, address_id)


@ADDRESS_ROUTE.put("/{address_id}")
async def put_address_by_id(user_email: str, address_id: str, updated_address: Address):
    return await update_address_by_id(user_email, address_id, updated_address)
