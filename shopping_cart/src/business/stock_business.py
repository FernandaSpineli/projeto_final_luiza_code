from shopping_cart.src.models.entity.stock import Stock
from shopping_cart.src.repository.product_repository import search_product_id_on_bd
from shopping_cart.src.repository.stock_repository import update_product_amount_on_bd, update_stock_on_bd


async def update_product_amount(product_id: str, amount: dict):
    product = await search_product_id_on_bd(product_id)
    if product:
        await update_product_amount_on_bd(product_id, amount)
        return "Estoque atualizado com sucesso."
    return "Nenhum produto cadastrado com o ID informado."

async def update_stock(product_id: str, amount: dict):
    product = await search_product_id_on_bd(product_id)
    if product:
        await update_stock_on_bd(product_id, amount)
        return "Estoque atualizado com sucesso."
    return "Nenhum produto cadastrado com o ID informado."
