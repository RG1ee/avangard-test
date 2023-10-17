from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.settings.config_database import Base


class ConfidentialData(Base):
    __tablename__ = "confidential_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    data: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    def __str__(self) -> str:
        return f"{self.id}"
