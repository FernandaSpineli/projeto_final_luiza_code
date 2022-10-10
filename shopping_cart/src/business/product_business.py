from shopping_cart.src.models.entity.product import Product
from shopping_cart.src.repository.product_repository import(
    insert_new_product,
    find_product_by_id,
    find_product_by_name,
    remove_product_by_id,
    update_product_by_id
) 

# Regras para acrescentar um produto
async def create_product(new_product: Product):
    try:
        duplicated_product = await find_product_by_id(new_product.id)
        if duplicated_product:
            return ("O ID informado já está sendo usado. Verifique os dados e tente novamente.")
        product_dict = new_product.dict()    
        await insert_new_product(product_dict)
    except Exception as e:
        print(e)
    
# Regras para atualizar as características de um produto
async def update_product(product_id, fields):
    try:
        product = await find_product_by_id(product_id)
        if not product:
            return "Produto não encontrado"
        await update_product_by_id(product_id, fields) 
        updeted_product = await find_product_by_id(product_id)
        return updeted_product
    except Exception as e:
        print(e)
        
# Regras para pesquisar um produto na base de dados pelo id
async def get_product_by_id(product_id):
    try:
        product = await find_product_by_id(product_id)
        if not product:
            return "Produto não encontrado"
        return product
    except Exception as e:
        print(e)
        
# Regras para pesquisar um produto na base de dados pelo nome. Caso não exista, retorna uma exceção. 
async def get_product_by_name(product_name):
    try:
        product = await find_product_by_name(product_name)
        return product
    except Exception as e:
        print(e)
        
# Regras para remover um produto da base de dados
async def delete_product(product_id):
    # validar se o produto existe.
    try:
        product = await find_product_by_id(product_id)
        if not product:
            return "Produto não encontrado"
        removed_quantity = await remove_product_by_id(product_id)
        return removed_quantity
    except Exception as e:
        print(e)
