__all__ = [
    "RelationshipApiException",
]


from abc import ABC


class RelationshipApiException(ABC, Exception):
    status_code: int
