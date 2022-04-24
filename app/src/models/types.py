__all__ = [
    "PersonType",
    "Relationship",
]


from enum import Enum


class PersonType(str, Enum):
    FISICA = "F"
    JURIDICA = "J"


class Relationship(str, Enum):
    UNKNOWN = "UNKNOWN"
    PARTNERSHIP = "PARTNERSHIP"
    REPRESENTATIVES = "REPRESENTATIVES"
    PROSECUTORS = "PROSECUTORS"
    RELATIVES = "RELATIVES"
