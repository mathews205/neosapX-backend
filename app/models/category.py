from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .shop import Shop
    from .shop_product import ShopProduct

from sqlalchemy import ForeignKey, Index, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Category(TimestampMixin, Base):
    __tablename__ = "categories"
    __table_args__ = (
        UniqueConstraint("shop_id", "name", name="unique_shop_category"),
        Index("ix_categories_shop_id_position", "shop_id", "position")
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    shop_id: Mapped[int] = mapped_column(ForeignKey("shops.id"))
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    position: Mapped[int | None] = mapped_column(Integer)

    shop: Mapped["Shop"] = relationship(back_populates="categories")
    shop_products: Mapped[list["ShopProduct"]] = relationship(back_populates="category")