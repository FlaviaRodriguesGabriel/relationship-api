__all__ = [
    "PersonTypeEnum",
    # "Relationship",
]


from enum import Enum


class PersonTypeEnum(str, Enum):
    FISICA = "F"
    JURIDICA = "J"


# TODO: If relationship type proves to be useless, remove it
# class Relationship(str, Enum):
#     UNKNOWN = "UNKNOWN"
#     PARTNERSHIP = "PARTNERSHIP"
#     REPRESENTATIVES = "REPRESENTATIVES"
#     PROSECUTORS = "PROSECUTORS"
#     RELATIVES = "RELATIVES"
