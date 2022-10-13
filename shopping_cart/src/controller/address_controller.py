
from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from shopping_cart.src.models.entity.address import Address, AdressUpdateRequest
from shopping_cart.src.business.address_business import (
    insert_address,
    get_user_addresses,
    update_user_address
)


ADDRESSES_ROUTE = APIRouter(
    prefix="/magaluJA/users"
)


@ADDRESSES_ROUTE.post("/{user_email}/addresses")
async def add_address(user_email: str, new_address: Address):
    new_address = await insert_address(user_email, new_address)
    result = jsonable_encoder(new_address)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)

@ADDRESSES_ROUTE.get("/{user_email}/addresses")
async def get_addresses(user_email: str, zipcode: str = '', nickname: str = ''):
    user_addresses = await get_user_addresses(user_email, zipcode, nickname)
    return JSONResponse(status_code=status.HTTP_200_OK, content=user_addresses)

@ADDRESSES_ROUTE.put("/{user_email}/addresses/{id}")
async def update_address(user_email: str, id: str, body: AdressUpdateRequest):
    try:
        new_address = await update_user_address(user_email, id, body)
        return new_address
    except Exception as e:
        return "erro"
    
#@ADDRESSES_ROUTE.delete("/{user_email}/addresses/{address_cep}")
#async def delete_address(user_email: str, address_zipcode: str):
#    try:
#        removed_quantity = await remove_address(address_zipcode)
#        return removed_quantity
#    except Exception as e:
#        return "falha"
     