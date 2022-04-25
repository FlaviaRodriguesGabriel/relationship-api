__all__ = [
    "health_check_blueprint",
]

from typing import Dict, Tuple

from flask import Blueprint, Response, jsonify
from requests.status_codes import codes

from interfaces.gremlin_server import GremlinServer

health_check_blueprint = Blueprint(
    name="health-check",
    url_prefix="/healthcheck",
    import_name=__name__,
)


@health_check_blueprint.route("/")
def health_check_all() -> Tuple[Response, int]:
    disk_status = get_disk_status()
    db_status = get_db_status()

    statuses = {
        **disk_status,
        **db_status,
    }
    status_code = get_status_code_for_all_values(statuses)

    return (
        jsonify(**translate_status_data(statuses)),
        status_code,
    )


@health_check_blueprint.route("/db")
def health_check_db() -> Tuple[Response, int]:
    db_status = get_db_status()
    status_code = get_status_code_for_all_values(db_status)

    return (
        jsonify(**translate_status_data(db_status)),
        status_code,
    )


@health_check_blueprint.route("/disk")
def health_check_disk() -> Tuple[Response, int]:
    disk_status = get_disk_status()
    status_code = get_status_code_for_all_values(disk_status)

    return (
        jsonify(**translate_status_data(disk_status)),
        status_code,
    )


def get_status_code_for_all_values(statuses: Dict[str, bool]) -> int:
    return codes.ok if all(statuses.values()) else codes.internal_server_error


def get_db_status() -> Dict[str, bool]:
    gremlin = GremlinServer()
    return {"db_status": gremlin.is_connected}


def get_disk_status() -> Dict[str, bool]:
    return {"disk_status": True}  # TODO: implement this dummy status check


def translate_status_data(statuses: Dict[str, bool]) -> Dict[str, str]:
    statuses_up_down = {}
    for key, value in statuses.items():
        statuses_up_down[key] = "UP" if value else "DOWN"
    return statuses_up_down
