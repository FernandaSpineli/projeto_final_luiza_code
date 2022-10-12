from shopping_cart.src.models.entity.product import Product
from shopping_cart.src.repository.product_repository import (
    insert_new_product,
    find_product_by_id_on_bd,
    find_product_by_name_on_bd,
    remove_product_by_id,
    update_product_by_id_on_bd
)


async def create_new_product(new_product: Product):
    try:
        duplicated_product = await find_product_by_id_on_bd(new_product.id)
        if duplicated_product:
            return "O ID informado já está sendo usado. Verifique os dados e tente novamente."
        product_dict = new_product.dict()
        await insert_new_product(product_dict)
        return "Produto cadastrado com sucesso."
    except Exception as e:
        print(e)


async def find_product_by_id(product_id: str):
    try:
        product = await find_product_by_id_on_bd(product_id)
        if product:
            return product
        return "Produto não encontrado"
    except Exception as e:
        print(e)


async def find_product_by_name(product_name):
    try:
        products = await find_product_by_name_on_bd(product_name)
        if len(products) > 0:
            return products
        return "Nenhum resultado corresponde busca."
    except Exception as e:
        print(e)


async def delete_product_by_id(product_id: str):
    try:
        product = await find_product_by_id_on_bd(product_id)
        if product:
            check = await remove_product_by_id(product_id)
            if check:
                return "Produto excluido com sucesso."
            return "Erro ao excluir usuário"
        return "Nenhum produto cadastrado com o ID encontrado"
    except Exception as e:
        print(e)


async def update_product_by_id(product_id: str, fields: dict):
    try:
        product = await find_product_by_id_on_bd(product_id)
        if product:
            check = await update_product_by_id_on_bd(product_id, fields)
            if check:
                return "Produto atualizado com sucesso."
            print(product)
            return "Erro ao atualizar produto."
        return "Produto não encontrado."
    except Exception as e:
        print(e)
