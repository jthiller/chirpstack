# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chirpstack-api/api/frame_log.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from chirpstack_api.common import common_pb2 as chirpstack__api_dot_common_dot_common__pb2
from chirpstack_api.gw import gw_pb2 as chirpstack__api_dot_gw_dot_gw__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"chirpstack-api/api/frame_log.proto\x12\x03\x61pi\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\"chirpstack-api/common/common.proto\x1a\x1a\x63hirpstack-api/gw/gw.proto\"\x90\x02\n\x0eUplinkFrameLog\x12\x13\n\x0bphy_payload\x18\x01 \x01(\x0c\x12!\n\x07tx_info\x18\x02 \x01(\x0b\x32\x10.gw.UplinkTxInfo\x12!\n\x07rx_info\x18\x03 \x03(\x0b\x32\x10.gw.UplinkRxInfo\x12\x1d\n\x06m_type\x18\x04 \x01(\x0e\x32\r.common.MType\x12\x10\n\x08\x64\x65v_addr\x18\x05 \x01(\t\x12\x0f\n\x07\x64\x65v_eui\x18\x06 \x01(\t\x12(\n\x04time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x18\n\x10plaintext_f_opts\x18\x08 \x01(\x08\x12\x1d\n\x15plaintext_frm_payload\x18\t \x01(\x08\"\x9a\x02\n\x10\x44ownlinkFrameLog\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bphy_payload\x18\x02 \x01(\x0c\x12#\n\x07tx_info\x18\x03 \x01(\x0b\x32\x12.gw.DownlinkTxInfo\x12\x13\n\x0b\x64ownlink_id\x18\x04 \x01(\r\x12\x12\n\ngateway_id\x18\x05 \x01(\t\x12\x1d\n\x06m_type\x18\x06 \x01(\x0e\x32\r.common.MType\x12\x10\n\x08\x64\x65v_addr\x18\x07 \x01(\t\x12\x0f\n\x07\x64\x65v_eui\x18\x08 \x01(\t\x12\x18\n\x10plaintext_f_opts\x18\t \x01(\x08\x12\x1d\n\x15plaintext_frm_payload\x18\n \x01(\x08\x42\x65\n\x11io.chirpstack.apiB\rFrameLogProtoP\x01Z.github.com/chirpstack/chirpstack/api/go/v4/api\xaa\x02\x0e\x43hirpstack.Apib\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chirpstack_api.api.frame_log_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\021io.chirpstack.apiB\rFrameLogProtoP\001Z.github.com/chirpstack/chirpstack/api/go/v4/api\252\002\016Chirpstack.Api'
  _UPLINKFRAMELOG._serialized_start=141
  _UPLINKFRAMELOG._serialized_end=413
  _DOWNLINKFRAMELOG._serialized_start=416
  _DOWNLINKFRAMELOG._serialized_end=698
# @@protoc_insertion_point(module_scope)
