from shopping_cart.src.models.entity.product import Product
from shopping_cart.src.repository.product_repository import (
    insert_new_product,
    find_product_by_id_on_bd,
    find_product_by_name_on_bd,
    remove_product_by_id,
    update_product_by_id_on_bd,
)


async def create_new_product(new_product: Product):
    if await find_product_by_id_on_bd(new_product.id):
        return (
            "O ID informado já está sendo usado. Verifique os dados e tente novamente."
        )
    product_dict = new_product.dict()
    await insert_new_product(product_dict)
    return "Produto cadastrado com sucesso."


async def find_product_by_id(product_id: str):
    product = await find_product_by_id_on_bd(product_id)
    if product:
        return product
    return "Produto não encontrado."


async def find_product_by_name(product_name):
    products = await find_product_by_name_on_bd(product_name)
    if products:
        return products
    return "Nenhum resultado corresponde busca."


async def delete_product_by_id(product_id: str):
    if await find_product_by_id_on_bd(product_id):
        if await remove_product_by_id(product_id):
            return "Produto excluido com sucesso."
        return "Erro ao excluir usuário"
    return "Nenhum produto cadastrado com o ID encontrado"


async def update_product_by_id(product_id: str, fields: dict):
    product = await find_product_by_id_on_bd(product_id)
    if product:
        if "id" in fields:
            return "Não é possível alterar o ID do produto."
        if await update_product_by_id_on_bd(product_id, fields):
            return "Produto atualizado com sucesso."
        print(product)
        return "Erro ao atualizar produto."
    return "Produto não encontrado."
