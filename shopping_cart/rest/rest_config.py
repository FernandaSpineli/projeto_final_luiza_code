from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from shopping_cart.src.controller.main_controller import MAIN_ROUTE
from shopping_cart.src.controller.product_controller import PRODUCT_ROUTE
from shopping_cart.src.controller.user_controller import USER_ROUTE
from shopping_cart.src.controller.address_controller import ADDRESSES_ROUTE
from shopping_cart.src.controller.stock_controller import STOCK_ROUTE
from shopping_cart.src.controller.shopping_cart_controller import SHOPPING_CART_ROUTE
from shopping_cart.src.controller.purchase_controller import TRANSACTION_HISTORY_ROUTE
from shopping_cart.src.models.exceptions.exceptions import Bad_Request_Exception, Duplicated_Exception, Not_Found_Exception, Server_Exception

def create_api():
    app = FastAPI()

    rest_config(app)
    route_config(app)

    return app


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
    
    @app.exception_handler(Exception)
    async def exception_handler(request: Request, exception: Exception):
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
      return JSONResponse(
        status_code=status_code,
        content={'status_code': status_code, 'message': f'Erro interno no servidor - {str(exception)}'}
      )

    @app.exception_handler(Server_Exception)
    async def server_exception_handler(request: Request, exception: Server_Exception):
      status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
      return JSONResponse(
        status_code=status_code,
        content={'status_code': status_code, 'message': exception.message}
      )

    @app.exception_handler(Not_Found_Exception)
    async def not_found_exception_handler(request: Request, exception: Not_Found_Exception):
      status_code=status.HTTP_404_NOT_FOUND
      return JSONResponse(
        status_code=status_code,
        content={'status_code': status_code, 'message': exception.message}
      )

    @app.exception_handler(Duplicated_Exception)
    async def duplicated_exception_handler(request: Request, exception: Duplicated_Exception):
      status_code = status.HTTP_409_CONFLICT
      return JSONResponse(
        status_code=status_code, 
        content={'status_code': status_code, 'message': exception.message}
      )

    @app.exception_handler(Bad_Request_Exception)
    async def duplicated_exception_handler(request: Request, exception: Duplicated_Exception):
      status_code = status.HTTP_400_BAD_REQUEST
      return JSONResponse(
        status_code=status_code, 
        content={'status_code': status_code, 'message': exception.message}
      )
