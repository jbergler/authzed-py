"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import authzed.api.v1.core_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class WatchResourcesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_OBJECT_TYPE_FIELD_NUMBER: builtins.int
    PERMISSION_FIELD_NUMBER: builtins.int
    SUBJECT_OBJECT_TYPE_FIELD_NUMBER: builtins.int
    OPTIONAL_SUBJECT_RELATION_FIELD_NUMBER: builtins.int
    OPTIONAL_START_CURSOR_FIELD_NUMBER: builtins.int
    resource_object_type: typing.Text = ...
    permission: typing.Text = ...
    subject_object_type: typing.Text = ...
    optional_subject_relation: typing.Text = ...

    @property
    def optional_start_cursor(self) -> authzed.api.v1.core_pb2.ZedToken: ...

    def __init__(self,
        *,
        resource_object_type : typing.Text = ...,
        permission : typing.Text = ...,
        subject_object_type : typing.Text = ...,
        optional_subject_relation : typing.Text = ...,
        optional_start_cursor : typing.Optional[authzed.api.v1.core_pb2.ZedToken] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"optional_start_cursor",b"optional_start_cursor"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"optional_start_cursor",b"optional_start_cursor",u"optional_subject_relation",b"optional_subject_relation",u"permission",b"permission",u"resource_object_type",b"resource_object_type",u"subject_object_type",b"subject_object_type"]) -> None: ...
global___WatchResourcesRequest = WatchResourcesRequest

class PermissionUpdate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class Permissionship(metaclass=_Permissionship):
        V = typing.NewType('V', builtins.int)

    PERMISSIONSHIP_UNSPECIFIED = PermissionUpdate.Permissionship.V(0)
    PERMISSIONSHIP_NO_PERMISSION = PermissionUpdate.Permissionship.V(1)
    PERMISSIONSHIP_HAS_PERMISSION = PermissionUpdate.Permissionship.V(2)

    class _Permissionship(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Permissionship.V], builtins.type):  # type: ignore
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        PERMISSIONSHIP_UNSPECIFIED = PermissionUpdate.Permissionship.V(0)
        PERMISSIONSHIP_NO_PERMISSION = PermissionUpdate.Permissionship.V(1)
        PERMISSIONSHIP_HAS_PERMISSION = PermissionUpdate.Permissionship.V(2)

    SUBJECT_FIELD_NUMBER: builtins.int
    RESOURCE_FIELD_NUMBER: builtins.int
    RELATION_FIELD_NUMBER: builtins.int
    UPDATED_PERMISSION_FIELD_NUMBER: builtins.int
    relation: typing.Text = ...
    updated_permission: global___PermissionUpdate.Permissionship.V = ...

    @property
    def subject(self) -> authzed.api.v1.core_pb2.SubjectReference: ...

    @property
    def resource(self) -> authzed.api.v1.core_pb2.ObjectReference: ...

    def __init__(self,
        *,
        subject : typing.Optional[authzed.api.v1.core_pb2.SubjectReference] = ...,
        resource : typing.Optional[authzed.api.v1.core_pb2.ObjectReference] = ...,
        relation : typing.Text = ...,
        updated_permission : global___PermissionUpdate.Permissionship.V = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"resource",b"resource",u"subject",b"subject"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"relation",b"relation",u"resource",b"resource",u"subject",b"subject",u"updated_permission",b"updated_permission"]) -> None: ...
global___PermissionUpdate = PermissionUpdate

class WatchResourcesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATES_FIELD_NUMBER: builtins.int
    CHANGES_THROUGH_FIELD_NUMBER: builtins.int

    @property
    def updates(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PermissionUpdate]: ...

    @property
    def changes_through(self) -> authzed.api.v1.core_pb2.ZedToken: ...

    def __init__(self,
        *,
        updates : typing.Optional[typing.Iterable[global___PermissionUpdate]] = ...,
        changes_through : typing.Optional[authzed.api.v1.core_pb2.ZedToken] = ...,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal[u"changes_through",b"changes_through"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal[u"changes_through",b"changes_through",u"updates",b"updates"]) -> None: ...
global___WatchResourcesResponse = WatchResourcesResponse