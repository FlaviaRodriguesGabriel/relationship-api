import re

from google.protobuf.descriptor import FieldDescriptor
from grpc_argument_validator import (
    AbstractArgumentValidator,
    ValidationContext,
    ValidationResult,
)

from stubs.relationship_pb2 import CompanyMessage
from utils import cpf_cnpj_regex


class CompanyMessageValidator(AbstractArgumentValidator):
    def check(
        self,
        name: str,
        value: CompanyMessage,
        field_descriptor: FieldDescriptor,
        validation_context: ValidationContext,
    ) -> ValidationResult:
        if value.person_type != "J":
            return ValidationResult(
                False, "Field company_message.person_type must be equal to 'J'"
            )

        if re.match(cpf_cnpj_regex, value.cpf_cnpj) is None:
            return ValidationResult(
                False, "Field company_message.cpf_cnpj must be a string with 14 digits"
            )

        return ValidationResult(valid=True)
