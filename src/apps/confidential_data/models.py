import uuid

from sqlalchemy import UUID
from sqlalchemy.orm import Mapped, mapped_column

from src.settings.config_database import Base


class ConfidentialData(Base):
    __tablename__ = "confidential_data"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    name: Mapped[str]
    data: Mapped[str]

    def __str__(self) -> str:
        return f"{self.id}"
