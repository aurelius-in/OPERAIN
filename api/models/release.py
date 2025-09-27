from datetime import datetime

from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class Release(Base):
    __tablename__ = "release"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id", ondelete="CASCADE"))
    model_version_id: Mapped[int] = mapped_column(ForeignKey("model_version.id", ondelete="SET NULL"))
    drifthawk_version: Mapped[str] = mapped_column(String(80), default="")
    result: Mapped[str] = mapped_column(String(32), default="pending")
    signed_receipt_url: Mapped[str] = mapped_column(String(255), default="")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

