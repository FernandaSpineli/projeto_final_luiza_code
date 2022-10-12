from typing import Callable, Tuple

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from shopping_cart.src.controller.main_controller import MAIN_ROUTE
from shopping_cart.src.controller.product_controller import PRODUCT_ROUTE
from shopping_cart.src.controller.user_controller import USER_ROUTE
from shopping_cart.src.controller.address_controller import ADDRESSES_ROUTE
from shopping_cart.src.controller.stock_controller import STOCK_ROUTE
from shopping_cart.src.controller.shopping_cart_controller import SHOPPING_CART_ROUTE
from shopping_cart.src.controller.purchase_controller import TRANSACTION_HISTORY_ROUTE
from shopping_cart.src.models.handler_exceptions import (
    not_found_exception,
    conflict_exception
)


def exception_config(app: FastAPI) -> Tuple[Callable]:
    async def interceptor_not_found_exception(request: Request):
        return not_found_exception.entity_not_found(request)

    async def interceptor_conflict_exception(request: Request):
        return conflict_exception.conflict_exception(request)

    return (
        interceptor_not_found_exception,
        interceptor_conflict_exception
    )


def route_config(app: FastAPI):
    app.include_router(MAIN_ROUTE)
    app.include_router(PRODUCT_ROUTE)
    app.include_router(USER_ROUTE)
    app.include_router(ADDRESSES_ROUTE)
    app.include_router(STOCK_ROUTE)
    app.include_router(SHOPPING_CART_ROUTE)
    app.include_router(TRANSACTION_HISTORY_ROUTE)


def rest_config(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    exception_config(app)


def create_api():
    app = FastAPI()

    rest_config(app)
    route_config(app)

    return app
