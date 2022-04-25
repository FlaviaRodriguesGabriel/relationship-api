__all__ = [
    "OriginationDocument",
    "ParticipationPercentage",
    "PersonName",
    "PersonSocialName",
    "PersonType",
    "Role",
]


from pydantic import Field

from models import ApiModel, Completeness, PersonTypeEnum
from models.validators import CpfCnpj, Name, SocialName


class OriginationDocument(ApiModel):
    number: CpfCnpj = Field(alias="numero")
    type: int = Field(alias="tipo")
    country: str = Field(alias="pais")
    completeness: Completeness = Field(alias="validacoes")


class ParticipationPercentage(ApiModel):
    value: float = Field(alias="valor_dado_cadastral")
    completeness: Completeness = Field(alias="validacoes")


class PersonName(ApiModel):
    value: Name = Field(alias="valor_dado_cadastral")
    completeness: Completeness = Field(alias="validacoes")


class PersonSocialName(ApiModel):
    value: SocialName = Field(alias="valor_dado_cadastral")
    completeness: Completeness = Field(alias="validacoes")


class PersonType(ApiModel):
    value: PersonTypeEnum = Field(alias="valor_dado_cadastral")
    completeness: Completeness = Field(alias="validacoes")


class Role(ApiModel):
    value: str = Field(alias="valor_dado_cadastral")
    completeness: Completeness = Field(alias="validacoes")
