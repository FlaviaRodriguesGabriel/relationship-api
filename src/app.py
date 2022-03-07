from flask import Flask
from loguru import logger

from inputs import GrpcServer
from inputs.routes import health_check
from outputs import GremlinServer


class App:
    http_server: Flask
    grpc_server: GrpcServer
    gremlin_server: GremlinServer

    clear_on_startup: bool

    def __init__(self, clear_on_startup=False) -> None:
        self.http_server = Flask(__name__)
        self.http_server.register_blueprint(health_check)
        self.grpc_server = GrpcServer()
        self.gremlin_server = GremlinServer()
        self.clear_on_startup = clear_on_startup

    def start_server(self) -> None:
        graph = self.gremlin_server.connect()
        if self.clear_on_startup:
            self.clear_graph()

        self.grpc_server.start(graph)
        # self.http_server.run(threaded=True, host="0.0.0.0", port=5000)

    def clear_graph(self) -> None:
        self.gremlin_server.graph.V().drop().iterate()
        logger.warning("Graph cleared!")
