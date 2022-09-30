from fastapi import APIRouter, status

rota_carrinho = APIRouter(
    prefix="/api/carrinho"
)

@rota_carrinho.get(
    "/",
    status_code=status.HTTP_201_CREATED,
)
def teste():
  return 'Teste Inicial'
