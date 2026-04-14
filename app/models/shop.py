from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.expiry_batch import ExpiryBatch
    from app.models.promo_item import PromoItem
    from app.models.restock_request import RestockRequest
    from app.models.shop_product import ShopProduct
    from app.models.user import User


class Shop(TimestampMixin, Base):
    __tablename__ = "shops"

    id: Mapped[int] = mapped_column(primary_key=True)
    shop_code: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    siret: Mapped[str | None] = mapped_column(String(20), unique=True, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    users: Mapped[list[User]] = relationship(back_populates="shop")
    categories: Mapped[list[Category]] = relationship(back_populates="shop")
    shop_products: Mapped[list[ShopProduct]] = relationship(back_populates="shop")
    restock_requests: Mapped[list[RestockRequest]] = relationship(back_populates="shop")
    expiry_batches: Mapped[list[ExpiryBatch]] = relationship(back_populates="shop")
    promo_items: Mapped[list[PromoItem]] = relationship(back_populates="shop")