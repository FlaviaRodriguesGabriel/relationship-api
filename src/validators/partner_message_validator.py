import re

from google.protobuf.descriptor import FieldDescriptor
from grpc_argument_validator import (
    AbstractArgumentValidator,
    ValidationContext,
    ValidationResult,
)

from stubs.relationship_pb2 import PartnerMessage
from utils import cpf_cnpj_regex


class PartnerMessageValidator(AbstractArgumentValidator):
    completeness_levels = {100, 150, 200, 300, 400}

    def check(
        self,
        name: str,
        value: PartnerMessage,
        field_descriptor: FieldDescriptor,
        validation_context: ValidationContext,
    ) -> ValidationResult:
        if value.person_type not in {"F", "J"}:
            return ValidationResult(
                False, "Field partner_message.person_type must be 'F' or 'J'"
            )

        if re.match(cpf_cnpj_regex, value.cpf_cnpj) is None:
            return ValidationResult(
                False, "Field partner_message.cpf_cnpj must be a string with 14 digits"
            )

        if value.completeness.completeness_level not in self.completeness_levels:
            return ValidationResult(
                False,
                "Field company_message.completeness.completeness_level must be valid",
            )

        return ValidationResult(valid=True)
