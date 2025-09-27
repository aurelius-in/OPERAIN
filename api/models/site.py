from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String, Integer
from api.models.base import Base


class Site(Base):
    __tablename__ = "site"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    timezone: Mapped[str] = mapped_column(String(64), nullable=False, default="UTC")

    projects = relationship("Project", back_populates="site")

