# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iteasyfile.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='iteasyfile.proto',
  package='iteasyfile',
  serialized_pb='\n\x10iteasyfile.proto\x12\niteasyfile\"\xd3\x05\n\x0bPkgFileTail\x12\x0f\n\x07version\x18\x01 \x02(\t\x12\x1a\n\x12\x66ilevaildlengthlow\x18\x02 \x02(\x05\x12\x1b\n\x13\x66ilevaildlengthhigh\x18\x03 \x02(\x05\x12\x11\n\tmagic1low\x18\n \x02(\x05\x12\x12\n\nmagic1high\x18\x0b \x02(\x05\x12\x11\n\tmagic2low\x18\x0c \x02(\x05\x12\x12\n\nmagic2high\x18\r \x02(\x05\x12\x18\n\x10keyencrypted1low\x18\x0e \x02(\x05\x12\x19\n\x11keyencrypted1high\x18\x0f \x02(\x05\x12\x18\n\x10keyencrypted2low\x18\x10 \x02(\x05\x12\x19\n\x11keyencrypted2high\x18\x11 \x02(\x05\x12\x15\n\rcompanyid1low\x18\x12 \x02(\x05\x12\x16\n\x0e\x63ompanyid1high\x18\x13 \x02(\x05\x12\x15\n\rcompanyid2low\x18\x14 \x02(\x05\x12\x16\n\x0e\x63ompanyid2high\x18\x15 \x02(\x05\x12\x16\n\x0e\x64\x65partment1low\x18\x16 \x02(\x05\x12\x17\n\x0f\x64\x65partment1high\x18\x17 \x02(\x05\x12\x16\n\x0e\x64\x65partment2low\x18\x18 \x02(\x05\x12\x17\n\x0f\x64\x65partment2high\x18\x19 \x02(\x05\x12\x15\n\rcreatetimelow\x18\x32 \x01(\x05\x12\x16\n\x0e\x63reatetimehigh\x18\x33 \x01(\x05\x12\x19\n\x11lastaccesstimelow\x18\x34 \x01(\x05\x12\x1a\n\x12lastaccesstimehigh\x18\x35 \x01(\x05\x12\x18\n\x10lastwritetimelow\x18\x36 \x01(\x05\x12\x19\n\x11lastwritetimehigh\x18\x37 \x01(\x05\x12\x15\n\rchangetimelow\x18\x38 \x01(\x05\x12\x16\n\x0e\x63hangetimehigh\x18\x39 \x01(\x05\x12\x11\n\tuseridnew\x18\x46 \x01(\t\x12\x14\n\x0cuseridmodify\x18G \x01(\t\x12\x0f\n\x07\x66ilemd5\x18H \x01(\t')




_PKGFILETAIL = _descriptor.Descriptor(
  name='PkgFileTail',
  full_name='iteasyfile.PkgFileTail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='iteasyfile.PkgFileTail.version', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filevaildlengthlow', full_name='iteasyfile.PkgFileTail.filevaildlengthlow', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filevaildlengthhigh', full_name='iteasyfile.PkgFileTail.filevaildlengthhigh', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magic1low', full_name='iteasyfile.PkgFileTail.magic1low', index=3,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magic1high', full_name='iteasyfile.PkgFileTail.magic1high', index=4,
      number=11, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magic2low', full_name='iteasyfile.PkgFileTail.magic2low', index=5,
      number=12, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='magic2high', full_name='iteasyfile.PkgFileTail.magic2high', index=6,
      number=13, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyencrypted1low', full_name='iteasyfile.PkgFileTail.keyencrypted1low', index=7,
      number=14, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyencrypted1high', full_name='iteasyfile.PkgFileTail.keyencrypted1high', index=8,
      number=15, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyencrypted2low', full_name='iteasyfile.PkgFileTail.keyencrypted2low', index=9,
      number=16, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keyencrypted2high', full_name='iteasyfile.PkgFileTail.keyencrypted2high', index=10,
      number=17, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='companyid1low', full_name='iteasyfile.PkgFileTail.companyid1low', index=11,
      number=18, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='companyid1high', full_name='iteasyfile.PkgFileTail.companyid1high', index=12,
      number=19, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='companyid2low', full_name='iteasyfile.PkgFileTail.companyid2low', index=13,
      number=20, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='companyid2high', full_name='iteasyfile.PkgFileTail.companyid2high', index=14,
      number=21, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='department1low', full_name='iteasyfile.PkgFileTail.department1low', index=15,
      number=22, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='department1high', full_name='iteasyfile.PkgFileTail.department1high', index=16,
      number=23, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='department2low', full_name='iteasyfile.PkgFileTail.department2low', index=17,
      number=24, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='department2high', full_name='iteasyfile.PkgFileTail.department2high', index=18,
      number=25, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='createtimelow', full_name='iteasyfile.PkgFileTail.createtimelow', index=19,
      number=50, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='createtimehigh', full_name='iteasyfile.PkgFileTail.createtimehigh', index=20,
      number=51, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastaccesstimelow', full_name='iteasyfile.PkgFileTail.lastaccesstimelow', index=21,
      number=52, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastaccesstimehigh', full_name='iteasyfile.PkgFileTail.lastaccesstimehigh', index=22,
      number=53, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastwritetimelow', full_name='iteasyfile.PkgFileTail.lastwritetimelow', index=23,
      number=54, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lastwritetimehigh', full_name='iteasyfile.PkgFileTail.lastwritetimehigh', index=24,
      number=55, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='changetimelow', full_name='iteasyfile.PkgFileTail.changetimelow', index=25,
      number=56, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='changetimehigh', full_name='iteasyfile.PkgFileTail.changetimehigh', index=26,
      number=57, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='useridnew', full_name='iteasyfile.PkgFileTail.useridnew', index=27,
      number=70, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='useridmodify', full_name='iteasyfile.PkgFileTail.useridmodify', index=28,
      number=71, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filemd5', full_name='iteasyfile.PkgFileTail.filemd5', index=29,
      number=72, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=33,
  serialized_end=756,
)

DESCRIPTOR.message_types_by_name['PkgFileTail'] = _PKGFILETAIL

class PkgFileTail(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PKGFILETAIL

  # @@protoc_insertion_point(class_scope:iteasyfile.PkgFileTail)


# @@protoc_insertion_point(module_scope)
