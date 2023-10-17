from src.apps.base.services import BaseService
from src.apps.users.models import User
from src.settings.config_database import Session


class UserService(BaseService):
    model = User

    @classmethod
    def get_first_by_username(cls, username: str):
        with Session() as session:
            return session.query(User).filter_by(username=username).first()
