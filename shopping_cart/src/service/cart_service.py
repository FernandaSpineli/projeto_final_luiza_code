from shopping_cart.src.models.cart import Purchase


def validate_purchase(purchase: Purchase):
    if purchase is None:
        raise TypeError("Compra não encontrada!")
