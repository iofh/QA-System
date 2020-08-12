"""Generated client library for accesscontextmanager version v1."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.accesscontextmanager.v1 import accesscontextmanager_v1_messages as messages


class AccesscontextmanagerV1(base_api.BaseApiClient):
  """Generated client library for service accesscontextmanager version v1."""

  MESSAGES_MODULE = messages
  BASE_URL = 'https://accesscontextmanager.googleapis.com/'
  MTLS_BASE_URL = 'https://accesscontextmanager.mtls.googleapis.com/'

  _PACKAGE = 'accesscontextmanager'
  _SCOPES = ['https://www.googleapis.com/auth/cloud-platform']
  _VERSION = 'v1'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'google-cloud-sdk'
  _CLIENT_CLASS_NAME = 'AccesscontextmanagerV1'
  _URL_VERSION = 'v1'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None, response_encoding=None):
    """Create a new accesscontextmanager handle."""
    url = url or self.BASE_URL
    super(AccesscontextmanagerV1, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers,
        response_encoding=response_encoding)
    self.accessPolicies_accessLevels = self.AccessPoliciesAccessLevelsService(self)
    self.accessPolicies_servicePerimeters = self.AccessPoliciesServicePerimetersService(self)
    self.accessPolicies = self.AccessPoliciesService(self)
    self.operations = self.OperationsService(self)

  class AccessPoliciesAccessLevelsService(base_api.BaseApiService):
    """Service class for the accessPolicies_accessLevels resource."""

    _NAME = 'accessPolicies_accessLevels'

    def __init__(self, client):
      super(AccesscontextmanagerV1.AccessPoliciesAccessLevelsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an Access Level. The longrunning.
operation from this RPC will have a successful status once the Access
Level has
propagated to long-lasting storage. Access Levels containing
errors will result in an error response for the first error encountered.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessLevelsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/accessLevels',
        http_method='POST',
        method_id='accesscontextmanager.accessPolicies.accessLevels.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/accessLevels',
        request_field='accessLevel',
        request_type_name='AccesscontextmanagerAccessPoliciesAccessLevelsCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an Access Level by resource.
name. The longrunning operation from this RPC will have a successful status
once the Access Level has been removed
from long-lasting storage.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessLevelsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/accessLevels/{accessLevelsId}',
        http_method='DELETE',
        method_id='accesscontextmanager.accessPolicies.accessLevels.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccesscontextmanagerAccessPoliciesAccessLevelsDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an Access Level by resource.
name.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessLevelsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AccessLevel) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/accessLevels/{accessLevelsId}',
        http_method='GET',
        method_id='accesscontextmanager.accessPolicies.accessLevels.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['accessLevelFormat'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccesscontextmanagerAccessPoliciesAccessLevelsGetRequest',
        response_type_name='AccessLevel',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List all Access Levels for an access.
policy.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessLevelsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAccessLevelsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/accessLevels',
        http_method='GET',
        method_id='accesscontextmanager.accessPolicies.accessLevels.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['accessLevelFormat', 'pageSize', 'pageToken'],
        relative_path='v1/{+parent}/accessLevels',
        request_field='',
        request_type_name='AccesscontextmanagerAccessPoliciesAccessLevelsListRequest',
        response_type_name='ListAccessLevelsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an Access Level. The longrunning.
operation from this RPC will have a successful status once the changes to
the Access Level have propagated
to long-lasting storage. Access Levels containing
errors will result in an error response for the first error encountered.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessLevelsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/accessLevels/{accessLevelsId}',
        http_method='PATCH',
        method_id='accesscontextmanager.accessPolicies.accessLevels.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='accessLevel',
        request_type_name='AccesscontextmanagerAccessPoliciesAccessLevelsPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def ReplaceAll(self, request, global_params=None):
      r"""Replace all existing Access Levels in an Access.
Policy with
the Access Levels provided. This
is done atomically. The longrunning operation from this RPC will have a
successful status once all replacements have propagated to long-lasting
storage. Replacements containing errors will result in an error response
for the first error encountered.  Replacement will be cancelled on error,
existing Access Levels will not be
affected. Operation.response field will contain
ReplaceAccessLevelsResponse. Removing Access Levels contained in existing
Service Perimeters will result in
error.

      Args:
        request: (AccesscontextmanagerAccessPoliciesAccessLevelsReplaceAllRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('ReplaceAll')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReplaceAll.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/accessLevels:replaceAll',
        http_method='POST',
        method_id='accesscontextmanager.accessPolicies.accessLevels.replaceAll',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/accessLevels:replaceAll',
        request_field='replaceAccessLevelsRequest',
        request_type_name='AccesscontextmanagerAccessPoliciesAccessLevelsReplaceAllRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class AccessPoliciesServicePerimetersService(base_api.BaseApiService):
    """Service class for the accessPolicies_servicePerimeters resource."""

    _NAME = 'accessPolicies_servicePerimeters'

    def __init__(self, client):
      super(AccesscontextmanagerV1.AccessPoliciesServicePerimetersService, self).__init__(client)
      self._upload_configs = {
          }

    def Commit(self, request, global_params=None):
      r"""Commit the dry-run spec for all the Service Perimeters in an.
Access Policy.
A commit operation on a Service Perimeter involves copying its `spec` field
to that Service Perimeter's `status` field. Only Service Perimeters with
`use_explicit_dry_run_spec` field set to true are affected by a commit
operation. The longrunning operation from this RPC will have a successful
status once the dry-run specs for all the Service Perimeters have been
committed. If a commit fails, it will cause the longrunning operation to
return an error response and the entire commit operation will be cancelled.
When successful, Operation.response field will contain
CommitServicePerimetersResponse. The `dry_run` and the `spec` fields will
be cleared after a successful commit operation.

      Args:
        request: (AccesscontextmanagerAccessPoliciesServicePerimetersCommitRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Commit')
      return self._RunMethod(
          config, request, global_params=global_params)

    Commit.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/servicePerimeters:commit',
        http_method='POST',
        method_id='accesscontextmanager.accessPolicies.servicePerimeters.commit',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/servicePerimeters:commit',
        request_field='commitServicePerimetersRequest',
        request_type_name='AccesscontextmanagerAccessPoliciesServicePerimetersCommitRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Create(self, request, global_params=None):
      r"""Create an Service Perimeter. The.
longrunning operation from this RPC will have a successful status once the
Service Perimeter has
propagated to long-lasting storage. Service Perimeters containing
errors will result in an error response for the first error encountered.

      Args:
        request: (AccesscontextmanagerAccessPoliciesServicePerimetersCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/servicePerimeters',
        http_method='POST',
        method_id='accesscontextmanager.accessPolicies.servicePerimeters.create',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/servicePerimeters',
        request_field='servicePerimeter',
        request_type_name='AccesscontextmanagerAccessPoliciesServicePerimetersCreateRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an Service Perimeter by resource.
name. The longrunning operation from this RPC will have a successful status
once the Service Perimeter has been
removed from long-lasting storage.

      Args:
        request: (AccesscontextmanagerAccessPoliciesServicePerimetersDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/servicePerimeters/{servicePerimetersId}',
        http_method='DELETE',
        method_id='accesscontextmanager.accessPolicies.servicePerimeters.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccesscontextmanagerAccessPoliciesServicePerimetersDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an Service Perimeter by resource.
name.

      Args:
        request: (AccesscontextmanagerAccessPoliciesServicePerimetersGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ServicePerimeter) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/servicePerimeters/{servicePerimetersId}',
        http_method='GET',
        method_id='accesscontextmanager.accessPolicies.servicePerimeters.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccesscontextmanagerAccessPoliciesServicePerimetersGetRequest',
        response_type_name='ServicePerimeter',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List all Service Perimeters for an.
access policy.

      Args:
        request: (AccesscontextmanagerAccessPoliciesServicePerimetersListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListServicePerimetersResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/servicePerimeters',
        http_method='GET',
        method_id='accesscontextmanager.accessPolicies.servicePerimeters.list',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=['pageSize', 'pageToken'],
        relative_path='v1/{+parent}/servicePerimeters',
        request_field='',
        request_type_name='AccesscontextmanagerAccessPoliciesServicePerimetersListRequest',
        response_type_name='ListServicePerimetersResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an Service Perimeter. The.
longrunning operation from this RPC will have a successful status once the
changes to the Service Perimeter have
propagated to long-lasting storage. Service Perimeter containing
errors will result in an error response for the first error encountered.

      Args:
        request: (AccesscontextmanagerAccessPoliciesServicePerimetersPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/servicePerimeters/{servicePerimetersId}',
        http_method='PATCH',
        method_id='accesscontextmanager.accessPolicies.servicePerimeters.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='servicePerimeter',
        request_type_name='AccesscontextmanagerAccessPoliciesServicePerimetersPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def ReplaceAll(self, request, global_params=None):
      r"""Replace all existing Service Perimeters in an.
Access Policy
with the Service Perimeters provided.
This is done atomically. The longrunning operation from this
RPC will have a successful status once all replacements have propagated to
long-lasting storage. Replacements containing errors will result in an
error response for the first error encountered. Replacement will be
cancelled on error, existing Service Perimeters will not be
affected. Operation.response field will contain
ReplaceServicePerimetersResponse.

      Args:
        request: (AccesscontextmanagerAccessPoliciesServicePerimetersReplaceAllRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('ReplaceAll')
      return self._RunMethod(
          config, request, global_params=global_params)

    ReplaceAll.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}/servicePerimeters:replaceAll',
        http_method='POST',
        method_id='accesscontextmanager.accessPolicies.servicePerimeters.replaceAll',
        ordered_params=['parent'],
        path_params=['parent'],
        query_params=[],
        relative_path='v1/{+parent}/servicePerimeters:replaceAll',
        request_field='replaceServicePerimetersRequest',
        request_type_name='AccesscontextmanagerAccessPoliciesServicePerimetersReplaceAllRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class AccessPoliciesService(base_api.BaseApiService):
    """Service class for the accessPolicies resource."""

    _NAME = 'accessPolicies'

    def __init__(self, client):
      super(AccesscontextmanagerV1.AccessPoliciesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      r"""Create an `AccessPolicy`. Fails if this organization already has a.
`AccessPolicy`. The longrunning Operation will have a successful status
once the `AccessPolicy` has propagated to long-lasting storage.
Syntactic and basic semantic errors will be returned in `metadata` as a
BadRequest proto.

      Args:
        request: (AccessPolicy) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method='POST',
        method_id='accesscontextmanager.accessPolicies.create',
        ordered_params=[],
        path_params=[],
        query_params=[],
        relative_path='v1/accessPolicies',
        request_field='<request>',
        request_type_name='AccessPolicy',
        response_type_name='Operation',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Delete an AccessPolicy by resource.
name. The longrunning Operation will have a successful status once the
AccessPolicy
has been removed from long-lasting storage.

      Args:
        request: (AccesscontextmanagerAccessPoliciesDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}',
        http_method='DELETE',
        method_id='accesscontextmanager.accessPolicies.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccesscontextmanagerAccessPoliciesDeleteRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Get an AccessPolicy by name.

      Args:
        request: (AccesscontextmanagerAccessPoliciesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (AccessPolicy) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}',
        http_method='GET',
        method_id='accesscontextmanager.accessPolicies.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccesscontextmanagerAccessPoliciesGetRequest',
        response_type_name='AccessPolicy',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""List all AccessPolicies under a.
container.

      Args:
        request: (AccesscontextmanagerAccessPoliciesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListAccessPoliciesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method='GET',
        method_id='accesscontextmanager.accessPolicies.list',
        ordered_params=[],
        path_params=[],
        query_params=['pageSize', 'pageToken', 'parent'],
        relative_path='v1/accessPolicies',
        request_field='',
        request_type_name='AccesscontextmanagerAccessPoliciesListRequest',
        response_type_name='ListAccessPoliciesResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      r"""Update an AccessPolicy. The.
longrunning Operation from this RPC will have a successful status once the
changes to the AccessPolicy have propagated
to long-lasting storage. Syntactic and basic semantic errors will be
returned in `metadata` as a BadRequest proto.

      Args:
        request: (AccesscontextmanagerAccessPoliciesPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/accessPolicies/{accessPoliciesId}',
        http_method='PATCH',
        method_id='accesscontextmanager.accessPolicies.patch',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['updateMask'],
        relative_path='v1/{+name}',
        request_field='accessPolicy',
        request_type_name='AccesscontextmanagerAccessPoliciesPatchRequest',
        response_type_name='Operation',
        supports_download=False,
    )

  class OperationsService(base_api.BaseApiService):
    """Service class for the operations resource."""

    _NAME = 'operations'

    def __init__(self, client):
      super(AccesscontextmanagerV1.OperationsService, self).__init__(client)
      self._upload_configs = {
          }

    def Cancel(self, request, global_params=None):
      r"""Starts asynchronous cancellation on a long-running operation.  The server.
makes a best effort to cancel the operation, but success is not
guaranteed.  If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.  Clients can use
Operations.GetOperation or
other methods to check whether the cancellation succeeded or whether the
operation completed despite cancellation. On successful cancellation,
the operation is not deleted; instead, it becomes an operation with
an Operation.error value with a google.rpc.Status.code of 1,
corresponding to `Code.CANCELLED`.

      Args:
        request: (AccesscontextmanagerOperationsCancelRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Cancel')
      return self._RunMethod(
          config, request, global_params=global_params)

    Cancel.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/operations/{operationsId}:cancel',
        http_method='POST',
        method_id='accesscontextmanager.operations.cancel',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}:cancel',
        request_field='cancelOperationRequest',
        request_type_name='AccesscontextmanagerOperationsCancelRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Delete(self, request, global_params=None):
      r"""Deletes a long-running operation. This method indicates that the client is.
no longer interested in the operation result. It does not cancel the
operation. If the server doesn't support this method, it returns
`google.rpc.Code.UNIMPLEMENTED`.

      Args:
        request: (AccesscontextmanagerOperationsDeleteRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Empty) The response message.
      """
      config = self.GetMethodConfig('Delete')
      return self._RunMethod(
          config, request, global_params=global_params)

    Delete.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/operations/{operationsId}',
        http_method='DELETE',
        method_id='accesscontextmanager.operations.delete',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccesscontextmanagerOperationsDeleteRequest',
        response_type_name='Empty',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      r"""Gets the latest state of a long-running operation.  Clients can use this.
method to poll the operation result at intervals as recommended by the API
service.

      Args:
        request: (AccesscontextmanagerOperationsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Operation) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/operations/{operationsId}',
        http_method='GET',
        method_id='accesscontextmanager.operations.get',
        ordered_params=['name'],
        path_params=['name'],
        query_params=[],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccesscontextmanagerOperationsGetRequest',
        response_type_name='Operation',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      r"""Lists operations that match the specified filter in the request. If the.
server doesn't support this method, it returns `UNIMPLEMENTED`.

NOTE: the `name` binding allows API services to override the binding
to use different resource name schemes, such as `users/*/operations`. To
override the binding, API services can add a binding such as
`"/v1/{name=users/*}/operations"` to their service configuration.
For backwards compatibility, the default name includes the operations
collection id, however overriding users must ensure the name binding
is the parent resource, without the operations collection id.

      Args:
        request: (AccesscontextmanagerOperationsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListOperationsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        flat_path='v1/operations',
        http_method='GET',
        method_id='accesscontextmanager.operations.list',
        ordered_params=['name'],
        path_params=['name'],
        query_params=['filter', 'pageSize', 'pageToken'],
        relative_path='v1/{+name}',
        request_field='',
        request_type_name='AccesscontextmanagerOperationsListRequest',
        response_type_name='ListOperationsResponse',
        supports_download=False,
    )