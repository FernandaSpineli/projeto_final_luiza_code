from fastapi import APIRouter
from fastapi.responses import HTMLResponse


MAIN_ROUTE = APIRouter(prefix="/MagaluJA")


@MAIN_ROUTE.get("/", response_class=HTMLResponse)
async def welcome_page():
    ...
    