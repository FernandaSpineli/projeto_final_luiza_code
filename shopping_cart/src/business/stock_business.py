from shopping_cart.src.repository.product_repository import find_product_by_id_on_bd
from shopping_cart.src.repository.stock_repository import update_product_quantity_on_bd, update_stock_on_bd


async def update_product_quantity(product_id: str, sum: dict):
    product = await find_product_by_id_on_bd(product_id)
    if product:
        await update_product_quantity_on_bd(product_id, sum)
        return "Estoque atualizado com sucesso."
    return "Nenhum produto cadastrado com o ID informado."


async def update_stock(product_id: str, quantity: dict):
    product = await find_product_by_id_on_bd(product_id)
    if product:
        await update_stock_on_bd(product_id, quantity)
        return "Estoque atualizado com sucesso."
    return "Nenhum produto cadastrado com o ID informado."
