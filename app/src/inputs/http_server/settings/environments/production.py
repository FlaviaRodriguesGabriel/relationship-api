"""
This file contains all the settings used in production.
This file is required and if development.py is present these
values are overridden.
"""

from inputs.http_server.settings import config

# Production flags:
# https://docs.djangoproject.com/en/4.0/howto/deployment/

ENVIRONMENT = "production"

DEBUG = False

ALLOWED_HOSTS = [
    # # TODO: check production hosts
    # config("DOMAIN_NAME"),
    # # We need this value for `healthcheck` to work:
    # "localhost",
]


# Security
# https://docs.djangoproject.com/en/4.0/topics/security/

SECURE_HSTS_SECONDS = 31536000  # the same as Caddy has
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT = True
SECURE_REDIRECT_EXEMPT = [
    # This is required for healthcheck to work:
    "^health/",
]

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
