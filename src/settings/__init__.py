from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

from src.settings.config import settings
from src.settings.config_database import Base


db = SQLAlchemy(model_class=Base)
migrate = Migrate(directory="src/migrations")
jwt = JWTManager()
ma = Marshmallow()


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return ({"description": "Token has expired!", "error": "token_expired"}, 401)


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        {"description": "Signature verification failed!", "error": "invalid_token"},
        401,
    )


@jwt.unauthorized_loader
def unauthorized_loader_callback(error):
    return (
        {"description": "Access token not found!", "error": "unauthorized_loader"},
        401,
    )


def create_app():
    """
    Creates an instance of a Flask application
    with settings and a connection to the database.

    Returns:
        Flask: An instance of a Flask application with settings and a database connection.

    Usage example:
        app = create_app()
        app.run(debug=True)
    """

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = settings.DATABASE_URI
    app.config["JWT_SECRET_KEY"] = settings.SECRET_KEY
    app.config["PROPAGATE_EXCEPTIONS"] = True

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    ma.init_app(app)

    return app
