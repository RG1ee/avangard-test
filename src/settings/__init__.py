from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from src.settings.config import settings
from src.settings.config_database import Base


db = SQLAlchemy(model_class=Base)
migrate = Migrate(directory="src/migrations")


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
    db.init_app(app)
    migrate.init_app(app, db)

    return app
