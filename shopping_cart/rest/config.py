from typing import Callable, Tuple

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from src.models.handler_exceptions.conflict_exception import conflict_exception

from src.controller.cart_controller import cart_route, purchases_route
from src.controller.product_controller import product_route
from src.controller.address_controller import route_addresses
from src.models.handler_exceptions import (
    not_found_exception,
    conflict_exception
)


def configurar_interceptador_excecoes(app: FastAPI) -> Tuple[Callable]:
    async def interceptador_nao_encontrado_excecao(request: Request):
        return not_found_exception.entity_not_found(request)

    async def interceptador_outro_registro_excecao(request: Request):
        return conflict_exception.conflict_exception(request)

    return (
        interceptador_nao_encontrado_excecao,
        interceptador_outro_registro_excecao
    )


def configurar_rotas(app: FastAPI):
    # Publicando as rotas para o FastAPI.

    app.include_router(cart_route)
    app.include_router(purchases_route)
    app.include_router(product_route)
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
