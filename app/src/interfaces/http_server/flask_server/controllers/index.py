from typing import Tuple
from uuid import UUID

from flask import Blueprint, Response, jsonify, request
from requests.status_codes import codes

from interfaces.http_server.flask_server.exceptions import InvalidUsage
from models import inputs

# from services import PartnershipService
from settings import Settings

index = Blueprint("index", __name__)
# partnership_service = PartnershipService()


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


@index.route("/inquilinos/<uuid:id_inquilino>/socios", methods=["POST"])
def socios_view(id_inquilino: UUID) -> Tuple[Response, int]:

    data = request.json or {}

    partnership = inputs.Partnership(id_inquilino=id_inquilino, **data)

    # partnership_created = partnership_service.create(partnership)

    # return (
    #     jsonify(**partnership_created.dict()),
    #     codes.created,
    # )
    return (
        jsonify(**partnership.dict(by_alias=True)),
        codes.created,
    )


@index.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
