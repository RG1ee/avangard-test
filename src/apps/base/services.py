from src.settings.config_database import Session


class BaseService:
    """
    Base service for working with a database
    """

    model = None

    @classmethod
    def insert_data(cls, **data):
        """
        Method for creating a record in the database
        """
        with Session() as session:
            stmt = cls.model(**data)
            session.add(stmt)
            session.commit()

    @classmethod
    def get_one_or_none(cls, **filters):
        with Session() as session:
            return session.query(cls.model).filter_by(**filters).one_or_none()

    @classmethod
    def get_all(cls):
        with Session() as session:
            return session.query(cls.model).all()
