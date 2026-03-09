from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .user import User
    from .category import Category
    from .shop_product import ShopProduct
    from .restock_request import RestockRequest
    from .expiry_batch import ExpiryBatch
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin


class Shop(TimestampMixin, Base):
    __tablename__ = "shops"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    location: Mapped[str | None] = mapped_column(String(255))

    users: Mapped[list["User"]] = relationship(back_populates="shop")
    categories: Mapped[list["Category"]] = relationship(back_populates="shop")
    shop_products: Mapped[list["ShopProduct"]] = relationship(back_populates="shop")
    restock_requests: Mapped[list["RestockRequest"]] = relationship(back_populates="shop")
    expiry_batches: Mapped[list["ExpiryBatch"]] = relationship(back_populates="shop")