from flask import request
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash

from src.apps.users.services import UserService
from src.apps.users.api.schemas import UserSchema


class UserRegistrationResource(Resource):
    def post(self):
        data = request.get_json()
        schema = UserSchema()
        errors = schema.validate(data)
        if errors:
            return {"Errors": errors}, 400

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
        data = request.get_json()
        schema = UserSchema()
        errors = schema.validate(data)
        if errors:
            return {"Errors": errors}, 400

        user = UserService.get_one_or_none(
            username=data["username"],
        )
        if user is None:
            return {"username": "Invalid username"}, 400

        if not check_password_hash(user.hashed_password, data["password"]):
            return {"password": "Invalid password"}, 400

        access_token = create_access_token(identity=data["username"])
        return {"access": access_token}, 200
