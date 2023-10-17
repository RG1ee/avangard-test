from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.settings.config_database import Base


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True)
    hashed_password: Mapped[str]

    def __str__(self) -> str:
        return self.username
