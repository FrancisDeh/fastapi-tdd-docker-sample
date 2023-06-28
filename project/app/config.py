import logging
from functools import lru_cache

from pydantic import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"  # dev, stage, prod
    testing: bool = bool(0)


@lru_cache()
async def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
