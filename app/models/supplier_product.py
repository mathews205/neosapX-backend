from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from app.models.product import Product
    from app.models.supplier import Supplier


class SupplierProduct(TimestampMixin, Base):
    __tablename__ = "supplier_products"

    __table_args__ = (
        UniqueConstraint("supplier_id", "product_id", name="unique_supplier_product"),
        Index("ix_supplier_products_supplier_default", "supplier_id", "is_default"),
        Index("ix_supplier_products_product_id", "product_id"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    supplier_id: Mapped[int] = mapped_column(ForeignKey("suppliers.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    is_default: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    supplier: Mapped[Supplier] = relationship(back_populates="supplier_products")
    product: Mapped[Product] = relationship(back_populates="supplier_products")