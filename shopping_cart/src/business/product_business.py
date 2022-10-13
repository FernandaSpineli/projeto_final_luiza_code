from shopping_cart.src.models.entity.product import Product, ProductResponse

from shopping_cart.src.models.exceptions.exceptions import Bad_Request_Exception, Duplicated_Exception, Not_Found_Exception, Server_Exception
from shopping_cart.src.repository.product_repository import(
    insert_new_product,
    find_product_by_code,
    find_product_by_name,
    remove_product_by_id,
    update_product_by_code_db,
) 

async def create_product(new_product: Product):
    exist_product = await find_product_by_code(new_product.code)
    if exist_product:
        raise Duplicated_Exception('Produto já cadastrado')
    try:
        product_dict = new_product.dict()
        product_inserted = await insert_new_product(product_dict)
        
        product = ProductResponse(
            code = product_inserted['code'],
            name = product_inserted['name'],
            description = product_inserted['description'],
            category = product_inserted['category'],
            price = product_inserted['price'],
        )
        return product
    except Exception as e:
        raise Server_Exception(f'Erro ao cadastrar produto - {str(e)}')
    
        
# Regras para pesquisar um produto na base de dados pelo id
async def get_product(product_code, product_name):
    response = []
    if product_code:
        product = await find_product_by_code(product_code)
        if product:
            response.append(product)
    else:
        response = await find_product_by_name(product_name)
        
    if len(response) > 0:
        return response
    
    raise Not_Found_Exception('Produto não encontrado')
        
# Regras para remover um produto da base de dados
async def delete_product(product_id):
        product = await find_product_by_code(product_id)
        if not product:
            return "Produto não encontrado"
        removed_quantity = await remove_product_by_id(product_id)
        return removed_quantity

async def update_product_by_code(product_code, fields):
    exist_product = await find_product_by_code(product_code)
    if not exist_product:
        raise Bad_Request_Exception("O produto informado não está cadastrado")
    updated = await update_product_by_code_db(product_code, fields)
    if updated == False:
        raise Server_Exception('Erro ao atualizar o produto')
        