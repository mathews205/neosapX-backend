from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from app.models.expiry_batch import ExpiryBatch
    from app.models.product import Product
    from app.models.shop import Shop
    from app.models.user import User


class PromoItem(TimestampMixin, Base):
    __tablename__ = "promo_items"

    __table_args__ = (
        Index("ix_promo_items_shop_active", "shop_id", "is_active"),
        Index("ix_promo_items_batch", "expiry_batch_id"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    shop_id: Mapped[int] = mapped_column(ForeignKey("shops.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    expiry_batch_id: Mapped[int] = mapped_column(ForeignKey("expiry_batches.id"), nullable=False)
    added_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    shop: Mapped[Shop] = relationship(back_populates="promo_items")
    product: Mapped[Product] = relationship(back_populates="promo_items")
    expiry_batch: Mapped[ExpiryBatch] = relationship(back_populates="promo_items")
    added_by_user: Mapped[User | None] = relationship(back_populates="promo_items")