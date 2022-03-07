import grpc
from gremlin_python.process.graph_traversal import GraphTraversalSource
from grpc_argument_validator import validate_args
from loguru import logger

from stubs import relationship_pb2_grpc
from stubs.relationship_pb2 import BusinessPartnershipMessage
from utils import relationships_by_type
from validators import (
    CompanyMessageValidator,
    PartnerMessageValidator,
    RelationshipTypeValidator,
)


class PartnershipService(relationship_pb2_grpc.PartnershipServiceServicer):
    graph: GraphTraversalSource

    def __init__(self, graph: GraphTraversalSource, *args, **kwargs) -> None:
        self.graph = graph
        super().__init__(*args, **kwargs)

    @validate_args(
        non_default=[
            "relationship_type",
            "company_message.name",
            "partner_message.completeness.additional_information",
            "partner_message.name",
        ],
        validators={
            "relationship_type": RelationshipTypeValidator(),
        },
        optional_validators={
            "company_message": CompanyMessageValidator(),
            "partner_message[]": PartnerMessageValidator(),
        },
    )
    def AddPartnership(
        self, request: BusinessPartnershipMessage, context: grpc.ServicerContext
    ):
        if request.relationship_type not in relationships_by_type:
            context.abort(grpc.StatusCode.NOT_FOUND, "Relationship type not supported")

        # gremlin_connection_result = g.has('name', 'marko').out('knows').values('name')
        # self.graph.addV(request.company_message.company_id).property('name', request.company_message[vertices].name)

        company = (
            self.graph.addV(request.company_message.company_id)
            .property(
                "name",
                request.company_message.name,
                "person_type",
                request.company_message.person_type,
            )
            .next()
        )

        for partner_message in request.partner_message:
            q = self.graph.addV(partner_message.partner_id).property(
                "name",
                partner_message.name,
                "person_type",
                partner_message.person_type,
                "partner_id",
                partner_message.partner_id,
            )
            partner = q.next()

            self.graph.V(company).addE("has_partner").to(partner).property(
                "participation_percentage", 0.5
            ).iterate()
            # print(self.graph.has("name", partner_message.name))
            print("Added message!")

        # for vertices in [0, 1]:
        #     print("!--------------------------------------------!")
        #     # print(self.graph.has('name', request.partner_message[vertices].name))
        #     # print(self.graph.has('person_type', request.partner_message[vertices].person_type))
        #     print(
        #         self.graph.has(
        #             "partner_id",
        #             request.partner_message[vertices].partner_id,
        #             "name",
        #             request.partner_message[vertices].name,
        #         )
        #     )

        logger.info(request)
        return request

    @validate_args(
        non_default=[
            "relationship_type",
        ],
        validators={
            "relationship_type": RelationshipTypeValidator(),
        },
        optional_validators={
            # "company_message": CompanyMessageValidator(),
            # "partner_message[]": PartnerMessageValidator(),
        },
    )
    def GetPartnership(
        self, request: BusinessPartnershipMessage, context: grpc.ServicerContext
    ):
        if request.relationship_type not in relationships_by_type:
            context.abort(grpc.StatusCode.NOT_FOUND, "Relationship type not supported")

        try:
            partnership = (
                self.graph.V()
                .has("company_id", request.company_message.company_id)
                .out()
                .next()
            )
            print("!--------------------------------------------!")
            print(partnership)

            return partnership
        except StopIteration:
            context.abort(grpc.StatusCode.NOT_FOUND, "Company not found")
