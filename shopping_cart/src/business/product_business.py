from shopping_cart.src.models.entity.product import Product
import shopping_cart.src.repository.product_repository as product_db

# Regras para acrescentar um produto
async def insert_product(product: Product):
    duplicated_product = await product_db.search_by_id(product.id)
    print(duplicated_product)
    if duplicated_product is not None:
        return "O id escolhido pertence a um produto no banco de dados."
    
    product_dict = product.dict()    
    await product_db.insert_new_product(product_dict)
    
# Regras para atualizar as características de um produto
async def update_features_product(product_id, features):
    await product_db.update_by_id(product_id, features) 
    
# Regras para pesquisar um produto na base de dados pelo id
async def get_product_by_id(product_id):
    product = await product_db.search_by_id(product_id)
    
    if not product:
        return "Produto não encontrado"
    
    return product

# Regras para pesquisar um produto na base de dados pelo nome. Caso não exista, retorna uma exceção. 
async def get_product_by_name(product_name):
    product = await product_db.search_by_name(product_name)
    return product

# Regras para remover um produto da base de dados
async def remove_product(product_id):
    # validar se o produto existe.
    removed_quantity = await product_db.remove_by_id(product_id)
    return removed_quantity

