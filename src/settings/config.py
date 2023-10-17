import os

from functools import lru_cache

from dotenv import load_dotenv


load_dotenv()


class Settings:
    """
    A class for storing application settings.

    Attributes:
        DEBUG (bool): Debug flag.
        By default, it is set to True,
        if not definitely

        DATABASE_URL (str): URI for connecting to the database.
        If the DATABASE_URL environment variable is not set,
        the default value is used.
    """

    DUBUG: bool = bool(os.getenv("DEBUG", default=True))
    DATABASE_URI = os.getenv(
        "DATABASE_URI",
        default="postgresql://postgres:postgres@127.0.0.1:5432/postgres",
    )


@lru_cache()
def get_settings():
    """
    Function for getting the application settings object.

    Returns an instance of the Settings class that contains the configuration
    settings for the application, including DEBUG and DATABASE_URL.

    Returns:
        Settings: An instance of the Settings class with configuration settings.
    """

    return Settings


settings = get_settings()
