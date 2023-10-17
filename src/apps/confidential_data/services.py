from src.apps.base.services import BaseService
from src.apps.confidential_data.models import ConfidentialData
from src.settings.config_database import Session


class ConfidentialDataService(BaseService):
    model = ConfidentialData

    @classmethod
    def get_one(cls, **filters):
        """
        Retrieve a single confidential data record that matches the specified filters.

        Args:
            **filters: Keyword arguments that specify the filters for the query.

        Returns:
            ConfidentialData: The first confidential data record that matches the filters.
        """
        with Session() as session:
            return session.query(cls.model).filter_by(**filters).first()

    @classmethod
    def delete_one(cls, confidential_data):
        """
        Delete a single confidential data record.

        Args:
            data (ConfidentialData): The confidential data record to delete.
        """
        with Session() as session:
            session.delete(confidential_data)
            session.commit()

    @classmethod
    def change_data(cls, confidential_data: ConfidentialData, name, data):
        """
        Update the name and data of a confidential data record.

        Args:
            confidential_data (ConfidentialData): The confidential data record to update.
            name (str): The new name for the data record.
            data (str): The new data for the data record.
        """
        with Session() as session:
            confidential_data.name = name
            confidential_data.data = data
            session.add(confidential_data)
            session.commit()

    @classmethod
    def get_all_by_user_id(cls, user_id):
        """
        Retrieve all confidential data records associated with a specific user.

        Args:
            user_id (int): The identifier of the user.

        Returns:
            List[ConfidentialData]: A list of confidential data records associated with the user.
        """
        with Session() as session:
            return session.query(cls.model).filter_by(user_id=user_id).all()
