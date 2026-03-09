from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .supplier import Supplier
    from .shop_product import ShopProduct
    from .restock_request import RestockRequest
    from .expiry_batch import ExpiryBatch

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Product(TimestampMixin, Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(150),
        index=True,
        nullable=False
    )

    sku: Mapped[str | None] = mapped_column(
        String(100),
        unique=True
    )

    barcode: Mapped[str | None] = mapped_column(
        String(100),
        unique=True,
        index=True,
        nullable=True
    )

    image_url: Mapped[str | None] = mapped_column(String(500))

    unit: Mapped[str | None] = mapped_column(String(50))

    supplier_id: Mapped[int | None] = mapped_column(
        ForeignKey("suppliers.id"),
        index=True
    )

    supplier: Mapped["Supplier"] = relationship(back_populates="products")

    shop_products: Mapped[list["ShopProduct"]] = relationship(
        back_populates="product"
    )

    restock_requests: Mapped[list["RestockRequest"]] = relationship(
        back_populates="product"
    )

    expiry_batches: Mapped[list["ExpiryBatch"]] = relationship(
        back_populates="product"
    )