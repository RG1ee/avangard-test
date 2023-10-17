from src.apps.base.services import BaseService
from src.apps.confidential_data.models import ConfidentialData
from src.settings.config_database import Session


class ConfidentialDataService(BaseService):
    model = ConfidentialData

    @classmethod
    def get_one(cls, **filters):
        with Session() as session:
            return session.query(cls.model).filter_by(**filters).first()

    @classmethod
    def delete_one(cls, data):
        with Session() as session:
            session.delete(data)
            session.commit()

    @classmethod
    def change_data(cls, confidential_data: ConfidentialData, name, data):
        with Session() as session:
            confidential_data.name = name
            confidential_data.data = data
            session.add(confidential_data)
            session.commit()
