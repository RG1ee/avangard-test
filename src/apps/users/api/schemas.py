from src.settings import ma
from src.apps.users.models import User


class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ("id", "username", "password")
