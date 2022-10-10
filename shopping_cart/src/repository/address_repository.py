from typing import Optional

from shopping_cart.bd import get_collection


ADDRESSES_COLLECTION = get_collection("addresses")


async def insert_new_address(newaddress: dict) -> dict:
    try:
        new_address = await ADDRESSES_COLLECTION.insert_one(newaddress)
        return new_address
    except Exception as e:
        print(e)

async def find_user_addresses(user_email: str) -> Optional[dict]:
    try:
        user_addresses = await ADDRESSES_COLLECTION.find_one({"email": user_email})
        return user_addresses
    except Exception as e:
        print(e)

async def find_address_by_zipcode(address_zipcode: str) -> Optional[dict]:
    try:
        address = ADDRESSES_COLLECTION.find_one({"zipcode": address_zipcode})
        return address
    except Exception as e:
        print(e)

async def find_address_by_nickname(address_nickname: str) -> Optional[dict]:
    try:
        address = ADDRESSES_COLLECTION.find_one({"nickname": address_nickname})
        return address
    except Exception as e:
        print(e)

async def update_address(address_zipcode, features: dict) -> bool:
    try:
        address = await ADDRESSES_COLLECTION.update_one({'zipcode': address_zipcode}, {"$set": features})
        return address.modified_count == 1
    except Exception as e:
        print(e)

async def remove_address(address_zipcode):
    try:
        address = await ADDRESSES_COLLECTION.delete_one({"zipcode": address_zipcode})
        removed_quantity = address.deleted_count > 0
        return removed_quantity
    except Exception as e:
        print(e)
