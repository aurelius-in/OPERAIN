from datetime import date

from sqlalchemy import String, Integer, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class Capa(Base):
    __tablename__ = "capa"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    incident_id: Mapped[int] = mapped_column(ForeignKey("incident.id", ondelete="CASCADE"))
    owner: Mapped[str] = mapped_column(String(120), default="")
    root_cause: Mapped[str] = mapped_column(String(255), default="")
    due_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    status: Mapped[str] = mapped_column(String(32), default="open")
    verification_note: Mapped[str] = mapped_column(String(255), default="")

