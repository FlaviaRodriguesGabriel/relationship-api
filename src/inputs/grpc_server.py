from concurrent import futures

import grpc
from gremlin_python.process.graph_traversal import GraphTraversalSource

from services import PartnershipService
from stubs import relationship_pb2_grpc


class GrpcServer:
    def start(self, graph: GraphTraversalSource, port="50051", max_workers=10) -> None:
        threads = futures.ThreadPoolExecutor(max_workers=max_workers)
        server = grpc.server(threads)

        relationship_pb2_grpc.add_PartnershipServiceServicer_to_server(
            servicer=PartnershipService(graph), server=server
        )
        server.add_insecure_port(f"[::]:{port}")

        server.start()
        print("GRPC server successfully initialized!")
        server.wait_for_termination()
