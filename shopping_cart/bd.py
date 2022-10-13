from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorDatabase,
    AsyncIOMotorCollection,
)

from shopping_cart.config import config


def init_mongo() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(config.bd_url)


client_mongo = init_mongo()


def get_bd() -> AsyncIOMotorDatabase:
    return client_mongo.get_default_database("magaluJA")


def get_collection(collection_name: str) -> AsyncIOMotorCollection:
    bd = get_bd()
    return bd[collection_name]
