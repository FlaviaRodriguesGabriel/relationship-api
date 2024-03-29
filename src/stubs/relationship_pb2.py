# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: relationship.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12relationship.proto\x12\x12stubs.relationship\x1a\x1fgoogle/protobuf/timestamp.proto\"\xd7\x01\n\x1a\x42usinessPartnershipMessage\x12?\n\x11relationship_type\x18\x01 \x01(\x0e\x32$.stubs.relationship.RelationshipType\x12;\n\x0f\x63ompany_message\x18\x02 \x01(\x0b\x32\".stubs.relationship.CompanyMessage\x12;\n\x0fpartner_message\x18\x03 \x03(\x0b\x32\".stubs.relationship.PartnerMessage\"\xba\x01\n\x0e\x43ompanyMessage\x12\x12\n\ncompany_id\x18\x01 \x01(\t\x12\x13\n\x0bperson_type\x18\x02 \x01(\t\x12\x10\n\x08\x63pf_cnpj\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12/\n\x0bincluded_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xba\x01\n\x13\x43ompletenessMessage\x12\x1a\n\x12\x63ompleteness_level\x18\x01 \x01(\x05\x12\x1e\n\x16\x61\x64\x64itional_information\x18\x02 \x01(\t\x12\x35\n\x0c\x64iff_message\x18\x03 \x01(\x0b\x32\x1f.stubs.relationship.DiffMessage\x12\x30\n\x0cvalidated_at\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"^\n\x0b\x44iffMessage\x12\x11\n\topen_diff\x18\x01 \x01(\x08\x12\x12\n\njourney_id\x18\x02 \x01(\t\x12(\n\x04\x64\x61te\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\xc3\x02\n\x0ePartnerMessage\x12\x12\n\npartner_id\x18\x01 \x01(\t\x12\x11\n\ttenant_id\x18\x02 \x01(\t\x12 \n\x18participation_percentage\x18\x03 \x01(\x01\x12\x10\n\x08\x63pf_cnpj\x18\x04 \x01(\t\x12\x13\n\x0bperson_type\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x13\n\x0bsocial_name\x18\x07 \x01(\t\x12=\n\x0c\x63ompleteness\x18\x08 \x01(\x0b\x32\'.stubs.relationship.CompletenessMessage\x12/\n\x0bincluded_at\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\nupdated_at\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp*e\n\x10RelationshipType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0f\n\x0bPARTNERSHIP\x10\x01\x12\x13\n\x0fREPRESENTATIVES\x10\x02\x12\x0f\n\x0bPROSECUTORS\x10\x03\x12\r\n\tRELATIVES\x10\x04\x32\xe2\x03\n\x12PartnershipService\x12p\n\x0e\x41\x64\x64Partnership\x12..stubs.relationship.BusinessPartnershipMessage\x1a..stubs.relationship.BusinessPartnershipMessage\x12p\n\x0eGetPartnership\x12..stubs.relationship.BusinessPartnershipMessage\x1a..stubs.relationship.BusinessPartnershipMessage\x12s\n\x11UpdatePartnership\x12..stubs.relationship.BusinessPartnershipMessage\x1a..stubs.relationship.BusinessPartnershipMessage\x12s\n\x11\x44\x65letePartnership\x12..stubs.relationship.BusinessPartnershipMessage\x1a..stubs.relationship.BusinessPartnershipMessageb\x06proto3')

_RELATIONSHIPTYPE = DESCRIPTOR.enum_types_by_name['RelationshipType']
RelationshipType = enum_type_wrapper.EnumTypeWrapper(_RELATIONSHIPTYPE)
UNKNOWN = 0
PARTNERSHIP = 1
REPRESENTATIVES = 2
PROSECUTORS = 3
RELATIVES = 4


_BUSINESSPARTNERSHIPMESSAGE = DESCRIPTOR.message_types_by_name['BusinessPartnershipMessage']
_COMPANYMESSAGE = DESCRIPTOR.message_types_by_name['CompanyMessage']
_COMPLETENESSMESSAGE = DESCRIPTOR.message_types_by_name['CompletenessMessage']
_DIFFMESSAGE = DESCRIPTOR.message_types_by_name['DiffMessage']
_PARTNERMESSAGE = DESCRIPTOR.message_types_by_name['PartnerMessage']
BusinessPartnershipMessage = _reflection.GeneratedProtocolMessageType('BusinessPartnershipMessage', (_message.Message,), {
  'DESCRIPTOR' : _BUSINESSPARTNERSHIPMESSAGE,
  '__module__' : 'relationship_pb2'
  # @@protoc_insertion_point(class_scope:stubs.relationship.BusinessPartnershipMessage)
  })
_sym_db.RegisterMessage(BusinessPartnershipMessage)

CompanyMessage = _reflection.GeneratedProtocolMessageType('CompanyMessage', (_message.Message,), {
  'DESCRIPTOR' : _COMPANYMESSAGE,
  '__module__' : 'relationship_pb2'
  # @@protoc_insertion_point(class_scope:stubs.relationship.CompanyMessage)
  })
_sym_db.RegisterMessage(CompanyMessage)

CompletenessMessage = _reflection.GeneratedProtocolMessageType('CompletenessMessage', (_message.Message,), {
  'DESCRIPTOR' : _COMPLETENESSMESSAGE,
  '__module__' : 'relationship_pb2'
  # @@protoc_insertion_point(class_scope:stubs.relationship.CompletenessMessage)
  })
_sym_db.RegisterMessage(CompletenessMessage)

DiffMessage = _reflection.GeneratedProtocolMessageType('DiffMessage', (_message.Message,), {
  'DESCRIPTOR' : _DIFFMESSAGE,
  '__module__' : 'relationship_pb2'
  # @@protoc_insertion_point(class_scope:stubs.relationship.DiffMessage)
  })
_sym_db.RegisterMessage(DiffMessage)

PartnerMessage = _reflection.GeneratedProtocolMessageType('PartnerMessage', (_message.Message,), {
  'DESCRIPTOR' : _PARTNERMESSAGE,
  '__module__' : 'relationship_pb2'
  # @@protoc_insertion_point(class_scope:stubs.relationship.PartnerMessage)
  })
_sym_db.RegisterMessage(PartnerMessage)

_PARTNERSHIPSERVICE = DESCRIPTOR.services_by_name['PartnershipService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RELATIONSHIPTYPE._serialized_start=1093
  _RELATIONSHIPTYPE._serialized_end=1194
  _BUSINESSPARTNERSHIPMESSAGE._serialized_start=76
  _BUSINESSPARTNERSHIPMESSAGE._serialized_end=291
  _COMPANYMESSAGE._serialized_start=294
  _COMPANYMESSAGE._serialized_end=480
  _COMPLETENESSMESSAGE._serialized_start=483
  _COMPLETENESSMESSAGE._serialized_end=669
  _DIFFMESSAGE._serialized_start=671
  _DIFFMESSAGE._serialized_end=765
  _PARTNERMESSAGE._serialized_start=768
  _PARTNERMESSAGE._serialized_end=1091
  _PARTNERSHIPSERVICE._serialized_start=1197
  _PARTNERSHIPSERVICE._serialized_end=1679
# @@protoc_insertion_point(module_scope)
