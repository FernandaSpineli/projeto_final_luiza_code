from shopping_cart.src.models.entity.user import User, UserResponse
from shopping_cart.src.models.exceptions.exceptions import Duplicated_Exception, Server_Exception
from shopping_cart.src.repository.user_repository import (
    insert_new_user,
    find_user_by_email,
    remove_user_by_email,
    update_user
)


async def insert_user(new_user: User):
    exist_user = await find_user_by_email(new_user.email)
    if exist_user:
        raise Duplicated_Exception('Usuário já cadastrado')

    try:
        user_dict = new_user.dict()
        user_inserted = await insert_new_user(user_dict)

        user = UserResponse(
        name=user_inserted['name'],
        email=user_inserted['email']
        )
        return user
    except Exception as e:
        raise Server_Exception(f'Erro ao cadastrar usuário - {str(e)}')
        
        
async def get_user_by_id(user_id: str):
    try:
        found_user_dict = await find_user_by_email(email)
        if found_user_dict:
            return found_user_dict
        return "Usuário não encontrado"
    except Exception as e:
        print(e)


async def delete_user_by_email(email: str):
    try:
        user = await find_user_by_email(email)
        if user:
            check = await remove_user_by_email(email)
            if check:
                return "Usuário excluído com sucesso."
            return "Erro ao excluir usuário."
        return "Nenhum usuário cadastrado com o e-mail informado."

    except Exception as e:
        print(e)


async def update_user_by_email(email: str, features: dict):
    try:
        user = await find_user_by_email(email)
        if user:
            check = await update_user(email, features)
            if check:
                return "Usuário atualizado com sucesso."
            return "Erro ao atualizar usuário."
        return "Usuário não encontrado."
    except Exception as e:
        print(e)
