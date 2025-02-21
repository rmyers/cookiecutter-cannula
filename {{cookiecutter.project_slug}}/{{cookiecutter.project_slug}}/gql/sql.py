from __future__ import annotations
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid import UUID


class Base(DeclarativeBase):
    pass


class DBUser(Base):
    __tablename__ = "users"
    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(index=True, unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(index=True, nullable=False)
