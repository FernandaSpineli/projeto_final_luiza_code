from fastapi import FastAPI
from models.product_models import Product
import product_rules

app = FastAPI()

 
# Cadastrar produto
@app.post("/product")
async def create_product(product: Product):
    new_product = await product_rules.insert_product(product)
    return new_product 
    
 # Atualizar dados do produto
@app.put("/product/{id}")
async def update_product(id: str, features: dict):
    updated_product = await product_rules.update_features_product(id, features)
    return updated_product

# Pesquisar produto pelo código
@app.get("/product/search_id/{id}")
async def search_product_by_id(id: str):
    product = await product_rules.get_product_by_id(id)
    return product

# Pesquisar produto pelo nome
@app.get("/product/search_name/{name}/")
async def search_product_by_name(name: str):
    product = await product_rules.get_product_by_name(name) 
    return product
    
# Remover um produto
@app.delete("/produto/{id}/")
async def delete_product(id: str):
    deleted_product = await product_rules.remove_product(id)
    return deleted_product
