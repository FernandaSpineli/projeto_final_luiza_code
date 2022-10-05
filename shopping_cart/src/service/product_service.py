from models.product_model import Product
from src.server.database import connect_db, db, disconnect_db


# Acrescenta um produto à base de dados 
async def insert_product(product):
    ...
    
# Atualiza características de um produto na base de dados
async def update_features_product(product_id, features):
    ... 
    
# Pesquisa um produto na base de dados pelo id
async def get_product_by_id(product_id):
    ... # Caso não exista, retorna uma exceção. 

# Pesquisa um produto na base de dados pelo nome. Caso não exista, retorna uma exceção. 
async def get_product_by_name(product_name):
    ... # Caso não exista, retorna uma exceção. Possibilidade de usar "like" aqui.


# Remove um produto da base de dados
async def remove_product(product_id):
    ...
