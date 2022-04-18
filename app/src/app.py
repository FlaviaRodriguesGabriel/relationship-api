from logging import getLogger

from interfaces import FlaskServer, GremlinServer, HttpServer
from settings import Settings

logger = getLogger(__name__)


class App:
    http_server: HttpServer
    gremlin_server: GremlinServer

    def __init__(self) -> None:
        self.http_server = FlaskServer(
            app_name=Settings.app_name,
            debug=Settings.debug,
            environment=Settings.environment,
            host="127.0.0.1",
            # prefix="v0",  # TODO: fica a dica
            port=Settings.http_port,
        )
        self.gremlin_server = GremlinServer()

    def start_server(self) -> None:
        self.gremlin_server.connect()
        self.http_server.run()

    def clear_graph(self) -> None:
        self.gremlin_server.clear_graph()
        logger.warning("Graph cleared!")
