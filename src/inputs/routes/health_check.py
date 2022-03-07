from flask import Blueprint, jsonify
from requests.status_codes import codes

health_check = Blueprint("health-check", __name__)


@health_check.route("/healthcheck")
def health_check_view():
    # graph = Graph()
    # remote_conn = DriverRemoteConnection("wss://127.0.0.1:8182/gremlin", "g")

    # g = graph.traversal().withRemote(remote_conn)

    # # remote_conn.close()
    # result = g.V().has("name", "marko").out("knows").values("name")

    # if remote_conn.close():
    #     return (
    #         jsonify(message="Healthcheck failed", status=codes.internal_server_error),
    #         codes.internal_server_error,
    #     )

    # print(str(result))
    return jsonify(message="UP", status=codes.ok), codes.ok
