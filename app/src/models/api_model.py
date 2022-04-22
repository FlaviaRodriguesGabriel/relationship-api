__all__ = [
    "ApiModel",
]

from pydantic import BaseModel


class ApiModel(BaseModel):
    class Config:
        allow_mutation = False
        extra = "forbid"
