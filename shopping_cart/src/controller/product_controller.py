from fastapi import APIRouter, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from shopping_cart.src.models.entity.product import Product
from shopping_cart.src.business.product_business import(
    create_product,
    get_product,
    update_product_by_code
)
from shopping_cart.src.models.exceptions.exceptions import Bad_Request_Exception


PRODUCT_ROUTE = APIRouter(prefix="/magaluJA/products")

 
# Cadastrar produto
@PRODUCT_ROUTE.post("/")
async def post_product(product: Product):
    new_product = await create_product(product)
    result = jsonable_encoder(new_product)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=result)

# Pesquisar produto pelo código ou nome
@PRODUCT_ROUTE.get("/")
async def get_product_by_code_or_name(product_code: str = '', product_name: str = ''):
    if product_code == '' and product_name == '':
      raise Bad_Request_Exception('Precisa ser passado o código ou nome do produto')
  
    product = await get_product(product_code, product_name)
    if not product:
            raise Bad_Request_Exception('Produto não existe no banco de dados.')
    result = jsonable_encoder(product)
    return JSONResponse(status_code=status.HTTP_200_OK, content=result)
        
 # Atualizar dados do produto
@PRODUCT_ROUTE.put("/{product_code}", status_code=status.HTTP_204_NO_CONTENT)
async def update_product(product_code: str, fields: dict):
    return await update_product_by_code(product_code, fields)    
