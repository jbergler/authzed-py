"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import authzed.api.v1alpha1.watchresources_service_pb2
import collections.abc
import grpc

class WatchResourcesServiceStub:
    """WatchResourcesService is used to receive a stream of updates for resources of a
    specific (resource type, permission, subject) combination.
    """

    def __init__(self, channel: grpc.Channel) -> None: ...
    WatchResources: grpc.UnaryStreamMultiCallable[
        authzed.api.v1alpha1.watchresources_service_pb2.WatchResourcesRequest,
        authzed.api.v1alpha1.watchresources_service_pb2.WatchResourcesResponse,
    ]
    """WatchResources initiates a watch for permission changes for the provided
    (resource type, permission, subject) pair.
    """

class WatchResourcesServiceServicer(metaclass=abc.ABCMeta):
    """WatchResourcesService is used to receive a stream of updates for resources of a
    specific (resource type, permission, subject) combination.
    """

    @abc.abstractmethod
    def WatchResources(
        self,
        request: authzed.api.v1alpha1.watchresources_service_pb2.WatchResourcesRequest,
        context: grpc.ServicerContext,
    ) -> collections.abc.Iterator[authzed.api.v1alpha1.watchresources_service_pb2.WatchResourcesResponse]:
        """WatchResources initiates a watch for permission changes for the provided
        (resource type, permission, subject) pair.
        """

def add_WatchResourcesServiceServicer_to_server(servicer: WatchResourcesServiceServicer, server: grpc.Server) -> None: ...
