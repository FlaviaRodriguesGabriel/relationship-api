from logging import getLogger

from inputs.http_server import Django

# from inputs import GrpcServer
from outputs import GremlinServer

# from gremlin_python.process.graph_traversal import GraphTraversalSource


logger = getLogger(__name__)


class App:
    # http_server: Flask
    http_server: Django
    # grpc_server: GrpcServer
    gremlin_server: GremlinServer

    clear_on_startup: bool

    def __init__(self, clear_on_startup: bool = False) -> None:
        # self.http_server = Flask(__name__)
        # self.http_server.register_blueprint(health_check)
        self.http_server = Django()
        # self.grpc_server = GrpcServer()
        self.gremlin_server = GremlinServer()  # TODO: move this to Django settings
        self.clear_on_startup = clear_on_startup

    def start_server(self) -> None:
        graph_db = self.gremlin_server.connect()
        if self.clear_on_startup:
            self.clear_graph()

        # self.grpc_server.start(graph)
        # self.http_server.run(threaded=True, host="0.0.0.0", port=5000)

        print(f"{self.http_server=}")
        print(f"{id(self.gremlin_server)=}")
        self.http_server.run()

    def clear_graph(self) -> None:
        self.gremlin_server.clear_graph()
        logger.warning("Graph cleared!")
