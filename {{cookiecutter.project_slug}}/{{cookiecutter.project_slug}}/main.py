import datetime
import typing
import uuid

from cannula import ResolveInfo, CannulaApplication

from .gql.context import Context
from .gql.types import RootType, User


async def resolve_people(info: ResolveInfo[Context]) -> typing.Sequence[User] | None:
    return [
        User(
            id=uuid.uuid4(),
            name="frank",
            email="ted@foo.com",
            created_at=datetime.datetime.now(),
        )
    ]


# The RootType object generated in `gql/types.py` will warn us if we use
# a resolver with an incorrect signature
root_value: RootType = {
    "people": resolve_people,
}


app = CannulaApplication[RootType](
    root_value=root_value,
    context=Context,
)
