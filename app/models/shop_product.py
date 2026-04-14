from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, ForeignKey, Index, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin

if TYPE_CHECKING:
    from app.models.category import Category
    from app.models.product import Product
    from app.models.shop import Shop


class ShopProduct(TimestampMixin, Base):
    __tablename__ = "shop_products"

    __table_args__ = (
        UniqueConstraint("shop_id", "product_id", name="unique_shop_product"),
        Index("ix_shop_products_shop_id_is_active", "shop_id", "is_active"),
        Index("ix_shop_products_shop_id_product_id", "shop_id", "product_id"),
        Index("ix_shop_products_shop_id_category_id", "shop_id", "category_id"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    shop_id: Mapped[int] = mapped_column(ForeignKey("shops.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    shop: Mapped[Shop] = relationship(back_populates="shop_products")
    product: Mapped[Product] = relationship(back_populates="shop_products")
    category: Mapped[Category | None] = relationship(back_populates="shop_products")