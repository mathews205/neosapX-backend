from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .shop import Shop
    from .restock_request import RestockRequest
from sqlalchemy import Enum, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin
from app.models.enums import UserRole
from app.models.enums import UserRole, user_role_enum


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    role: Mapped[UserRole] = mapped_column(user_role_enum, nullable=False)

    shop_id: Mapped[int] = mapped_column(ForeignKey("shops.id"))

    shop: Mapped["Shop"] = relationship(back_populates="users")
    created_restock_requests: Mapped[list["RestockRequest"]] = relationship(
        back_populates="created_by_user"
    )