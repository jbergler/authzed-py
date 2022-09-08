# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authzed/api/v1/schema_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#authzed/api/v1/schema_service.proto\x12\x0e\x61uthzed.api.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17validate/validate.proto\"\x13\n\x11ReadSchemaRequest\"5\n\x12ReadSchemaResponse\x12\x1f\n\x0bschema_text\x18\x01 \x01(\tR\nschemaText\"7\n\x12WriteSchemaRequest\x12!\n\x06schema\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04(\x80\x80\x10R\x06schema\"\x15\n\x13WriteSchemaResponse2\xf5\x01\n\rSchemaService\x12o\n\nReadSchema\x12!.authzed.api.v1.ReadSchemaRequest\x1a\".authzed.api.v1.ReadSchemaResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/v1/schema/read:\x01*\x12s\n\x0bWriteSchema\x12\".authzed.api.v1.WriteSchemaRequest\x1a#.authzed.api.v1.WriteSchemaResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1/schema/write:\x01*BH\n\x12\x63om.authzed.api.v1Z2github.com/authzed/authzed-go/proto/authzed/api/v1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.v1.schema_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.authzed.api.v1Z2github.com/authzed/authzed-go/proto/authzed/api/v1'
  _WRITESCHEMAREQUEST.fields_by_name['schema']._options = None
  _WRITESCHEMAREQUEST.fields_by_name['schema']._serialized_options = b'\372B\006r\004(\200\200\020'
  _SCHEMASERVICE.methods_by_name['ReadSchema']._options = None
  _SCHEMASERVICE.methods_by_name['ReadSchema']._serialized_options = b'\202\323\344\223\002\024\"\017/v1/schema/read:\001*'
  _SCHEMASERVICE.methods_by_name['WriteSchema']._options = None
  _SCHEMASERVICE.methods_by_name['WriteSchema']._serialized_options = b'\202\323\344\223\002\025\"\020/v1/schema/write:\001*'
  _READSCHEMAREQUEST._serialized_start=110
  _READSCHEMAREQUEST._serialized_end=129
  _READSCHEMARESPONSE._serialized_start=131
  _READSCHEMARESPONSE._serialized_end=184
  _WRITESCHEMAREQUEST._serialized_start=186
  _WRITESCHEMAREQUEST._serialized_end=241
  _WRITESCHEMARESPONSE._serialized_start=243
  _WRITESCHEMARESPONSE._serialized_end=264
  _SCHEMASERVICE._serialized_start=267
  _SCHEMASERVICE._serialized_end=512
# @@protoc_insertion_point(module_scope)
