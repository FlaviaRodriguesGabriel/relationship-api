"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
https://sobolevn.me/2017/04/managing-djangos-settings
To change settings file:
`ENVIRONMENT=production python manage.py runserver`
"""

from os import environ

import django_stubs_ext

from .exceptions import UnkownEnvironment

# Monkeypatching Django, so stubs will work for all generics,
# see: https://github.com/typeddjango/django-stubs
django_stubs_ext.monkeypatch()


from inputs.http_server.settings.components.caches import *  # noqa: F401, F403
from inputs.http_server.settings.components.common import *  # noqa: F401, F403
from inputs.http_server.settings.components.db import *  # noqa: F401, F403
from inputs.http_server.settings.components.logging import *  # noqa: F401, F403

environ.setdefault("ENVIRONMENT", "local")
_ENVIRONMENT = environ["ENVIRONMENT"]

if _ENVIRONMENT == "production":
    from inputs.http_server.settings.environments.production import *
elif _ENVIRONMENT == "homolog":
    from inputs.http_server.settings.environments.homolog import *
elif _ENVIRONMENT == "development":
    from inputs.http_server.settings.environments.development import *
elif _ENVIRONMENT == "test":
    from inputs.http_server.settings.environments.test import *
elif _ENVIRONMENT == "local":
    from inputs.http_server.settings.environments.local import *
else:
    raise UnkownEnvironment
