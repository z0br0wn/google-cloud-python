# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/automl_v1beta1/proto/text.proto

import sys

_b = sys.version_info[0] < 3 and (lambda x: x) or (lambda x: x.encode("latin1"))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.cloud.automl_v1beta1.proto import (
    classification_pb2 as google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2,
)


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/automl_v1beta1/proto/text.proto",
    package="google.cloud.automl.v1beta1",
    syntax="proto3",
    serialized_pb=_b(
        '\n,google/cloud/automl_v1beta1/proto/text.proto\x12\x1bgoogle.cloud.automl.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x36google/cloud/automl_v1beta1/proto/classification.proto"q\n!TextClassificationDatasetMetadata\x12L\n\x13\x63lassification_type\x18\x01 \x01(\x0e\x32/.google.cloud.automl.v1beta1.ClassificationType"!\n\x1fTextClassificationModelMetadataB\x8f\x01\n\x1f\x63om.google.cloud.automl.v1beta1B\tTextProtoP\x01ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\xca\x02\x1bGoogle\\Cloud\\AutoMl\\V1beta1b\x06proto3'
    ),
    dependencies=[
        google_dot_api_dot_annotations__pb2.DESCRIPTOR,
        google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2.DESCRIPTOR,
    ],
)


_TEXTCLASSIFICATIONDATASETMETADATA = _descriptor.Descriptor(
    name="TextClassificationDatasetMetadata",
    full_name="google.cloud.automl.v1beta1.TextClassificationDatasetMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="classification_type",
            full_name="google.cloud.automl.v1beta1.TextClassificationDatasetMetadata.classification_type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            options=None,
            file=DESCRIPTOR,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=163,
    serialized_end=276,
)


_TEXTCLASSIFICATIONMODELMETADATA = _descriptor.Descriptor(
    name="TextClassificationModelMetadata",
    full_name="google.cloud.automl.v1beta1.TextClassificationModelMetadata",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[],
    extensions=[],
    nested_types=[],
    enum_types=[],
    options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=278,
    serialized_end=311,
)

_TEXTCLASSIFICATIONDATASETMETADATA.fields_by_name[
    "classification_type"
].enum_type = (
    google_dot_cloud_dot_automl__v1beta1_dot_proto_dot_classification__pb2._CLASSIFICATIONTYPE
)
DESCRIPTOR.message_types_by_name[
    "TextClassificationDatasetMetadata"
] = _TEXTCLASSIFICATIONDATASETMETADATA
DESCRIPTOR.message_types_by_name[
    "TextClassificationModelMetadata"
] = _TEXTCLASSIFICATIONMODELMETADATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TextClassificationDatasetMetadata = _reflection.GeneratedProtocolMessageType(
    "TextClassificationDatasetMetadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TEXTCLASSIFICATIONDATASETMETADATA,
        __module__="google.cloud.automl_v1beta1.proto.text_pb2",
        __doc__="""Dataset metadata for classification.
  
  
  Attributes:
      classification_type:
          Required. Type of the classification problem.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextClassificationDatasetMetadata)
    ),
)
_sym_db.RegisterMessage(TextClassificationDatasetMetadata)

TextClassificationModelMetadata = _reflection.GeneratedProtocolMessageType(
    "TextClassificationModelMetadata",
    (_message.Message,),
    dict(
        DESCRIPTOR=_TEXTCLASSIFICATIONMODELMETADATA,
        __module__="google.cloud.automl_v1beta1.proto.text_pb2",
        __doc__="""Model metadata that is specific to text classification.
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.automl.v1beta1.TextClassificationModelMetadata)
    ),
)
_sym_db.RegisterMessage(TextClassificationModelMetadata)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(
    descriptor_pb2.FileOptions(),
    _b(
        "\n\037com.google.cloud.automl.v1beta1B\tTextProtoP\001ZAgoogle.golang.org/genproto/googleapis/cloud/automl/v1beta1;automl\312\002\033Google\\Cloud\\AutoMl\\V1beta1"
    ),
)
# @@protoc_insertion_point(module_scope)
