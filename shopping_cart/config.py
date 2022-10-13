from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings


class Config(BaseSettings):
    bd_url: Optional[str] = None


def config_start():
    load_dotenv()
    return Config()


config = config_start()
