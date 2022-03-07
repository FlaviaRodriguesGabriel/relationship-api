from gremlin_python.driver.driver_remote_connection import DriverRemoteConnection
from gremlin_python.process.anonymous_traversal import traversal
from gremlin_python.process.graph_traversal import GraphTraversalSource


class GremlinServer:
    graph: GraphTraversalSource
    remote_conn: DriverRemoteConnection

    def __init__(self, url="ws://127.0.0.1:8182/gremlin") -> None:
        self.remote_conn = DriverRemoteConnection(url)

    def connect(self) -> GraphTraversalSource:
        self.graph: GraphTraversalSource = traversal().withRemote(self.remote_conn)
        return self.graph
