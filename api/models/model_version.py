from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from api.models.base import Base


class ModelVersion(Base):
    __tablename__ = "model_version"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(120))
    sha: Mapped[str] = mapped_column(String(80), index=True)
    registry_url: Mapped[str] = mapped_column(String(255))

