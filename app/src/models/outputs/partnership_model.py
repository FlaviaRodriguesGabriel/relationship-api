__all__ = [
    "Diff",
    "OriginationDocument",
    "Company",
    "Partner",
    "Partnership",
]

from datetime import datetime

from pydantic import Field

from models import ApiModel
from models.inputs import Company as CompanyInput
from models.inputs import Partner as PartnerInput
from models.inputs import Partnership as PartnershipInput


class Diff(ApiModel):
    open_diff: bool = Field(alias="indicador_diff_aberto")
    created_at: datetime = Field(alias="data_criacao")
    updated_at: datetime = Field(alias="data_ultima_atualizacao")


class OriginationDocument(ApiModel):
    created_at: datetime = Field(alias="data_criacao")


class Company(CompanyInput):
    company_id: str = Field(alias="id_cliente")
    included_at: datetime = Field(alias="data_inclusao")
    updated_at: datetime = Field(alias="data_ultima_atualizacao")


class Partner(PartnerInput):
    partner_id: str = Field(alias="id_cliente")
    # diff: Optional[Diff] = Field(alias="diferenca_cadastral")
    # TODO: Evaluate if we should return diff ... probably not
    included_at: datetime = Field(alias="data_inclusao")
    updated_at: datetime = Field(alias="data_ultima_atualizacao")


class Partnership(PartnershipInput):
    ...
