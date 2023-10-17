from marshmallow import fields

from src.settings import ma
from src.apps.users.models import User


class UserSchema(ma.Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)

    class Meta:
        model = User
        fields = ("id", "username", "password")
