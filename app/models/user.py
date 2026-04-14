from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, CheckConstraint, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin
from app.models.enums import UserRole, user_role_enum

if TYPE_CHECKING:
    from app.models.promo_item import PromoItem
    from app.models.restock_request import RestockRequest
    from app.models.shop import Shop
    from app.models.supplier import Supplier


class User(TimestampMixin, Base):
    __tablename__ = "users"

    __table_args__ = (
        CheckConstraint(
            "(shop_id IS NOT NULL AND supplier_id IS NULL) OR "
            "(shop_id IS NULL AND supplier_id IS NOT NULL)",
            name="ck_users_exactly_one_org",
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    phone_number: Mapped[str | None] = mapped_column(String(30), unique=True, nullable=True)
    role: Mapped[UserRole] = mapped_column(user_role_enum, nullable=False)

    shop_id: Mapped[int | None] = mapped_column(ForeignKey("shops.id"), nullable=True)
    supplier_id: Mapped[int | None] = mapped_column(ForeignKey("suppliers.id"), nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    shop: Mapped[Shop | None] = relationship(back_populates="users")
    supplier: Mapped[Supplier | None] = relationship(back_populates="users")
    created_restock_requests: Mapped[list[RestockRequest]] = relationship(
        back_populates="created_by_user"
    )
    promo_items: Mapped[list[PromoItem]] = relationship(back_populates="added_by_user")