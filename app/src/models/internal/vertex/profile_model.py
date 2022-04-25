__all__ = [
    "Profile",
]

from datetime import datetime
from typing import Optional
from uuid import UUID

from models import DbModel, inputs

from .client_model import Client


class Profile(DbModel):
    @property
    def profile_id(self) -> str:
        return f"{self.client.client_id}.{self.tenant_id}"

    client: Client
    name: Optional[inputs.PersonName]
    social_name: Optional[inputs.PersonSocialName]
    tenant_id: UUID

    included_at: Optional[datetime]
    updated_at: Optional[datetime]

    @classmethod
    def from_company(
        cls,
        client: Client,
        company: inputs.Company,
        tenant_id: UUID,
    ) -> "Profile":
        return cls(
            client=client,
            name=company.name,
            tenant_id=tenant_id,
        )

    @classmethod
    def from_partner(
        cls,
        client: Client,
        partner: inputs.Partner,
        tenant_id: UUID,
    ) -> "Profile":
        return cls(
            client=client,
            name=partner.name,
            social_name=partner.social_name,
            tenant_id=tenant_id,
        )
