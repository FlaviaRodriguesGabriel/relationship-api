__all__ = [
    "SocialName",
]

from typing import Any, Callable, Iterable


class SocialName(str):
    @classmethod
    def __get_validators__(cls) -> Iterable[Callable[[Any], str]]:
        yield cls.validate_type
        yield cls.validate_value

    @classmethod
    def validate_type(cls, value: Any) -> str:
        if not isinstance(value, str):
            raise TypeError("Nome social deve ser uma 'string'")
        return value

    @classmethod
    def validate_value(cls, value: str) -> str:
        if len(value) < 3:
            raise ValueError("Nome social deve ter um preenchimento válido")

        return value
