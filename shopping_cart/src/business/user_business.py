from shopping_cart.src.models.entity.user import User
from shopping_cart.src.repository.user_repository import (
    insert_new_user,
    find_user_by_email,
    remove_user_by_email,
    update_user
)


async def insert_user(new_user: User):
    if "@" not in new_user.email or len(new_user.email) < 4:
        return "E-mail inválido"
    if (new_user.email != new_user.shopping_cart.user_email) or (new_user.email != new_user.transaction_history.user_email):
        return "E-mail deve ser o mesmo para o usuário, carrinho e histórico de compras."
    if await find_user_by_email(new_user.email):
        return "O E-mail informado já está sendo usado. Verifique os dados e tente novamente."
    new_user_dict = new_user.dict()
    await insert_new_user(new_user_dict)
    return "Usuário cadastrado com sucesso."


async def get_user_email(email: str):
    found_user_dict = await find_user_by_email(email)
    if found_user_dict:
        return found_user_dict
    return "Usuário não encontrado"


async def delete_user_by_email(email: str):
    if await find_user_by_email(email):
        if await remove_user_by_email(email):
            return "Usuário excluído com sucesso."
        return "Erro ao excluir usuário."
    return "Nenhum usuário cadastrado com o e-mail informado."


async def update_user_by_email(email: str, features: dict):
    if await find_user_by_email(email):
        if await update_user(email, features):
            return "Usuário atualizado com sucesso."
        return "Erro ao atualizar usuário."
    return "Usuário não encontrado."
