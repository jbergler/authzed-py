"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class Relationship(google.protobuf.message.Message):
    """Relationship specifies how a resource relates to a subject. Relationships
    form the data for the graph over which all permissions questions are
    answered.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESOURCE_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    SUBJECT_FIELD_NUMBER: builtins.int
    OPTIONAL_CAVEAT_FIELD_NUMBER: builtins.int
    @property
    def resource(self) -> global___ObjectReference:
        """resource is the resource to which the subject is related, in some manner"""
    relation: builtins.str
    """relation is how the resource and subject are related."""
    @property
    def subject(self) -> global___SubjectReference:
        """subject is the subject to which the resource is related, in some manner."""
    @property
    def optional_caveat(self) -> global___ContextualizedCaveat:
        """optional_caveat is a reference to a the caveat that must be enforced over the relationship"""
    def __init__(
        self,
        *,
        resource: global___ObjectReference | None = ...,
        relation: builtins.str = ...,
        subject: global___SubjectReference | None = ...,
        optional_caveat: global___ContextualizedCaveat | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["optional_caveat", b"optional_caveat", "resource", b"resource", "subject", b"subject"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["optional_caveat", b"optional_caveat", "relation", b"relation", "resource", b"resource", "subject", b"subject"]) -> None: ...

global___Relationship = Relationship

class ContextualizedCaveat(google.protobuf.message.Message):
    """*
    ContextualizedCaveat represents a reference to a caveat to be used by caveated relationships.
    The context consists of key-value pairs that will be injected at evaluation time.
    The keys must match the arguments defined on the caveat in the schema.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CAVEAT_NAME_FIELD_NUMBER: builtins.int
    CONTEXT_FIELD_NUMBER: builtins.int
    caveat_name: builtins.str
    """* caveat_name is the name of the caveat expression to use, as defined in the schema *"""
    @property
    def context(self) -> google.protobuf.struct_pb2.Struct:
        """* context consists of any named values that are defined at write time for the caveat expression *"""
    def __init__(
        self,
        *,
        caveat_name: builtins.str = ...,
        context: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["context", b"context"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["caveat_name", b"caveat_name", "context", b"context"]) -> None: ...

global___ContextualizedCaveat = ContextualizedCaveat

class SubjectReference(google.protobuf.message.Message):
    """SubjectReference is used for referring to the subject portion of a
    Relationship. The relation component is optional and is used for defining a
    sub-relation on the subject, e.g. group:123#members
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_FIELD_NUMBER: builtins.int
    OPTIONAL_RELATION_FIELD_NUMBER: builtins.int
    @property
    def object(self) -> global___ObjectReference: ...
    optional_relation: builtins.str
    def __init__(
        self,
        *,
        object: global___ObjectReference | None = ...,
        optional_relation: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["object", b"object"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["object", b"object", "optional_relation", b"optional_relation"]) -> None: ...

global___SubjectReference = SubjectReference

class ObjectReference(google.protobuf.message.Message):
    """ObjectReference is used to refer to a specific object in the system."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OBJECT_ID_FIELD_NUMBER: builtins.int
    object_type: builtins.str
    object_id: builtins.str
    def __init__(
        self,
        *,
        object_type: builtins.str = ...,
        object_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["object_id", b"object_id", "object_type", b"object_type"]) -> None: ...

global___ObjectReference = ObjectReference

class ZedToken(google.protobuf.message.Message):
    """ZedToken is used to provide causality metadata between Write and Check
    requests.

    See the authzed.api.v1.Consistency message for more information.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TOKEN_FIELD_NUMBER: builtins.int
    token: builtins.str
    def __init__(
        self,
        *,
        token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["token", b"token"]) -> None: ...

global___ZedToken = ZedToken

class RelationshipUpdate(google.protobuf.message.Message):
    """RelationshipUpdate is used for mutating a single relationship within the
    service.

    CREATE will create the relationship only if it doesn't exist, and error
    otherwise.

    TOUCH will upsert the relationship, and will not error if it
    already exists.

    DELETE will delete the relationship and error if it doesn't
    exist.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Operation:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _OperationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[RelationshipUpdate._Operation.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        OPERATION_UNSPECIFIED: RelationshipUpdate._Operation.ValueType  # 0
        OPERATION_CREATE: RelationshipUpdate._Operation.ValueType  # 1
        OPERATION_TOUCH: RelationshipUpdate._Operation.ValueType  # 2
        OPERATION_DELETE: RelationshipUpdate._Operation.ValueType  # 3

    class Operation(_Operation, metaclass=_OperationEnumTypeWrapper): ...
    OPERATION_UNSPECIFIED: RelationshipUpdate.Operation.ValueType  # 0
    OPERATION_CREATE: RelationshipUpdate.Operation.ValueType  # 1
    OPERATION_TOUCH: RelationshipUpdate.Operation.ValueType  # 2
    OPERATION_DELETE: RelationshipUpdate.Operation.ValueType  # 3

    OPERATION_FIELD_NUMBER: builtins.int
    RELATIONSHIP_FIELD_NUMBER: builtins.int
    operation: global___RelationshipUpdate.Operation.ValueType
    @property
    def relationship(self) -> global___Relationship: ...
    def __init__(
        self,
        *,
        operation: global___RelationshipUpdate.Operation.ValueType = ...,
        relationship: global___Relationship | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["relationship", b"relationship"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["operation", b"operation", "relationship", b"relationship"]) -> None: ...

global___RelationshipUpdate = RelationshipUpdate

class PermissionRelationshipTree(google.protobuf.message.Message):
    """PermissionRelationshipTree is used for representing a tree of a resource and
    its permission relationships with other objects.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    INTERMEDIATE_FIELD_NUMBER: builtins.int
    LEAF_FIELD_NUMBER: builtins.int
    EXPANDED_OBJECT_FIELD_NUMBER: builtins.int
    EXPANDED_RELATION_FIELD_NUMBER: builtins.int
    @property
    def intermediate(self) -> global___AlgebraicSubjectSet: ...
    @property
    def leaf(self) -> global___DirectSubjectSet: ...
    @property
    def expanded_object(self) -> global___ObjectReference: ...
    expanded_relation: builtins.str
    def __init__(
        self,
        *,
        intermediate: global___AlgebraicSubjectSet | None = ...,
        leaf: global___DirectSubjectSet | None = ...,
        expanded_object: global___ObjectReference | None = ...,
        expanded_relation: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["expanded_object", b"expanded_object", "intermediate", b"intermediate", "leaf", b"leaf", "tree_type", b"tree_type"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["expanded_object", b"expanded_object", "expanded_relation", b"expanded_relation", "intermediate", b"intermediate", "leaf", b"leaf", "tree_type", b"tree_type"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["tree_type", b"tree_type"]) -> typing_extensions.Literal["intermediate", "leaf"] | None: ...

global___PermissionRelationshipTree = PermissionRelationshipTree

class AlgebraicSubjectSet(google.protobuf.message.Message):
    """AlgebraicSubjectSet is a subject set which is computed based on applying the
    specified operation to the operands according to the algebra of sets.

    UNION is a logical set containing the subject members from all operands.

    INTERSECTION is a logical set containing only the subject members which are
    present in all operands.

    EXCLUSION is a logical set containing only the subject members which are
    present in the first operand, and none of the other operands.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Operation:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _OperationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[AlgebraicSubjectSet._Operation.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        OPERATION_UNSPECIFIED: AlgebraicSubjectSet._Operation.ValueType  # 0
        OPERATION_UNION: AlgebraicSubjectSet._Operation.ValueType  # 1
        OPERATION_INTERSECTION: AlgebraicSubjectSet._Operation.ValueType  # 2
        OPERATION_EXCLUSION: AlgebraicSubjectSet._Operation.ValueType  # 3

    class Operation(_Operation, metaclass=_OperationEnumTypeWrapper): ...
    OPERATION_UNSPECIFIED: AlgebraicSubjectSet.Operation.ValueType  # 0
    OPERATION_UNION: AlgebraicSubjectSet.Operation.ValueType  # 1
    OPERATION_INTERSECTION: AlgebraicSubjectSet.Operation.ValueType  # 2
    OPERATION_EXCLUSION: AlgebraicSubjectSet.Operation.ValueType  # 3

    OPERATION_FIELD_NUMBER: builtins.int
    CHILDREN_FIELD_NUMBER: builtins.int
    operation: global___AlgebraicSubjectSet.Operation.ValueType
    @property
    def children(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PermissionRelationshipTree]: ...
    def __init__(
        self,
        *,
        operation: global___AlgebraicSubjectSet.Operation.ValueType = ...,
        children: collections.abc.Iterable[global___PermissionRelationshipTree] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["children", b"children", "operation", b"operation"]) -> None: ...

global___AlgebraicSubjectSet = AlgebraicSubjectSet

class DirectSubjectSet(google.protobuf.message.Message):
    """DirectSubjectSet is a subject set which is simply a collection of subjects."""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SUBJECTS_FIELD_NUMBER: builtins.int
    @property
    def subjects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SubjectReference]: ...
    def __init__(
        self,
        *,
        subjects: collections.abc.Iterable[global___SubjectReference] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["subjects", b"subjects"]) -> None: ...

global___DirectSubjectSet = DirectSubjectSet
