__all__ = [
    "Completeness",
    "Company",
    "Partner",
    "Partnership",
]

from datetime import datetime
from typing import Any, Dict, Optional
from uuid import UUID

from pydantic import Field, conlist, root_validator

from models import ApiModel, PersonType, Relationship
from models.validators import CpfCnpj, Name, SocialName, validate_partner
from settings import Settings


class Completeness(ApiModel):
    completeness_level: int = Field(alias="nivel_completude")
    additional_information: str = Field(alias="informacoes_adicionais")
    validated_at: datetime = Field(alias="data_validacao")


class Company(ApiModel):
    person_type: PersonType = Field(alias="tipo_pessoa")
    cpf_cnpj: CpfCnpj = Field(alias="documento_originacao")
    name: Optional[Name] = Field(alias="nome")


class Partner(ApiModel):
    participation_percentage: float = Field(alias="percentual_participacao")
    cpf_cnpj: CpfCnpj = Field(alias="documento_originacao")
    person_type: PersonType = Field(alias="tipo_pessoa")
    name: Optional[Name] = Field(alias="nome")
    social_name: Optional[SocialName] = Field(alias="nome_social")
    role: Optional[str] = Field(alias="cargo")
    completeness: Completeness = Field(alias="validacoes")

    @root_validator
    def validate_root(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        return validate_partner(values)


class Partnership(ApiModel):
    tenant_id: UUID = Field(alias="id_inquilino")
    journey_id: UUID = Field(alias="id_jornada")
    company: Company = Field(alias="pessoa")
    partners: conlist(  # type: ignore[valid-type]
        Partner, min_items=1, max_items=Settings.max_partners_in_partnership
    ) = Field(alias="socios")
    relationship: Relationship = Field(alias="relacionamento")
