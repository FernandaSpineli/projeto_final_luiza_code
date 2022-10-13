from shopping_cart.src.models.entity.stock import Stock
from shopping_cart.src.models.exceptions.exceptions import Bad_Request_Exception, Not_Found_Exception, Server_Exception
from shopping_cart.src.repository.product_repository import find_product_by_code
from shopping_cart.src.repository.stock_repository import get_stock_on_bd, update_product_quantity_on_bd, update_stock_on_bd

async def update_product_quantity(product_code: str, sum: dict):
    product = await find_product_by_code(product_code)
    stock = await get_stock_on_bd(product_code)
    stock_stock = stock["stock"]
    quantity = stock_stock + sum["stock"]
    if quantity >= 0:
        if product:
            updated = await update_product_quantity_on_bd(product_code, sum)
            if updated == False:
                raise Server_Exception('Erro ao atualizar quantidade de produto')
            return True
        raise Not_Found_Exception('Produto não encontrado')
    

async def update_stock(product_code: str, quantity: dict):
    product = await find_product_by_code(product_code)
    if product:
        if quantity["stock"] < 0:
            raise Bad_Request_Exception('Estoque não aceita quantidade menor que zero')
        updated = await update_stock_on_bd(product_code, quantity)
        if updated == False:
            raise Server_Exception('Erro ao atualizar estoque')
        return True
    raise Not_Found_Exception('Produto não cadastrado')
