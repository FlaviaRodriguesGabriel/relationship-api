__all__ = [
    "Partnership",
]

from uuid import UUID

from pydantic import Field, conlist

from models import ApiModel
from settings import Settings

from .company_model import Company
from .partner_model import Partner


class Partnership(ApiModel):
    journey_id: UUID = Field(alias="id_jornada")
    product_group_id: str = Field(alias="chave_agrupamento_produto")
    product_id: str = Field(alias="chave_produto")
    company: Company = Field(alias="pessoa_relacionada")
    partners: conlist(  # type: ignore[valid-type]
        Partner, min_items=1, max_items=Settings.max_partners_in_partnership
    ) = Field(alias="socios")
    # TODO: if relationship type proves to be useless, remove it
    # relationship: Relationship = Field(alias="relacionamento")
