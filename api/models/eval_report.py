from datetime import datetime

from sqlalchemy import String, Integer, ForeignKey, DateTime, Float
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class EvalReport(Base):
    __tablename__ = "eval_report"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    model_version_id: Mapped[int] = mapped_column(ForeignKey("model_version.id", ondelete="SET NULL"))
    url: Mapped[str] = mapped_column(String(255))
    map: Mapped[float | None] = mapped_column(Float, nullable=True)
    iou: Mapped[float | None] = mapped_column(Float, nullable=True)
    idf1: Mapped[float | None] = mapped_column(Float, nullable=True)
    latency_ms: Mapped[float | None] = mapped_column(Float, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)

