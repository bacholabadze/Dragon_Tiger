import os

from functools import lru_cache


class BaseConfig:
    MONGODB_URL: str = os.environ.get("MONGODB_URL", "mongodb://localhost:27017")
    MONGODB_DATABASE_NAME: str = os.environ.get("MONGODB_DATABASE_NAME", "dragondb")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    ALGORITHM = os.environ.get("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES")


class DevelopmentConfig(BaseConfig):
    pass


@lru_cache()
def get_settings():
    config_cls_dict = {
        "DEV": DevelopmentConfig,
    }

    config = os.environ.get("FASTAPI_CONFIG")
    return config_cls_dict.get(config)()


settings = get_settings()
