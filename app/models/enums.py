import enum

from sqlalchemy import Enum as SqlEnum

from app.core.config import settings


class UserRole(str, enum.Enum):
    OWNER = "owner"
    EMPLOYEE = "employee"


class RestockRequestStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    FULFILLED = "fulfilled"
    CANCELLED = "cancelled"


user_role_enum = SqlEnum(
    UserRole,
    name="user_role_enum",
    schema=settings.DB_SCHEMA,
    create_type=True,
    values_callable=lambda enum_cls: [e.value for e in enum_cls],
)

restock_request_status_enum = SqlEnum(
    RestockRequestStatus,
    name="restock_request_status_enum",
    schema=settings.DB_SCHEMA,
    create_type=True,
    values_callable=lambda enum_cls: [e.value for e in enum_cls],
)