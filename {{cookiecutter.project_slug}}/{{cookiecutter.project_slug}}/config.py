import functools

from cannula.contrib.config import BaseConfig
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker


class Config(BaseConfig):
    database_uri: str = "sqlite+aiosqlite:///db.sqlite"
    debug: bool = True
    port: int = 8000
    host: str = "0.0.0.0"

    @functools.cached_property
    def engine(self) -> AsyncEngine:
        return create_async_engine(self.database_uri)

    @property
    def session(self) -> async_sessionmaker:
        return async_sessionmaker(self.engine, expire_on_commit=False)


config = Config()
