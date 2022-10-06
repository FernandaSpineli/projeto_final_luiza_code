from shopping_cart.src.models.address import Address


def validate_address(address: Address):
    if address is None:
        raise TypeError("Endereço não encontrado!")
