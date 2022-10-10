from typing import Callable, Tuple

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from shopping_cart.src.controller.main_controller import MAIN_ROUTE
from shopping_cart.src.controller.product_controller import PRODUCT_ROUTE
from shopping_cart.src.controller.user_controller import USER_ROUTE
from shopping_cart.src.models.handler_exceptions import (
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
    app.include_router(MAIN_ROUTE)
    app.include_router(PRODUCT_ROUTE)
    app.include_router(USER_ROUTE) 

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