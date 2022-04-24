__all__ = [
    "validate_partner",
]

from typing import Any, Dict

from models import PersonType


def validate_partner(values: Dict[str, Any]) -> Dict[str, Any]:
    values = validate_social_name_only_for_natural_person(values)
    return values


def validate_social_name_only_for_natural_person(
    values: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Reusable validator for pydantic models
    """
    if (values["person_type"] != PersonType.FISICA) & (
        values["social_name"] is not None
    ):
        raise ValueError("Nome social somente pode ser preenchido para pessoas físicas")
    return values
