__all__ = [
    "Completeness",
]


from datetime import datetime

from pydantic import Field

from .api_model import ApiModel


class Completeness(ApiModel):
    completeness_level: int = Field(alias="nivel_completude")
    additional_information: str = Field(alias="informacoes_adicionais")
    validated_at: datetime = Field(alias="data_validacao")
