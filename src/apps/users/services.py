from src.apps.base.services import BaseService
from src.apps.users.models import User


class UserService(BaseService):
    model = User
