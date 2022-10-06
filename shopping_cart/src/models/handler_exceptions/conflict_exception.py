from fastapi import Request, status
from fastapi.responses import JSONResponse

def response_conflict_exception(requisicao: Request):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "mensagem": 'Erro'
        }
    )