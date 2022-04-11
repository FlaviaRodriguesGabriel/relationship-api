#!/usr/bin/env python
from google.protobuf.descriptor import FieldDescriptor
from grpc_argument_validator import (
    AbstractArgumentValidator,
    ValidationContext,
    ValidationResult,
)

from stubs.relationship_pb2 import RelationshipType
from utils import relationships_by_type


class RelationshipTypeValidator(AbstractArgumentValidator):
    def check(
        self,
        name: str,
        value: RelationshipType,
        field_descriptor: FieldDescriptor,
        validation_context: ValidationContext,
    ) -> ValidationResult:
        if value in relationships_by_type:
            return ValidationResult(valid=True)
        return ValidationResult(False, "Field relationship_type must be valid")
