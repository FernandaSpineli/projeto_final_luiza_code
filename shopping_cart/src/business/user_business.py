from shopping_cart.src.controller.user_controller import User
from shopping_cart.src.repository.user_repository import (
    find_user_by_id,
    set_new_user,
    find_user_by_email,
    find_user_by_name,
    remove_user_by_email,
    set_user_by_email
)


async def get_user_by_id(user_id: str):
    try:
        user = find_user_by_id(user_id)
        return user
    except Exception as e:
        print(e)

async def post_user(user_email, new_user: User):
    try:
        new_user = set_new_user(user_email)
        return new_user
    except Exception as e:
        print(e)

async def get_user_by_email(user_email):
    try:
        user = find_user_by_email(user_email)
        return user
    except Exception as e:
        print(e)

async def get_user_by_name(user_name):
    try:
        user = find_user_by_name(user_name)
        return user
    except Exception as e:
        print(e)

async def delete_user_by_email(user_email):
    try:
        user_deleted = remove_user_by_email(user_email)
        return user_deleted
    except Exception as e:
        print(e)

async def update_user_by_email(user_email):
    try:
        user_updated = set_user_by_email(user_email)
        return user_updated
    except Exception as e:
        print(e)
