from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings


class Configuracao(BaseSettings):
    bd_url: Optional[str] = None


def iniciar_configuracao():
    load_dotenv()
    return Configuracao()


configuracao = iniciar_configuracao()
