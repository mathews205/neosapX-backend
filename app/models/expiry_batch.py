from __future__ import annotations

from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Index, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from app.models.product import Product
    from app.models.shop import Shop


class ExpiryBatch(TimestampMixin, Base):
    __tablename__ = "expiry_batches"

    __table_args__ = (
        Index("ix_expiry_batches_shop_id_expiry_date", "shop_id", "expiry_date"),
        Index("ix_expiry_batches_shop_id_product_id", "shop_id", "product_id"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    shop_id: Mapped[int] = mapped_column(ForeignKey("shops.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))
    quantity: Mapped[int] = mapped_column(Integer)
    expiry_date: Mapped[date] = mapped_column(Date)

    shop: Mapped[Shop] = relationship(back_populates="expiry_batches")
    product: Mapped[Product] = relationship(back_populates="expiry_batches")