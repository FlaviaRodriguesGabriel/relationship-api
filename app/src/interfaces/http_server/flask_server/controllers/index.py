from typing import Tuple

from flask import Blueprint, Response, jsonify
from requests.status_codes import codes

from settings import Settings

index = Blueprint("index", __name__)


@index.route("/")
def index_view() -> Tuple[Response, int]:
    return (
        jsonify(
            app_name=Settings.app_name,
            version=Settings.version,
            environment=Settings.environment,
        ),
        codes.ok,
    )
