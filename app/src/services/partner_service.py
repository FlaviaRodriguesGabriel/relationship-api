__all__ = [
    "PartnerService",
]

from datetime import datetime
from typing import List, Optional, Tuple
from uuid import UUID, uuid4

from gremlin_python.process.graph_traversal import (
    GraphTraversal,
    GraphTraversalSource,
    __,
)
from gremlin_python.process.traversal import T
from gremlin_python.structure.graph import Edge, Vertex
from loguru import logger

from clients import PowerOIG
from models import internal
from utils import Singleton


class PartnerService(Singleton):
    graph: GraphTraversalSource
    power_oig: PowerOIG

    def __init__(
        self,
        graph: GraphTraversalSource,
        power_oig: Optional[PowerOIG] = None,
        *args,
        **kwargs,
    ) -> None:
        self.graph = graph
        self.power_oig = power_oig or PowerOIG()
        super().__init__(*args, **kwargs)

    def _create_edge(self, partnership: internal.Partnership) -> Edge:
        partnership.partnership_id == uuid4()
        partnership.included_at = partnership.updated_at = datetime.utcnow()

        return (
            self.graph.V(partnership.company.client_id)
            .add_e("has_partner")
            # TODO: make this a single query using get/created vertex/id from before
            .to(self.graph.V(partnership.partner.client_id).next())
            .property(T.id, partnership.partnership_id)
            # .property("client_origin",partnership.client_origin.dict())
            # .property("client_target",partnership.client_target.dict())
            .property(
                "participation_percentage", partnership.participation_percentage.dict()
            )
            .property("role", partnership.role.dict() if partnership.role else None)
            .property("tenant_id", partnership.tenant_id)
            .property("included_at", partnership.included_at)
            .property("updated_at", partnership.updated_at)
            .iterate()
        )

    def _create_vertex(self, partner: internal.vertex.Client) -> Vertex:
        partner.included_at = partner.updated_at = datetime.utcnow()

        return (
            self.graph.add_v(partner.person_type.value)
            .property(T.id, partner.client_id)
            .property("origination_document", partner.origination_document.dict())
            .property("person_type", partner.person_type.dict())
            .property("included_at", partner.included_at)
            .property("updated_at", partner.updated_at)
        ).next()

    def _get_or_create_edge(self, partnership: internal.edges.Partnership) -> Edge:
        edges = self.get_edges(
            company_id=partnership.company.client_id,  # type: ignore # FIXME: should not ignore typing
            partner_id=partnership.partner.client_id,  # type: ignore # FIXME: should not ignore typing
        )
        if edges:
            edge = edges[0]
            if len(edges) > 1:
                logger.warning(
                    "It was found more than one relationship"
                    f" between company #{partnership.company.client_id}"
                    f" and partner #{partnership.partner.client_id}."
                    f" Returning that first one: #{edge.id}."
                )
        # TODO: implement upsert in case of equal or greater completeness level (may need to change this method name to something related with upsert)

        else:
            edge = self._create_edge(partnership)

        return edge

    def _get_or_create_vertex(self, partner: internal.vertex.Client) -> Vertex:
        partner.client_id = self.power_oig.get_partner_id(partner)

        vertex = self.get_vertex(partner.client_id)
        # TODO: implement upsert in case of equal or greater completeness level (may need to change this method name to something related with upsert)
        if not vertex:
            vertex = self._create_vertex(partner)

        return vertex

    def create(self, partnership: internal.edges.Partnership) -> Tuple[Vertex, Edge]:
        vertex = self._create_vertex(partnership.partner)
        edge = self._create_edge(partnership)

        return vertex, edge

    def get_vertex(self, id: UUID) -> Optional[Vertex]:
        query: GraphTraversal = self.graph.V().has(T.id, id)
        if query.has_next():
            return query.next()
        else:
            return None

    def get_edges(self, company_id: UUID, partner_id: UUID) -> List[Edge]:
        query = (
            self.graph.V(company_id)
            .out_e("has_partner")  # TODO: make a shared constant of "has_partner"
            .where(__.in_v().where(__.has_id(partner_id)))
        )

        edges = []
        while query.has_next():
            edge = query.next()
            edges.append(edge)

        return edges

    def get_or_create(
        self, partnership: internal.edges.Partnership
    ) -> Tuple[Vertex, Edge]:
        vertex = self._get_or_create_vertex(partnership.partner)
        edge = self._get_or_create_edge(partnership)

        return vertex, edge
