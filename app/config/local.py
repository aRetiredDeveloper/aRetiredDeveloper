from .base_config import Config


class LocalDevelopmentConfig(Config):
    def __init__(self):
        Config.__init__(self)

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:joydeep@localhost:5432/url_shorter"