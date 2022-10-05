from fastapi import APIRouter, status
from src.repository.cart_repository import (
    CartSchema,
    buscar_carrinho_aberto,
    fechar_carrinho_aberto,
    inserir_novo_carrinho,
    inserir_novo_produto_carrinho
)

rota_carrinho = APIRouter(
    prefix="/api/carrinho"
)


@rota_carrinho.post(
    "/{id_usuario}/novo",
    status_code=status.HTTP_201_CREATED,
    # response_model=CartSchema
)
async def criar_carrinho(id_usuario: str):
    return await inserir_novo_carrinho(id_usuario)


@rota_carrinho.put(
    "/{codigo_carrinho}/produtos",
    status_code=status.HTTP_202_ACCEPTED
)
async def adicionar_produto(codigo_carrinho: str, codigo_produto: str):
    return await inserir_novo_produto_carrinho(codigo_carrinho, codigo_produto)


@rota_carrinho.get(
    "/{id_usuario}",
    # response_model=CartSchema
)
async def pesquisar_carrinho(id_usuario: str):
    return await buscar_carrinho_aberto(id_usuario)


@rota_carrinho.put(
    "/{codigo_carrinho}/status",
    status_code=status.HTTP_202_ACCEPTED
)
async def fechar_carrinho(codigo_carrinho: str):
    return await fechar_carrinho_aberto(codigo_carrinho)
