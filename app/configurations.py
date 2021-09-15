from .config.production import ProductionEnvrionmentConfig
from .config.dev import DevEnvrionmentConfig
from .config.local import LocalDevelopmentConfig
from .config.base_config import Config

config_by_name = dict(
    dev=DevEnvrionmentConfig,
    prod=ProductionEnvrionmentConfig,
    local=LocalDevelopmentConfig
)

key = Config.SECRET_KEY
