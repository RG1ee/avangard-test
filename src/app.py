from src.settings import create_app, jwt
from src.settings.config import settings
from src.apps.users.api.routing import api_user
from src.apps.confidential_data.api.routing import api_data


app = create_app()


@jwt.invalid_token_loader
def invalid_token_callback():
    return (
        {"description": "Signature verification failed!", "error": "invalid_token"},
        401,
    )


@jwt.unauthorized_loader
def unauthorized_loader_callback():
    return (
        {"description": "Access token not found!", "error": "unauthorized_loader"},
        401,
    )


app.register_blueprint(api_user)
app.register_blueprint(api_data)


def main():
    app.run(debug=settings.DUBUG)


if __name__ == "__main__":
    main()
