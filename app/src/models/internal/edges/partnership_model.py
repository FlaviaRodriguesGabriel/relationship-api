__all__ = [
    "Partnership",
]

from datetime import datetime
from typing import Optional
from uuid import UUID

from models import DbModel, inputs
from models.internal.vertex import Client


class Partnership(DbModel):
    partnership_id: Optional[UUID]

    company: Client
    partner: Client

    participation_percentage: inputs.ParticipationPercentage
    role: Optional[inputs.Role]
    tenant_id: UUID

    included_at: Optional[datetime]
    updated_at: Optional[datetime]

    @classmethod
    def from_input(
        cls,
        client_company: Client,
        client_partner: Client,
        partner: inputs.Partner,
        tenant_id: UUID,
    ) -> "Partnership":
        return cls(
            company=client_company,
            partner=client_partner,
            participation_percentage=partner.participation_percentage,
            role=partner.role,
            tenant_id=tenant_id,
        )
