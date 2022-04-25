__all__ = [
    "Partner",
]

from typing import Any, Dict, Optional

from pydantic import Field, root_validator

from models import ApiModel
from models.validators import validate_partner

from .fields import (
    OriginationDocument,
    ParticipationPercentage,
    PersonName,
    PersonSocialName,
    PersonType,
    Role,
)


class Partner(ApiModel):
    participation_percentage: ParticipationPercentage = Field(
        alias="percentual_participacao"
    )
    origination_document: OriginationDocument = Field(alias="documento_originacao")
    person_type: PersonType = Field(alias="tipo_pessoa")
    name: Optional[PersonName] = Field(alias="nome")
    social_name: Optional[PersonSocialName] = Field(alias="nome_social")
    role: Optional[Role] = Field(alias="cargo")

    @root_validator
    def validate_root(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        return validate_partner(values)
