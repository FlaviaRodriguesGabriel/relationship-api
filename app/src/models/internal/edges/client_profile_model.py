__all__ = [
    "ClientProfile",
]


from datetime import datetime
from typing import Optional

from models import DbModel
from models.internal.vertex import Client, Profile


class ClientProfile(DbModel):
    @property
    def id(self) -> str:
        return f"{self.client.client_id}.{self.profile.tenant_id}"

    client: Client
    profile: Profile

    included_at: Optional[datetime]
    updated_at: Optional[datetime]
