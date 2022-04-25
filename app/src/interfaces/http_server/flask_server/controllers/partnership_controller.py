__all__ = [
    "partnership_blueprint",
]

from typing import Tuple, Type, Union
from uuid import UUID

from flask import Blueprint, Response, jsonify, request
from requests.status_codes import codes

from interfaces.gremlin_server import GremlinServer
from interfaces.http_server.flask_server.exceptions import InvalidUsage
from models import inputs
from services import PartnershipService

partnership_blueprint = Blueprint(
    name="inquilinos",
    url_prefix="/dados_cadastrais/v1/inquilinos",
    import_name=__name__,
)


@partnership_blueprint.route(
    "/<uuid:id_inquilino>/clientes/<uuid:id_cliente>/socios", methods=["POST"]
)
def socios_view(id_inquilino: UUID, id_cliente: UUID) -> Tuple[Response, int]:
    gremlin_server = GremlinServer()
    partnership_service = PartnershipService(graph=gremlin_server.graph_db)

    data = request.json or {}
    partnership = inputs.Partnership.parse_obj(data)

    # TODO: retrieve/validate tenant_id related to the journey_id in Redis
    partnership_created = partnership_service.create_from_model(
        partnership=partnership,
        tenant_id=id_inquilino,
        client_id=id_cliente,
    )
    return (
        jsonify(**partnership_created.dict()),
        codes.created,
    )


@partnership_blueprint.errorhandler(InvalidUsage)
def handle_invalid_usage(
    code_or_exception: Union[Type[Exception], int]
) -> Tuple[Response, int]:
    try:
        response_content = code_or_exception.to_dict()  # type: ignore[union-attr]
    except Exception:
        try:
            response_content = {
                "error": dict(code_or_exception)  # type: ignore[call-overload]
            }
        except Exception:
            response_content = {"error": str(code_or_exception)}

    return (
        jsonify(**response_content),
        getattr(code_or_exception, "status_code", codes.internal_server_error),
    )
