from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Index, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from app.models.product import Product
    from app.models.promo_item import PromoItem
    from app.models.shop import Shop


class ExpiryBatch(TimestampMixin, Base):
    __tablename__ = "expiry_batches"

    __table_args__ = (
        Index("ix_expiry_batches_shop_active_expiry", "shop_id", "is_active", "expiry_date"),
        Index("ix_expiry_batches_shop_product_active", "shop_id", "product_id", "is_active"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    shop_id: Mapped[int] = mapped_column(ForeignKey("shops.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)

    expiry_date: Mapped[date] = mapped_column(Date, nullable=False)
    alert_days: Mapped[int] = mapped_column(Integer, default=3, nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    finished_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    shop: Mapped[Shop] = relationship(back_populates="expiry_batches")
    product: Mapped[Product] = relationship(back_populates="expiry_batches")
    promo_items: Mapped[list[PromoItem]] = relationship(back_populates="expiry_batch")