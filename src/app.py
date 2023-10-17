from src.settings import create_app
from src.settings.config import settings
from src.apps.users.api.routing import api_user
from src.apps.confidential_data.api.routing import api_data


app = create_app()

app.register_blueprint(api_user)
app.register_blueprint(api_data)


def main():
    app.run(debug=settings.DUBUG)


if __name__ == "__main__":
    main()
