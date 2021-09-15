from .base_config import Config


class ProductionEnvrionmentConfig(Config):
    def __init__(self):
        Config.__init__(self)

    DEBUG = True

    @property
    def database_config(self):
        return "postgresql://postgres:joydeep@localhost:5432/url_shorter"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
