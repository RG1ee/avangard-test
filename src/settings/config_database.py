from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from src.settings.config import settings


engine = create_engine(settings.DATABASE_URI)
Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)


class Base(DeclarativeBase):
    """
    Base class used for declarative class definitions.
    """

    pass
