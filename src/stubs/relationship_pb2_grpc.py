# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import stubs.relationship_pb2 as relationship__pb2


class PartnershipServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddPartnership = channel.unary_unary(
            "/stubs.relationship.PartnershipService/AddPartnership",
            request_serializer=relationship__pb2.BusinessPartnershipMessage.SerializeToString,
            response_deserializer=relationship__pb2.BusinessPartnershipMessage.FromString,
        )
        self.GetPartnership = channel.unary_unary(
            "/stubs.relationship.PartnershipService/GetPartnership",
            request_serializer=relationship__pb2.BusinessPartnershipMessage.SerializeToString,
            response_deserializer=relationship__pb2.BusinessPartnershipMessage.FromString,
        )
        self.UpdatePartnership = channel.unary_unary(
            "/stubs.relationship.PartnershipService/UpdatePartnership",
            request_serializer=relationship__pb2.BusinessPartnershipMessage.SerializeToString,
            response_deserializer=relationship__pb2.BusinessPartnershipMessage.FromString,
        )
        self.DeletePartnership = channel.unary_unary(
            "/stubs.relationship.PartnershipService/DeletePartnership",
            request_serializer=relationship__pb2.BusinessPartnershipMessage.SerializeToString,
            response_deserializer=relationship__pb2.BusinessPartnershipMessage.FromString,
        )


class PartnershipServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddPartnership(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def GetPartnership(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def UpdatePartnership(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeletePartnership(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_PartnershipServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "AddPartnership": grpc.unary_unary_rpc_method_handler(
            servicer.AddPartnership,
            request_deserializer=relationship__pb2.BusinessPartnershipMessage.FromString,
            response_serializer=relationship__pb2.BusinessPartnershipMessage.SerializeToString,
        ),
        "GetPartnership": grpc.unary_unary_rpc_method_handler(
            servicer.GetPartnership,
            request_deserializer=relationship__pb2.BusinessPartnershipMessage.FromString,
            response_serializer=relationship__pb2.BusinessPartnershipMessage.SerializeToString,
        ),
        "UpdatePartnership": grpc.unary_unary_rpc_method_handler(
            servicer.UpdatePartnership,
            request_deserializer=relationship__pb2.BusinessPartnershipMessage.FromString,
            response_serializer=relationship__pb2.BusinessPartnershipMessage.SerializeToString,
        ),
        "DeletePartnership": grpc.unary_unary_rpc_method_handler(
            servicer.DeletePartnership,
            request_deserializer=relationship__pb2.BusinessPartnershipMessage.FromString,
            response_serializer=relationship__pb2.BusinessPartnershipMessage.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "stubs.relationship.PartnershipService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class PartnershipService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddPartnership(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/stubs.relationship.PartnershipService/AddPartnership",
            relationship__pb2.BusinessPartnershipMessage.SerializeToString,
            relationship__pb2.BusinessPartnershipMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def GetPartnership(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/stubs.relationship.PartnershipService/GetPartnership",
            relationship__pb2.BusinessPartnershipMessage.SerializeToString,
            relationship__pb2.BusinessPartnershipMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def UpdatePartnership(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/stubs.relationship.PartnershipService/UpdatePartnership",
            relationship__pb2.BusinessPartnershipMessage.SerializeToString,
            relationship__pb2.BusinessPartnershipMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def DeletePartnership(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/stubs.relationship.PartnershipService/DeletePartnership",
            relationship__pb2.BusinessPartnershipMessage.SerializeToString,
            relationship__pb2.BusinessPartnershipMessage.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
