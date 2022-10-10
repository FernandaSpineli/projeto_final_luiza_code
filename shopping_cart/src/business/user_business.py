from shopping_cart.src.models.entity.user import User
from shopping_cart.src.repository.user_repository import (
    insert_new_user,
    find_user_by_id,
    find_user_by_email,
    find_user_by_name,
    remove_user_by_email,
    update_user_by_email
)

async def insert_user(new_user: User):
    try:
        duplicated_user = await find_user_by_email(new_user.email)
        if duplicated_user:
            return "O E-mail informado já está sendo usado. Verifique os dados e tente novamente."
        user_dict = new_user.dict()
        await insert_new_user(user_dict)
        return "Usuário cadastrado com sucesso."
    except Exception as e:
        print(e)
        
async def get_user_by_id(user_id: str):
    try:
        user = find_user_by_id(user_id)
        if not user:
            return "Usuario não encontrado"
        return user
    except Exception as e:
        print(e)

async def get_user_by_email(user_email):
    try:
        user = find_user_by_email(user_email)
        if not user:
            return "Usuario não encontrado"
        return user
    except Exception as e:
        print(e)

async def get_user_by_name(user_name):
    try:
        user = find_user_by_name(user_name)
        if not user:
            return "Usuario não encontrado"
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
        user = find_user_by_email(user_email)
        if not user:
            return "Usuario não encontrado"
        user_updated = update_user_by_email(user_email)
        return user_updated
    except Exception as e:
        print(e)
