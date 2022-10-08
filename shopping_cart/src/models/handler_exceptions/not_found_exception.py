from fastapi import Request, status
from fastapi.responses import JSONResponse

def entity_not_found(requisicao: Request):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "mensagem": 'Erro'
        }
    )