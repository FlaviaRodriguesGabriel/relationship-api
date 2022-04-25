__all__ = [
    "index_blueprint",
]

from typing import Tuple

from flask import Blueprint, Response, jsonify
from requests.status_codes import codes

from settings import Settings

index_blueprint = Blueprint(
    name="index",
    import_name=__name__,
)


@index_blueprint.route("/")
def index_view() -> Tuple[Response, int]:
    return (
        jsonify(
            app_name=Settings.app_name,
            version=Settings.version,
            environment=Settings.environment,
        ),
        codes.ok,
    )
