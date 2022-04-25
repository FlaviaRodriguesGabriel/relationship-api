__all__ = [
    "Client",
]

from datetime import datetime
from typing import Optional
from uuid import UUID

from models import DbModel, inputs


class Client(DbModel):
    client_id: Optional[UUID]

    origination_document: inputs.OriginationDocument
    person_type: inputs.PersonType

    included_at: Optional[datetime]
    updated_at: Optional[datetime]

    @classmethod
    def from_company(cls, company: inputs.Company, client_id: UUID) -> "Client":
        return cls(
            client_id=client_id,
            origination_document=company.origination_document,
            person_type=company.person_type,
        )

    @classmethod
    def from_partner(cls, partner: inputs.Partner) -> "Client":
        return cls(
            origination_document=partner.origination_document,
            person_type=partner.person_type,
        )
