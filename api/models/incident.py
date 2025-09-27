from datetime import datetime

from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class Incident(Base):
    __tablename__ = "incident"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id", ondelete="CASCADE"))
    source: Mapped[str] = mapped_column(String(32))  # edgesight|rainlane|manual
    sku: Mapped[str] = mapped_column(String(100), default="")
    image_url: Mapped[str] = mapped_column(String(255), default="")
    log_url: Mapped[str] = mapped_column(String(255), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    severity: Mapped[str] = mapped_column(String(16), default="info")

