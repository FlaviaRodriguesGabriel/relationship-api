from typing import Dict, Tuple

from flask import Blueprint, Response, jsonify
from requests.status_codes import codes

from interfaces.gremlin_server import GremlinServer

health_check = Blueprint("health-check", __name__, url_prefix="/healthcheck")


@health_check.route("/")
def health_check_all() -> Tuple[Response, int]:
    disk_status = get_disk_status()
    gremlin_status = get_gremlin_status()

    statuses = {
        **disk_status,
        **gremlin_status,
    }
    status_code = get_status_code_for_all_values(statuses)

    return (
        jsonify(**translate_status_data(statuses)),
        status_code,
    )


@health_check.route("/disk")
def health_check_disk() -> Tuple[Response, int]:
    disk_status = get_disk_status()
    status_code = get_status_code_for_all_values(disk_status)

    return (
        jsonify(**translate_status_data(disk_status)),
        status_code,
    )


@health_check.route("/gremlin")
def health_check_gremlin() -> Tuple[Response, int]:
    gremlin_status = get_gremlin_status()
    status_code = get_status_code_for_all_values(gremlin_status)

    return (
        jsonify(**translate_status_data(gremlin_status)),
        status_code,
    )


def get_status_code_for_all_values(statuses: Dict[str, bool]) -> int:
    return codes.ok if all(statuses.values()) else codes.internal_server_error


def get_disk_status() -> Dict[str, bool]:
    return {"disk_status": True}  # TODO: implement this dummy status check


def get_gremlin_status() -> Dict[str, bool]:
    gremlin = GremlinServer()
    return {"gremlin_status": gremlin.is_connected}


def translate_status_data(statuses: Dict[str, bool]) -> Dict[str, str]:
    statuses_up_down = {}
    for key, value in statuses.items():
        statuses_up_down[key] = "UP" if value else "DOWN"
    return statuses_up_down
