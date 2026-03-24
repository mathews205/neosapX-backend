from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from app.models.expiry_batch import ExpiryBatch
    from app.models.promo_item import PromoItem
    from app.models.restock_request import RestockRequest
    from app.models.shop_product import ShopProduct
    from app.models.supplier import Supplier


class Product(TimestampMixin, Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(150),
        index=True,
        nullable=False,
    )

    sku: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        nullable=True,
    )

    barcode: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        index=True,
        nullable=True,
    )

    image_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    unit: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    global_category: Mapped[str | None] = mapped_column(
        String(100),
        index=True,
        nullable=True,
    )

    supplier_id: Mapped[int | None] = mapped_column(
        ForeignKey("suppliers.id"),
        index=True,
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    supplier: Mapped[Supplier | None] = relationship(back_populates="products")
    shop_products: Mapped[list[ShopProduct]] = relationship(back_populates="product")
    restock_requests: Mapped[list[RestockRequest]] = relationship(back_populates="product")
    expiry_batches: Mapped[list[ExpiryBatch]] = relationship(back_populates="product")
    promo_items: Mapped[list[PromoItem]] = relationship(back_populates="product")