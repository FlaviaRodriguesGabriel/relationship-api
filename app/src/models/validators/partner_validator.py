__all__ = [
    "validate_partner",
]

from typing import Any, Dict

from models import PersonTypeEnum

# from models.inputs.fields import PersonType, SocialName


def validate_partner(values: Dict[str, Any]) -> Dict[str, Any]:
    values = validate_social_name_only_for_natural_person(values)
    return values


def validate_social_name_only_for_natural_person(
    values: Dict[str, Any]
) -> Dict[str, Any]:
    # FIXME: find a way to prevent circular reference imports and then uncomment this
    # person_type: PersonType = values["person_type"]
    # social_name: Optional[SocialName] = values.get("social_name")
    person_type = values["person_type"]
    social_name = values.get("social_name")

    if person_type.value is not PersonTypeEnum.FISICA and social_name is not None:
        raise ValueError("Nome social somente pode ser preenchido para pessoas físicas")

    return values
