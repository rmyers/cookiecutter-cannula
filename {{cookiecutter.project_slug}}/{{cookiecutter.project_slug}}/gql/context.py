from __future__ import annotations
from cannula.context import Context as BaseContext
from cannula.datasource.orm import DatabaseRepository
from sqlalchemy import text, true
from sqlalchemy.ext.asyncio import async_sessionmaker
from typing import Optional, Sequence
from uuid import UUID
from .sql import DBUser
from .types import User


class UserDatasource(
    DatabaseRepository[DBUser, User], graph_model=User, db_model=DBUser
):

    async def query_people(self) -> Optional[Sequence[User]]:
        return await self.get_models(true())

    async def query_person(self, id: UUID) -> Optional[User]:
        return await self.get_model(text("id = :id").bindparams(id=id))


class Context(BaseContext):
    users: UserDatasource

    def __init__(self, session_maker: async_sessionmaker):
        self.users = UserDatasource(session_maker)
