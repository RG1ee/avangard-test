from src.settings import create_app
from src.settings.config import settings


app = create_app()


def main():
    app.run(debug=settings.DUBUG)


if __name__ == "__main__":
    main()
