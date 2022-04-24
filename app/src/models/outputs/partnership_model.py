__all__ = [
    "Diff",
    "Company",
    "Completeness",
    "Partner",
    "Partnership",
    "PersonType",
    "Relationship",
]

from datetime import datetime

from models import ApiModel
from models.inputs import Company as CompanyInput
from models.inputs import Completeness as CompletenessInput
from models.inputs import Partner as PartnerInput
from models.inputs import Partnership as PartnershipInput
from models.inputs import PersonType, Relationship


class Diff(ApiModel):
    open_diff: bool
    journey_id: str
    date: datetime


class Company(CompanyInput):
    company_id: str
    included_at: datetime
    updated_at: datetime


class Completeness(CompletenessInput):
    diff: Diff


class Partner(PartnerInput):
    partner_id: str
    included_at: datetime
    updated_at: datetime


class Partnership(PartnershipInput):
    ...
