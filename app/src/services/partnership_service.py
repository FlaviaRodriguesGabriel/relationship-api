__all__ = [
    "PartnershipService",
]

from typing import List, Optional, Tuple
from uuid import UUID

from gremlin_python.process.graph_traversal import GraphTraversalSource
from gremlin_python.structure.graph import Edge

from models import inputs, internal, outputs
from utils import Singleton

from .company_service import CompanyService
from .partner_service import PartnerService
from .profile_service import ProfileService


class PartnershipService(Singleton):
    graph: GraphTraversalSource

    company_service: CompanyService
    partner_service: PartnerService

    def __init__(
        self,
        graph: GraphTraversalSource,
        company_service: Optional[CompanyService] = None,
        partner_service: Optional[PartnerService] = None,
        profile_service: Optional[ProfileService] = None,
        *args,
        **kwargs,
    ) -> None:
        self.graph = graph
        self.company_service = company_service or CompanyService(graph)
        self.partner_service = partner_service or PartnerService(graph)
        self.profile_service = profile_service or ProfileService(graph)
        super().__init__(*args, **kwargs)

    @staticmethod
    def _convert_from_input(
        partnership: inputs.Partnership,
        tenant_id: UUID,
        client_id: UUID,
    ) -> Tuple[
        internal.edges.ClientProfile,
        List[Tuple[internal.edges.ClientProfile, internal.edges.Partnership]],
    ]:
        client_company = internal.vertex.Client.from_company(
            company=partnership.company,
            client_id=client_id,
        )
        company_profile = internal.vertex.Profile.from_company(
            client=client_company,
            company=partnership.company,
            tenant_id=tenant_id,
        )
        client_profile_company = internal.edges.ClientProfile(
            client=client_company,
            profile=company_profile,
        )

        partners_relationships: List[
            Tuple[internal.edges.ClientProfile, internal.edges.Partnership]
        ] = []

        for partner in partnership.partners:
            client_partner = internal.vertex.Client.from_partner(partner)
            partner_profile = internal.vertex.Profile.from_partner(
                client=client_partner,
                partner=partner,
                tenant_id=tenant_id,
            )

            client_profile_partner = internal.edges.ClientProfile(
                client=client_partner,
                profile=partner_profile,
            )

            partnership_edge = internal.edges.Partnership.from_input(
                client_company=client_company,
                client_partner=client_partner,
                partner=partner,
                tenant_id=tenant_id,
            )

            partners_relationships.append((client_profile_partner, partnership_edge))

        return (
            client_profile_company,
            partners_relationships,
        )

    @staticmethod
    def _convert_to_output(**kwargs) -> outputs.Partnership:
        ...  # TODO: to be implemented

    def create_from_model(
        self,
        partnership: inputs.Partnership,
        tenant_id: UUID,  # TODO: make use of this argument
        client_id: UUID,  # TODO: make use of this argument
    ) -> outputs.Partnership:
        client_profile_company, partners_relationships = self._convert_from_input(
            partnership=partnership,
            tenant_id=tenant_id,
            client_id=client_id,
        )

        self.company_service.get_or_create(client_profile_company.client)
        _, company_profile_edge = self.profile_service.get_or_create(
            client_profile_company
        )

        partner_edges: List[Edge] = []
        partner_profile_edges: List[Edge] = []
        for client_profile_partner, partnership_edge_model in partners_relationships:
            _, partner_edge = self.partner_service.get_or_create(partnership_edge_model)
            _, partner_profile_edge = self.profile_service.get_or_create(
                client_profile_partner
            )

            partner_edges.append(partner_edge)
            partner_profile_edges.append(partner_profile_edge)

        ################################################################################
        # Translate internal to output models
        # TODO: Retrieve object from DB instead of parsing input
        self._convert_to_output(
            company_profile_edge=company_profile_edge,
            partner_edges=partner_edges,
            partner_profile_edges=partner_profile_edges,
        )
        return outputs.Partnership(**partnership.dict(by_alias=True))
