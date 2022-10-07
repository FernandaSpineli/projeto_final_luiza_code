from shopping_cart.src.models.user import User


def validate_user(user: User):
    if user is None:
        raise TypeError("Usuário não encontrado!")
