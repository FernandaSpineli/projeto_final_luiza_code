from shopping_cart.src.models.product_models import Product
from shopping_cart.src.models.cart_model import CartSchema
from shopping_cart.src.models.user_models import User


def validate_user(user: User):
    if user is None:
        raise TypeError("Usuário não encontrado!")


def validate_cart(cart: CartSchema):
    if cart is None:
        raise TypeError("Carrinho não encontrado!")


def validate_open_cart(cart: CartSchema):
    if cart is not None:
        raise TypeError(
            "Usuário já possui um carrinho aberto! Feche-o para continuar.")
    else:
        return cart


def validate_product(product: Product):
    if product is None:
        raise TypeError("Produto não encontrado!")


def validate_user_address(addresses):
    if len(addresses) == 0:
        raise TypeError(
            "Para fechar o carrinho, usuário precisa de um endereço cadastrado!")
