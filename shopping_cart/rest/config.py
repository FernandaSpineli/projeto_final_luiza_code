from typing import Callable, Tuple

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from models.handler_exceptions.conflict_exception import conflict_exception

from src.controller.cart_controller import rota_carrinho
from src.controller.address_controller import route_addresses
from src.models.handler_exceptions import (
    not_found_exception,
    conflict_exception
)


def responder_nao_encontrado_excecao(requisicao: Request):
    return not_found_exception.entity_not_found()


def responder_outro_registro_excecao(requisicao: Request):
    return conflict_exception.conflict_exception()

def configurar_interceptador_excecoes(app: FastAPI) -> Tuple[Callable]:
    async def interceptador_naoencontradoexcecao(request: Request):
        return responder_nao_encontrado_excecao(request)

    async def interceptador_outroregistroexcecao(request: Request):
        return responder_outro_registro_excecao(request)

    return (
        interceptador_naoencontradoexcecao,
        interceptador_outroregistroexcecao,
    )


def configurar_rotas(app: FastAPI):
    # Publicando as rotas para o FastAPI.
    app.include_router(rota_carrinho)
    app.include_router(route_addresses)


def configurar_api_rest(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    configurar_interceptador_excecoes(app)


def criar_aplicacao_fastapi():
    app = FastAPI()

    configurar_api_rest(app)
    configurar_rotas(app)

    return app
