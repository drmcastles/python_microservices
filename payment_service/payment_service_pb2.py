# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: payment_service.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'payment_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15payment_service.proto\x12\x07payment\"C\n\x0ePaymentRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x10\n\x08order_id\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x02\"\'\n\x11GetPaymentRequest\x12\x12\n\npayment_id\x18\x01 \x01(\t\"h\n\x0fPaymentResponse\x12\x12\n\npayment_id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x10\n\x08order_id\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x02\x12\x0e\n\x06status\x18\x05 \x01(\t2\x99\x01\n\x0ePaymentService\x12\x43\n\x0eProcessPayment\x12\x17.payment.PaymentRequest\x1a\x18.payment.PaymentResponse\x12\x42\n\nGetPayment\x12\x1a.payment.GetPaymentRequest\x1a\x18.payment.PaymentResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'payment_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PAYMENTREQUEST']._serialized_start=34
  _globals['_PAYMENTREQUEST']._serialized_end=101
  _globals['_GETPAYMENTREQUEST']._serialized_start=103
  _globals['_GETPAYMENTREQUEST']._serialized_end=142
  _globals['_PAYMENTRESPONSE']._serialized_start=144
  _globals['_PAYMENTRESPONSE']._serialized_end=248
  _globals['_PAYMENTSERVICE']._serialized_start=251
  _globals['_PAYMENTSERVICE']._serialized_end=404
# @@protoc_insertion_point(module_scope)
