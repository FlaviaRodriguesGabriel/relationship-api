__all__ = [
    "Labels",
]


from enum import Enum

from models import PersonTypeEnum


class Labels(str, Enum):
    FISICA = PersonTypeEnum.FISICA
    JURIDICA = PersonTypeEnum.JURIDICA
    PROFILE = "profile"
