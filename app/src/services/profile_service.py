__all__ = [
    "ProfileService",
]

from datetime import datetime
from typing import List, Optional, Tuple
from uuid import UUID

from gremlin_python.process.graph_traversal import (
    GraphTraversal,
    GraphTraversalSource,
    __,
)
from gremlin_python.process.traversal import T
from gremlin_python.structure.graph import Edge, Vertex
from loguru import logger

from clients import PowerOIG
from models import PersonTypeEnum, internal
from utils import Singleton


class ProfileService(Singleton):
    graph: GraphTraversalSource
    power_oig: PowerOIG

    def __init__(self, graph: GraphTraversalSource, *args, **kwargs) -> None:
        self.graph = graph
        super().__init__(*args, **kwargs)

    def _create_edge(self, client_profile: internal.edges.ClientProfile) -> Edge:
        client_profile.included_at = client_profile.updated_at = datetime.utcnow()

        return (
            self.graph.V(client_profile.client.client_id)
            .add_e("has_profile")
            # TODO: make this a single query using get/created vertex/id from before
            .to(self.graph.V(client_profile.profile.profile_id).next())
            .property(T.id, client_profile.id)
            # .property("client", client_profile.client.dict())
            # .property("profile", client_profile.profile.dict())
            .property("included_at", client_profile.included_at)
            .property("updated_at", client_profile.updated_at)
            .iterate()
        )

    def _create_vertex(self, profile: internal.vertex.Profile) -> Vertex:
        profile.included_at = profile.updated_at = datetime.utcnow()

        vertex: Vertex = (
            self.graph.add_v(internal.vertex.Labels.PROFILE)
            .property(T.id, profile.profile_id)
            # FIXME: .dict() here and similar lines in all code is not working as expected
            .property("client", profile.client.dict())
            .property("name", profile.name.dict() if profile.name else None)
            .property("tenant_id", profile.tenant_id)
            .property("included_at", profile.included_at)
            .property("updated_at", profile.updated_at)
        ).next()

        if (
            profile.client.person_type.value is PersonTypeEnum.FISICA
            and profile.social_name is not None
        ):
            self.graph.V().has(T.id, profile.profile_id).property(
                "social_name", profile.social_name.dict()
            ).next()

        return vertex

    def _get_or_create_edge(self, client_profile: internal.edges.ClientProfile) -> Edge:
        edges = self.get_edges(
            client_id=client_profile.client.client_id,  # type: ignore # FIXME: should not ignore typing
            profile_id=client_profile.profile.profile_id,
        )
        if edges:
            edge = edges[0]
            if len(edges) > 1:
                logger.warning(
                    "It was found more than one relationship"
                    f" between client #{client_profile.client.client_id}"
                    f" and partner #{client_profile.profile.profile_id}."
                    f" Returning that first one: #{edge.id}."
                )
        # TODO: implement upsert in case of equal or greater completeness level (may need to change this method name to something related with upsert)

        else:
            edge = self._create_edge(client_profile)

        return edge

    def _get_or_create_vertex(self, profile: internal.vertex.Profile) -> Vertex:
        vertex = self.get_vertex(profile.profile_id)
        # TODO: implement upsert in case of equal or greater completeness level (may need to change this method name to something related with upsert)

        if not vertex:
            vertex = self._create_vertex(profile)

        return vertex

    def create(
        self, client_profile: internal.edges.ClientProfile
    ) -> Tuple[Vertex, Edge]:
        vertex = self._create_vertex(client_profile.profile)
        edge = self._create_edge(client_profile)

        return vertex, edge

    def get_vertex(self, id: str) -> Optional[Vertex]:
        query: GraphTraversal = self.graph.V().has(T.id, id)
        if query.has_next():
            return query.next()
        else:
            return None

    def get_edges(self, client_id: UUID, profile_id: str) -> List[Edge]:
        query = (
            self.graph.V(client_id)
            .out_e("has_profile")  # TODO: make a shared constant of "has_profile"
            .where(__.in_v().where(__.has_id(profile_id)))
        )

        edges = []
        while query.has_next():
            edge = query.next()
            edges.append(edge)

        return edges

    def get_or_create(
        self, client_profile: internal.edges.ClientProfile
    ) -> Tuple[Vertex, Edge]:
        vertex = self._get_or_create_vertex(client_profile.profile)
        edge = self._get_or_create_edge(client_profile)

        return vertex, edge
