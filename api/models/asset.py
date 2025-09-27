from datetime import datetime

from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class Asset(Base):
    __tablename__ = "asset"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id", ondelete="CASCADE"))
    type: Mapped[str] = mapped_column(String(16))  # edge|camera
    serial: Mapped[str] = mapped_column(String(120), index=True)
    mac: Mapped[str] = mapped_column(String(64), default="")
    model: Mapped[str] = mapped_column(String(120), default="")
    location: Mapped[str] = mapped_column(String(200), default="")
    status: Mapped[str] = mapped_column(String(50), default="new")
    provisioned_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

