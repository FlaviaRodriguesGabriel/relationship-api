from typing import Tuple

from flask import Blueprint, Response, jsonify, request
from requests.status_codes import codes

from interfaces.http_server.flask_server.exceptions import InvalidUsage
from models import inputs
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


@index.route("/socios", methods=["POST"])
def socios_view() -> Tuple[Response, int]:
    partnership = inputs.Partnership.parse_obj(request.json)

    ...  # TODO: insert `partnership` in DB

    return (
        jsonify(**partnership.dict()),
        codes.created,
    )


@index.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
