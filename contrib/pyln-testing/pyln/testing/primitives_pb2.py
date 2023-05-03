# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: primitives.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10primitives.proto\x12\x03\x63ln\"\x16\n\x06\x41mount\x12\x0c\n\x04msat\x18\x01 \x01(\x04\"D\n\x0b\x41mountOrAll\x12\x1d\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x0b.cln.AmountH\x00\x12\r\n\x03\x61ll\x18\x02 \x01(\x08H\x00\x42\x07\n\x05value\"D\n\x0b\x41mountOrAny\x12\x1d\n\x06\x61mount\x18\x01 \x01(\x0b\x32\x0b.cln.AmountH\x00\x12\r\n\x03\x61ny\x18\x02 \x01(\x08H\x00\x42\x07\n\x05value\"\x19\n\x17\x43hannelStateChangeCause\"(\n\x08Outpoint\x12\x0c\n\x04txid\x18\x01 \x01(\x0c\x12\x0e\n\x06outnum\x18\x02 \x01(\r\"h\n\x07\x46\x65\x65rate\x12\x0e\n\x04slow\x18\x01 \x01(\x08H\x00\x12\x10\n\x06normal\x18\x02 \x01(\x08H\x00\x12\x10\n\x06urgent\x18\x03 \x01(\x08H\x00\x12\x0f\n\x05perkb\x18\x04 \x01(\rH\x00\x12\x0f\n\x05perkw\x18\x05 \x01(\rH\x00\x42\x07\n\x05style\":\n\nOutputDesc\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x1b\n\x06\x61mount\x18\x02 \x01(\x0b\x32\x0b.cln.Amount\"t\n\x08RouteHop\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x18\n\x10short_channel_id\x18\x02 \x01(\t\x12\x1c\n\x07\x66\x65\x65\x62\x61se\x18\x03 \x01(\x0b\x32\x0b.cln.Amount\x12\x0f\n\x07\x66\x65\x65prop\x18\x04 \x01(\r\x12\x13\n\x0b\x65xpirydelta\x18\x05 \x01(\r\"(\n\tRoutehint\x12\x1b\n\x04hops\x18\x01 \x03(\x0b\x32\r.cln.RouteHop\".\n\rRoutehintList\x12\x1d\n\x05hints\x18\x02 \x03(\x0b\x32\x0e.cln.Routehint\"\'\n\x08TlvEntry\x12\x0c\n\x04type\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x0c\"+\n\tTlvStream\x12\x1e\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\r.cln.TlvEntry*$\n\x0b\x43hannelSide\x12\t\n\x05LOCAL\x10\x00\x12\n\n\x06REMOTE\x10\x01*\x84\x02\n\x0c\x43hannelState\x12\x0c\n\x08Openingd\x10\x00\x12\x1a\n\x16\x43hanneldAwaitingLockin\x10\x01\x12\x12\n\x0e\x43hanneldNormal\x10\x02\x12\x18\n\x14\x43hanneldShuttingDown\x10\x03\x12\x17\n\x13\x43losingdSigexchange\x10\x04\x12\x14\n\x10\x43losingdComplete\x10\x05\x12\x16\n\x12\x41waitingUnilateral\x10\x06\x12\x14\n\x10\x46undingSpendSeen\x10\x07\x12\x0b\n\x07Onchain\x10\x08\x12\x15\n\x11\x44ualopendOpenInit\x10\t\x12\x1b\n\x17\x44ualopendAwaitingLockin\x10\n*\x8a\x02\n\tHtlcState\x12\x0f\n\x0bSentAddHtlc\x10\x00\x12\x11\n\rSentAddCommit\x10\x01\x12\x15\n\x11RcvdAddRevocation\x10\x02\x12\x14\n\x10RcvdAddAckCommit\x10\x03\x12\x18\n\x14SentAddAckRevocation\x10\x04\x12\x18\n\x14RcvdAddAckRevocation\x10\x05\x12\x12\n\x0eRcvdRemoveHtlc\x10\x06\x12\x14\n\x10RcvdRemoveCommit\x10\x07\x12\x18\n\x14SentRemoveRevocation\x10\x08\x12\x17\n\x13SentRemoveAckCommit\x10\t\x12\x1b\n\x17RcvdRemoveAckRevocation\x10\nb\x06proto3')

_CHANNELSIDE = DESCRIPTOR.enum_types_by_name['ChannelSide']
ChannelSide = enum_type_wrapper.EnumTypeWrapper(_CHANNELSIDE)
_CHANNELSTATE = DESCRIPTOR.enum_types_by_name['ChannelState']
ChannelState = enum_type_wrapper.EnumTypeWrapper(_CHANNELSTATE)
_HTLCSTATE = DESCRIPTOR.enum_types_by_name['HtlcState']
HtlcState = enum_type_wrapper.EnumTypeWrapper(_HTLCSTATE)
LOCAL = 0
REMOTE = 1
Openingd = 0
ChanneldAwaitingLockin = 1
ChanneldNormal = 2
ChanneldShuttingDown = 3
ClosingdSigexchange = 4
ClosingdComplete = 5
AwaitingUnilateral = 6
FundingSpendSeen = 7
Onchain = 8
DualopendOpenInit = 9
DualopendAwaitingLockin = 10
SentAddHtlc = 0
SentAddCommit = 1
RcvdAddRevocation = 2
RcvdAddAckCommit = 3
SentAddAckRevocation = 4
RcvdAddAckRevocation = 5
RcvdRemoveHtlc = 6
RcvdRemoveCommit = 7
SentRemoveRevocation = 8
SentRemoveAckCommit = 9
RcvdRemoveAckRevocation = 10


_AMOUNT = DESCRIPTOR.message_types_by_name['Amount']
_AMOUNTORALL = DESCRIPTOR.message_types_by_name['AmountOrAll']
_AMOUNTORANY = DESCRIPTOR.message_types_by_name['AmountOrAny']
_CHANNELSTATECHANGECAUSE = DESCRIPTOR.message_types_by_name['ChannelStateChangeCause']
_OUTPOINT = DESCRIPTOR.message_types_by_name['Outpoint']
_FEERATE = DESCRIPTOR.message_types_by_name['Feerate']
_OUTPUTDESC = DESCRIPTOR.message_types_by_name['OutputDesc']
_ROUTEHOP = DESCRIPTOR.message_types_by_name['RouteHop']
_ROUTEHINT = DESCRIPTOR.message_types_by_name['Routehint']
_ROUTEHINTLIST = DESCRIPTOR.message_types_by_name['RoutehintList']
_TLVENTRY = DESCRIPTOR.message_types_by_name['TlvEntry']
_TLVSTREAM = DESCRIPTOR.message_types_by_name['TlvStream']
Amount = _reflection.GeneratedProtocolMessageType('Amount', (_message.Message,), {
  'DESCRIPTOR' : _AMOUNT,
  '__module__' : 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cln.Amount)
  })
_sym_db.RegisterMessage(Amount)

AmountOrAll = _reflection.GeneratedProtocolMessageType('AmountOrAll', (_message.Message,), {
  'DESCRIPTOR' : _AMOUNTORALL,
  '__module__' : 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cln.AmountOrAll)
  })
_sym_db.RegisterMessage(AmountOrAll)

AmountOrAny = _reflection.GeneratedProtocolMessageType('AmountOrAny', (_message.Message,), {
  'DESCRIPTOR' : _AMOUNTORANY,
  '__module__' : 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cln.AmountOrAny)
  })
_sym_db.RegisterMessage(AmountOrAny)

ChannelStateChangeCause = _reflection.GeneratedProtocolMessageType('ChannelStateChangeCause', (_message.Message,), {
  'DESCRIPTOR' : _CHANNELSTATECHANGECAUSE,
  '__module__' : 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cln.ChannelStateChangeCause)
  })
_sym_db.RegisterMessage(ChannelStateChangeCause)

Outpoint = _reflection.GeneratedProtocolMessageType('Outpoint', (_message.Message,), {
  'DESCRIPTOR' : _OUTPOINT,
  '__module__' : 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cln.Outpoint)
  })
_sym_db.RegisterMessage(Outpoint)

Feerate = _reflection.GeneratedProtocolMessageType('Feerate', (_message.Message,), {
  'DESCRIPTOR' : _FEERATE,
  '__module__' : 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cln.Feerate)
  })
_sym_db.RegisterMessage(Feerate)

OutputDesc = _reflection.GeneratedProtocolMessageType('OutputDesc', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTDESC,
  '__module__' : 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cln.OutputDesc)
  })
_sym_db.RegisterMessage(OutputDesc)

RouteHop = _reflection.GeneratedProtocolMessageType('RouteHop', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEHOP,
  '__module__' : 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cln.RouteHop)
  })
_sym_db.RegisterMessage(RouteHop)

Routehint = _reflection.GeneratedProtocolMessageType('Routehint', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEHINT,
  '__module__' : 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cln.Routehint)
  })
_sym_db.RegisterMessage(Routehint)

RoutehintList = _reflection.GeneratedProtocolMessageType('RoutehintList', (_message.Message,), {
  'DESCRIPTOR' : _ROUTEHINTLIST,
  '__module__' : 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cln.RoutehintList)
  })
_sym_db.RegisterMessage(RoutehintList)

TlvEntry = _reflection.GeneratedProtocolMessageType('TlvEntry', (_message.Message,), {
  'DESCRIPTOR' : _TLVENTRY,
  '__module__' : 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cln.TlvEntry)
  })
_sym_db.RegisterMessage(TlvEntry)

TlvStream = _reflection.GeneratedProtocolMessageType('TlvStream', (_message.Message,), {
  'DESCRIPTOR' : _TLVSTREAM,
  '__module__' : 'primitives_pb2'
  # @@protoc_insertion_point(class_scope:cln.TlvStream)
  })
_sym_db.RegisterMessage(TlvStream)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHANNELSIDE._serialized_start=718
  _CHANNELSIDE._serialized_end=754
  _CHANNELSTATE._serialized_start=757
  _CHANNELSTATE._serialized_end=1017
  _HTLCSTATE._serialized_start=1020
  _HTLCSTATE._serialized_end=1286
  _AMOUNT._serialized_start=25
  _AMOUNT._serialized_end=47
  _AMOUNTORALL._serialized_start=49
  _AMOUNTORALL._serialized_end=117
  _AMOUNTORANY._serialized_start=119
  _AMOUNTORANY._serialized_end=187
  _CHANNELSTATECHANGECAUSE._serialized_start=189
  _CHANNELSTATECHANGECAUSE._serialized_end=214
  _OUTPOINT._serialized_start=216
  _OUTPOINT._serialized_end=256
  _FEERATE._serialized_start=258
  _FEERATE._serialized_end=362
  _OUTPUTDESC._serialized_start=364
  _OUTPUTDESC._serialized_end=422
  _ROUTEHOP._serialized_start=424
  _ROUTEHOP._serialized_end=540
  _ROUTEHINT._serialized_start=542
  _ROUTEHINT._serialized_end=582
  _ROUTEHINTLIST._serialized_start=584
  _ROUTEHINTLIST._serialized_end=630
  _TLVENTRY._serialized_start=632
  _TLVENTRY._serialized_end=671
  _TLVSTREAM._serialized_start=673
  _TLVSTREAM._serialized_end=716
# @@protoc_insertion_point(module_scope)
