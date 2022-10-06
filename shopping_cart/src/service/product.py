from models.product import Product


def validate_product(product: Product):
    if product is None:
        raise TypeError("Produto não encontrado!")
