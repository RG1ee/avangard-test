from flask import Blueprint
from flask_restful import Api

from src.apps.users.api.resources import AuthResource, UserRegistrationResource


api_user = Blueprint("user", __name__)
api = Api(api_user, prefix="/api/v1/users")

api.add_resource(
    UserRegistrationResource, "/registration", endpoint="users-registration"
)
api.add_resource(AuthResource, "/login", endpoint="users-login")
