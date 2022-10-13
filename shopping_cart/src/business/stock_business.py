from shopping_cart.src.repository.product_repository import find_product_by_id_on_bd
from shopping_cart.src.repository.stock_repository import get_stock_on_bd, update_product_quantity_on_bd, update_stock_on_bd


async def update_product_quantity(product_id: str, sum: dict):
    sum["stock"] = int(sum["stock"])
    product = await find_product_by_id_on_bd(product_id)
    stock = await get_stock_on_bd(product_id)
    stock_stock = stock["stock"]
    quantity = stock_stock + sum["stock"]
    if quantity >= 0:
        if product:
            await update_product_quantity_on_bd(product_id, sum)
            return "Estoque atualizado com sucesso."
        return "Nenhum produto cadastrado com o ID informado."
    sum_stock = abs(sum["stock"])
    return f"Voce está tentando comprar {sum_stock} unidade(s) do produto {product_id}. Existe(m) {stock_stock} disponível(is) no estoque."


async def update_stock(product_id: str, quantity: dict):
    quantity["stock"] = int(quantity["stock"])
    if await find_product_by_id_on_bd(product_id):
        if quantity["stock"] < 0:
            return "Estoque não aceita quantidade negativa."
        await update_stock_on_bd(product_id, quantity)
        return "Estoque atualizado com sucesso."
    return "Nenhum produto cadastrado com o ID informado."
