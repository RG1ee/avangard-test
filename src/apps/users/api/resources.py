from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from marshmallow import ValidationError
from werkzeug.security import check_password_hash, generate_password_hash

from src.apps.users.services import UserService
from src.apps.users.api.schemas import UserSchema
from src.apps.base.validations import validate_data


class UserRegistrationResource(Resource):
    def post(self):
        """
        Registers a new user.

        Expects input data in JSON format and validates it using UserSchema.
        If the data passes validation, it checks if a user with the same username already exists.
        If not, it inserts the user into the database and returns a success message.

        Returns:
            JSON object with a success message if registration is successful.

        HTTP Status Codes:
            - 200 OK: Successful registration.
            - 400 Bad Request: Input data validation error or a user with the same username already exists.
        """
        data = request.get_json()
        try:
            validate_data(UserSchema, data)
        except ValidationError as e:
            return e.messages_dict, 400

        user = UserService.get_one_or_none(username=data["username"])
        if user is not None:
            return {"message": "A user with this username exists"}, 400

        UserService.insert_data(
            username=data["username"],
            hashed_password=generate_password_hash(data["password"]),
        )

        return {"message": "Success"}, 200


class AuthResource(Resource):
    def post(self):
        """
        Authenticates a user.

        Expects input data in JSON format and validates it using UserSchema.
        If the data passes validation, it checks if a user with the provided username exists.
        If the user exists, it checks if the provided password matches the hashed password in the database.
        If authentication is successful, it returns an access token.

        Returns:
            JSON object with an access token if authentication is successful.

        HTTP Status Codes:
            - 200 OK: Successful authentication and an access token is provided.
            - 400 Bad Request: Input data validation error, an invalid username, or an invalid password.
        """
        data = request.get_json()
        try:
            validate_data(UserSchema, data)
        except ValidationError as e:
            return e.messages_dict, 400

        user = UserService.get_one_or_none(
            username=data["username"],
        )
        if user is None:
            return {"username": "Invalid username"}, 400

        if not check_password_hash(user.hashed_password, data["password"]):
            return {"password": "Invalid password"}, 400

        access_token = create_access_token(identity=data["username"])
        return {"access": access_token}, 200
