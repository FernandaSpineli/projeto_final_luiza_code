
from shopping_cart.src.models.entity.user import User
from shopping_cart.bd import get_collection


ADDRESSES_COLLECTION = get_collection("addresses")


async def insert_new_address(new_address: dict) -> dict:
    new_address = await ADDRESSES_COLLECTION.insert_one(new_address)
    return new_address

async def find_user_addresses(user: User) -> dict:
  address = await ADDRESSES_COLLECTION.find_one({'user._id': user['_id']})
  return address

async def update_address(address, new_address: dict) -> dict:
  result = await ADDRESSES_COLLECTION.update_one(
    { "_id": address["_id"] },
    {
      "$addToSet": {
        "address": new_address
      }
    }
  )
  return result

async def remove_address(address_zipcode):
        address = await ADDRESSES_COLLECTION.delete_one({"zipcode": address_zipcode})
        removed_quantity = address.deleted_count > 0
        return removed_quantity
