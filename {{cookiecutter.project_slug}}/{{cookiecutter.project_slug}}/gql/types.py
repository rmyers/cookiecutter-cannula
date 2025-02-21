from __future__ import annotations
from abc import ABC
from cannula import ResolveInfo
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Protocol, Sequence, TYPE_CHECKING
from typing_extensions import TypedDict
from uuid import UUID

if TYPE_CHECKING:
    from .context import Context


@dataclass(kw_only=True)
class User(ABC):
    __typename = "User"
    id: UUID
    name: str
    email: str
    created_at: datetime


class peopleQuery(Protocol):

    async def __call__(
        self, info: ResolveInfo["Context"]
    ) -> Optional[Sequence[User]]: ...


class personQuery(Protocol):

    async def __call__(
        self, info: ResolveInfo["Context"], id: UUID
    ) -> Optional[User]: ...


class RootType(TypedDict, total=False):
    people: Optional[peopleQuery]
    person: Optional[personQuery]
