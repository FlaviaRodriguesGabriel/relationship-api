import re

from stubs.relationship_pb2 import RelationshipType

cpf_cnpj_regex = re.compile(r"^\d{14}|000\d{11}$")

relationships_by_type = {
    RelationshipType.UNKNOWN,
    RelationshipType.PARTNERSHIP,
    RelationshipType.REPRESENTATIVES,
    RelationshipType.PROSECUTORS,
    # RelationshipType.RELATIVES,
}
