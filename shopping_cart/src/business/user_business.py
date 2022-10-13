from shopping_cart.src.models.entity.user import User, UserResponse
from shopping_cart.src.models.exceptions.exceptions import Bad_Request_Exception, Duplicated_Exception, Not_Found_Exception, Server_Exception
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
        response_db = await insert_new_user(user_dict)
        
        if response_db.inserted_id:
            user = UserResponse(
                name=new_user.name,
                email=new_user.email
            )
            return user
    except Exception as e:
        raise Server_Exception(f'Erro ao cadastrar usuário - {str(e)}')

async def get_user_by_email(user_email: str):
    user_found = await find_user_by_email(user_email)
    if user_found:
            user = UserResponse(
                name=user_found['name'],
                email=user_found['email']
            )
            return user
    raise Not_Found_Exception('Usuario não cadastrado')
        
async def update_user_by_email(user_email: str, fields: dict):
    exist_user = await find_user_by_email(user_email)
    if not exist_user:
        raise Bad_Request_Exception("O usuário informado não está cadastrado")
    updated = await update_user(user_email, fields)
    if updated == False:
        raise Server_Exception('Erro ao atualizar o usuário')

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
