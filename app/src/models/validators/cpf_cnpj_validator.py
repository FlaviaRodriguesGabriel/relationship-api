__all__ = [
    "CpfCnpj",
]

import re
from typing import Any, Callable, Iterable


class CpfCnpj(str):
    pattern = re.compile(r"^\d{14}|000\d{11}$")

    @classmethod
    def __get_validators__(cls) -> Iterable[Callable[[Any], str]]:
        yield cls.validate_type
        yield cls.validate_value

    @classmethod
    def validate_type(cls, value: Any) -> str:
        if not isinstance(value, str):
            raise TypeError("CPF / CNPJ deve ser uma 'string'")
        return value

    @classmethod
    def validate_value(cls, value: str) -> str:
        match = re.match(cls.pattern, value)
        if match is None:
            raise ValueError("CPF / CNPJ deve ter um preenchimento válido")
        return value
