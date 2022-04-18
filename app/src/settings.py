from os import environ

from utils.singleton import SingletonMeta


class Settings(metaclass=SingletonMeta):
    app_name: str = environ.get("APP_NAME") or "relationship-api"
    debug: bool = bool(environ.get("DEBUG") or "False")
    environment: str = environ.get("ENVIRONMENT") or "undefined"
    version: str = environ.get("VERSION") or "0"

    http_port: int = int(environ.get("HTTP_PORT") or "8081")
    # http_workers: int = int(environ.get("HTTP_WORKERS") or "1")