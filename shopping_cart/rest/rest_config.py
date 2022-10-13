from fastapi import FastAPI

from shopping_cart.src.controller.main_controller import MAIN_ROUTE
from shopping_cart.src.controller.product_controller import PRODUCT_ROUTE
from shopping_cart.src.controller.user_controller import USER_ROUTE
from shopping_cart.src.controller.address_controller import ADDRESS_ROUTE
from shopping_cart.src.controller.stock_controller import STOCK_ROUTE
from shopping_cart.src.controller.shopping_cart_controller import SHOPPING_CART_ROUTE
from shopping_cart.src.controller.purchase_controller import TRANSACTION_HISTORY_ROUTE


def route_config(app: FastAPI):
    app.include_router(MAIN_ROUTE)
    app.include_router(PRODUCT_ROUTE)
    app.include_router(USER_ROUTE)
    app.include_router(ADDRESS_ROUTE)
    app.include_router(STOCK_ROUTE)
    app.include_router(SHOPPING_CART_ROUTE)
    app.include_router(TRANSACTION_HISTORY_ROUTE)


def create_api():
    app = FastAPI()
    route_config(app)
    return app
