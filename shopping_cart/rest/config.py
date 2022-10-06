from typing import Callable, Tuple

from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from shopping_cart.src.controller.cart_controller import cart_route, purchases_route
from shopping_cart.src.controller.product_controller import product_route


def responder_naoencontradoexcecao(requisicao: Request):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND, content={"mensagem": "Erro"}
    )


def responder_outroregistroexcecao(requisicao: Request):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT, content={"mensagem": "Erro"}
    )


def configurar_interceptador_excecoes(app: FastAPI) -> Tuple[Callable]:
    async def interceptador_naoencontradoexcecao(request: Request):
        return responder_naoencontradoexcecao(request)

    async def interceptador_outroregistroexcecao(request: Request):
        return responder_outroregistroexcecao(request)

    return (
        interceptador_naoencontradoexcecao,
        interceptador_outroregistroexcecao,
    )


def configurar_rotas(app: FastAPI):
    # Publicando as rotas para o FastAPI.
    app.include_router(cart_route)
    app.include_router(purchases_route)
    app.include_router(product_route)


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
