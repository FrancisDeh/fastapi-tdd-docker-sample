import logging
from functools import lru_cache

from pydantic.networks import AnyUrl

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"  # dev, stage, prod
    testing: bool = bool(0)
    database_url: AnyUrl = None


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
