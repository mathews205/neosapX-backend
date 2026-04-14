from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Index, Integer, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.config import settings
from app.models.base import Base, TimestampMixin
from app.models.enums import RestockRequestStatus, restock_request_status_enum

if TYPE_CHECKING:
    from app.models.product import Product
    from app.models.shop import Shop
    from app.models.supplier import Supplier
    from app.models.user import User


class RestockRequest(TimestampMixin, Base):
    __tablename__ = "restock_requests"

    __table_args__ = (
        Index("ix_restock_requests_shop_id_status", "shop_id", "status"),
        Index(
            "uq_pending_restock_per_shop_product",
            "shop_id",
            "product_id",
            unique=True,
            postgresql_where=text(
                f"status = 'pending'::{settings.DB_SCHEMA}.restock_request_status_enum"
            ),
        ),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    shop_id: Mapped[int] = mapped_column(ForeignKey("shops.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    supplier_id: Mapped[int | None] = mapped_column(ForeignKey("suppliers.id"), nullable=True)
    created_by_user_id: Mapped[int | None] = mapped_column(ForeignKey("users.id"), nullable=True)
    requested_quantity: Mapped[int | None] = mapped_column(Integer, nullable=True)

    status: Mapped[RestockRequestStatus] = mapped_column(
        restock_request_status_enum,
        default=RestockRequestStatus.PENDING,
        nullable=False,
    )

    shop: Mapped[Shop] = relationship(back_populates="restock_requests")
    product: Mapped[Product] = relationship(back_populates="restock_requests")
    supplier: Mapped[Supplier | None] = relationship()
    created_by_user: Mapped[User | None] = relationship(back_populates="created_restock_requests")