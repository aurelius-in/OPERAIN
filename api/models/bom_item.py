from sqlalchemy import String, Integer, ForeignKey, Numeric, Date
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class BomItem(Base):
    __tablename__ = "bom_item"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("project.id", ondelete="CASCADE"))
    sku: Mapped[str] = mapped_column(String(100), index=True)
    description: Mapped[str] = mapped_column(String(255), default="")
    qty: Mapped[int] = mapped_column(Integer, default=1)
    alt_sku: Mapped[str] = mapped_column(String(100), default="")
    eta: Mapped[Date | None] = mapped_column(Date, nullable=True)
    cost_monthly: Mapped[float | None] = mapped_column(Numeric(12, 2), nullable=True)

