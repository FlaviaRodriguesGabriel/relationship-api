__all__ = [
    "Company",
]

from typing import Optional

from pydantic import Field

from models import ApiModel

from .fields import OriginationDocument, PersonName, PersonType


class Company(ApiModel):
    person_type: PersonType = Field(alias="tipo_pessoa")
    origination_document: OriginationDocument = Field(alias="documento_originacao")
    name: Optional[PersonName] = Field(alias="nome")
