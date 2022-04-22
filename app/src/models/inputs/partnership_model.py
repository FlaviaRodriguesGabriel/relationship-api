__all__ = [
    "PersonType",
    "Relationship",
    "Completeness",
    "Company",
    "Partner",
    "Partnership",
]

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import conlist

from models import ApiModel
from models.validators import CpfCnpj
from settings import Settings


class PersonType(str, Enum):
    FISICA = "F"
    JURIDICA = "J"


class Relationship(str, Enum):
    UNKNOWN = "UNKNOWN"
    PARTNERSHIP = "PARTNERSHIP"
    REPRESENTATIVES = "REPRESENTATIVES"
    PROSECUTORS = "PROSECUTORS"
    RELATIVES = "RELATIVES"


class Completeness(ApiModel):
    completeness_level: int
    additional_information: str
    validated_at: datetime


class Company(ApiModel):
    company_id: str
    person_type: PersonType = PersonType.JURIDICA
    cpf_cnpj: CpfCnpj
    name: str


class Partner(ApiModel):
    partner_id: str
    tenant_id: str
    participation_percentage: float
    cpf_cnpj: CpfCnpj
    person_type: str
    name: Optional[str]
    social_name: str
    completeness: Completeness


class Partnership(ApiModel):
    company: Company
    partners: conlist(  # type: ignore[valid-type]
        Partner, min_items=1, max_items=Settings.max_partners_in_partnership
    )
    relationship: Relationship
