from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class PO(Base):
    __tablename__ = "po"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id", ondelete="CASCADE"))
    body_json: Mapped[str] = mapped_column(String(2000), default="{}")

