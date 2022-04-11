"""
This file contains all the settings that defines the development server.
SECURITY WARNING: don't run with debug turned on in production!
"""

# from inputs.http_server.settings.components.common import INSTALLED_APPS, MIDDLEWARE
from inputs.http_server.settings import config

ENVIRONMENT = "development"

DEBUG = True

ALLOWED_HOSTS = [
    # config("DOMAIN_NAME"),
    # "localhost",
    # "0.0.0.0",  # noqa: S104  # nosec
    # "127.0.0.1",
    # "[::1]",
]


# INSTALLED_APPS += (
# )

# MIDDLEWARE += (
# )
