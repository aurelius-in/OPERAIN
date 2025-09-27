from datetime import datetime

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    role: Mapped[str] = mapped_column(String(32), default="Operator")
    name: Mapped[str] = mapped_column(String(120), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

