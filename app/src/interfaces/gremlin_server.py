from aiohttp.client_exceptions import ClientConnectionError
from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.graph_traversal import GraphTraversalSource

from utils.singleton import SingletonMeta


class GremlinServer(metaclass=SingletonMeta):
    graph_db: GraphTraversalSource
    remote_conn: DriverRemoteConnection

    def __init__(self, url="ws://127.0.0.1:8182/gremlin") -> None:
        self.remote_conn = DriverRemoteConnection(url)

    def clear_graph(self) -> None:
        if not self.is_connected:
            self.connect()

        self.graph_db.V().drop().iterate()

    def connect(self) -> GraphTraversalSource:
        self.graph_db: GraphTraversalSource = traversal().withRemote(self.remote_conn)
        return self.graph_db

    @property
    def is_connected(self) -> bool:
        if not hasattr(self, "graph_db"):
            return False

        try:
            self.graph_db.V().iterate()
        except ClientConnectionError:
            return False

        return True
