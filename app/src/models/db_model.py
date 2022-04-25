__all__ = [
    "DbModel",
]

from pydantic import BaseModel


class DbModel(BaseModel):
    class Config:
        allow_mutation = True
        extra = "forbid"
