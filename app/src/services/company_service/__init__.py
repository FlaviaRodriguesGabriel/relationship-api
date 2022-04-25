__all__ = [
    "CompanyService",
    "ClientIdMismatch",
]

from datetime import datetime
from typing import Optional
from uuid import UUID

from gremlin_python.process.graph_traversal import GraphTraversal, GraphTraversalSource
from gremlin_python.process.traversal import T
from gremlin_python.structure.graph import Vertex

from clients import PowerOIG
from models import internal
from utils import Singleton

from .exceptions import ClientIdMismatch


class CompanyService(Singleton):
    graph: GraphTraversalSource
    power_oig: PowerOIG

    def __init__(
        self,
        graph: GraphTraversalSource,
        power_oig: Optional[PowerOIG] = None,
        *args,
        **kwargs
    ) -> None:
        self.graph = graph
        self.power_oig = power_oig or PowerOIG()
        super().__init__(*args, **kwargs)

    def create(self, company: internal.vertex.Client) -> Vertex:
        company.included_at = company.updated_at = datetime.utcnow()

        return (
            self.graph.add_v(company.person_type.value)
            .property(T.id, company.client_id)
            .property("origination_document", company.origination_document.dict())
            .property("person_type", company.person_type.dict())
            .property("included_at", company.included_at)
            .property("updated_at", company.updated_at)
            .next()
        )

    def get(self, id: UUID) -> Optional[Vertex]:
        query: GraphTraversal = self.graph.V().has(T.id, id)
        if query.has_next():
            return query.next()
        else:
            return None

    def get_or_create(self, company: internal.vertex.Client) -> Vertex:
        query_id = self.power_oig.get_company_id(company)
        if company.client_id != query_id:
            raise ClientIdMismatch(
                input_client_id=company.client_id,  # type: ignore # FIXME: should not ignore typing
                queried_client_id=query_id,
            )

        vertex = self.get(company.client_id)  # type: ignore # FIXME: should not ignore typing
        if not vertex:
            vertex = self.create(company=company)
        return vertex
