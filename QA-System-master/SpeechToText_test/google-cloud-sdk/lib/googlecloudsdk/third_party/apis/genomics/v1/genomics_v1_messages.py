"""Generated message classes for genomics version v1.

Uploads, processes, queries, and searches Genomics data in the cloud.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding
from apitools.base.py import extra_types


package = 'genomics'


class CancelOperationRequest(_messages.Message):
  r"""The request message for Operations.CancelOperation."""


class ComputeEngine(_messages.Message):
  r"""Describes a Compute Engine resource that is being managed by a running
  pipeline.

  Fields:
    diskNames: The names of the disks that were created for this pipeline.
    instanceName: The instance on which the operation is running.
    machineType: The machine type of the instance.
    zone: The availability zone in which the instance resides.
  """

  diskNames = _messages.StringField(1, repeated=True)
  instanceName = _messages.StringField(2)
  machineType = _messages.StringField(3)
  zone = _messages.StringField(4)


class ContainerKilledEvent(_messages.Message):
  r"""An event generated when a container is forcibly terminated by the
  worker. Currently, this only occurs when the container outlives the timeout
  specified by the user.

  Fields:
    actionId: The numeric ID of the action that started the container.
  """

  actionId = _messages.IntegerField(1, variant=_messages.Variant.INT32)


class ContainerStartedEvent(_messages.Message):
  r"""An event generated when a container starts.

  Messages:
    PortMappingsValue: The container-to-host port mappings installed for this
      container. This set will contain any ports exposed using the
      `PUBLISH_EXPOSED_PORTS` flag as well as any specified in the `Action`
      definition.

  Fields:
    actionId: The numeric ID of the action that started this container.
    ipAddress: The public IP address that can be used to connect to the
      container. This field is only populated when at least one port mapping
      is present. If the instance was created with a private address, this
      field will be empty even if port mappings exist.
    portMappings: The container-to-host port mappings installed for this
      container. This set will contain any ports exposed using the
      `PUBLISH_EXPOSED_PORTS` flag as well as any specified in the `Action`
      definition.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class PortMappingsValue(_messages.Message):
    r"""The container-to-host port mappings installed for this container. This
    set will contain any ports exposed using the `PUBLISH_EXPOSED_PORTS` flag
    as well as any specified in the `Action` definition.

    Messages:
      AdditionalProperty: An additional property for a PortMappingsValue
        object.

    Fields:
      additionalProperties: Additional properties of type PortMappingsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a PortMappingsValue object.

      Fields:
        key: Name of the additional property.
        value: A integer attribute.
      """

      key = _messages.StringField(1)
      value = _messages.IntegerField(2, variant=_messages.Variant.INT32)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  actionId = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  ipAddress = _messages.StringField(2)
  portMappings = _messages.MessageField('PortMappingsValue', 3)


class ContainerStoppedEvent(_messages.Message):
  r"""An event generated when a container exits.

  Fields:
    actionId: The numeric ID of the action that started this container.
    exitStatus: The exit status of the container.
    stderr: The tail end of any content written to standard error by the
      container. If the content emits large amounts of debugging noise or
      contains sensitive information, you can prevent the content from being
      printed by setting the `DISABLE_STANDARD_ERROR_CAPTURE` flag.  Note that
      only a small amount of the end of the stream is captured here. The
      entire stream is stored in the `/google/logs` directory mounted into
      each action, and can be copied off the machine as described elsewhere.
  """

  actionId = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  exitStatus = _messages.IntegerField(2, variant=_messages.Variant.INT32)
  stderr = _messages.StringField(3)


class DelayedEvent(_messages.Message):
  r"""An event generated whenever a resource limitation or transient error
  delays execution of a pipeline that was otherwise ready to run.

  Fields:
    cause: A textual description of the cause of the delay. The string can
      change without notice because it is often generated by another service
      (such as Compute Engine).
    metrics: If the delay was caused by a resource shortage, this field lists
      the Compute Engine metrics that are preventing this operation from
      running (for example, `CPUS` or `INSTANCES`). If the particular metric
      is not known, a single `UNKNOWN` metric will be present.
  """

  cause = _messages.StringField(1)
  metrics = _messages.StringField(2, repeated=True)


class Empty(_messages.Message):
  r"""A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }  The
  JSON representation for `Empty` is empty JSON object `{}`.
  """



class Event(_messages.Message):
  r"""Carries information about events that occur during pipeline execution.

  Messages:
    DetailsValue: Machine-readable details about the event.

  Fields:
    description: A human-readable description of the event. Note that these
      strings can change at any time without notice. Any application logic
      must use the information in the `details` field.
    details: Machine-readable details about the event.
    timestamp: The time at which the event occurred.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValue(_messages.Message):
    r"""Machine-readable details about the event.

    Messages:
      AdditionalProperty: An additional property for a DetailsValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  description = _messages.StringField(1)
  details = _messages.MessageField('DetailsValue', 2)
  timestamp = _messages.StringField(3)


class FailedEvent(_messages.Message):
  r"""An event generated when the execution of a pipeline has failed. Note
  that other events can continue to occur after this event.

  Enums:
    CodeValueValuesEnum: The Google standard error code that best describes
      this failure.

  Fields:
    cause: The human-readable description of the cause of the failure.
    code: The Google standard error code that best describes this failure.
  """

  class CodeValueValuesEnum(_messages.Enum):
    r"""The Google standard error code that best describes this failure.

    Values:
      OK: Not an error; returned on success  HTTP Mapping: 200 OK
      CANCELLED: The operation was cancelled, typically by the caller.  HTTP
        Mapping: 499 Client Closed Request
      UNKNOWN: Unknown error.  For example, this error may be returned when a
        `Status` value received from another address space belongs to an error
        space that is not known in this address space.  Also errors raised by
        APIs that do not return enough error information may be converted to
        this error.  HTTP Mapping: 500 Internal Server Error
      INVALID_ARGUMENT: The client specified an invalid argument.  Note that
        this differs from `FAILED_PRECONDITION`.  `INVALID_ARGUMENT` indicates
        arguments that are problematic regardless of the state of the system
        (e.g., a malformed file name).  HTTP Mapping: 400 Bad Request
      DEADLINE_EXCEEDED: The deadline expired before the operation could
        complete. For operations that change the state of the system, this
        error may be returned even if the operation has completed
        successfully.  For example, a successful response from a server could
        have been delayed long enough for the deadline to expire.  HTTP
        Mapping: 504 Gateway Timeout
      NOT_FOUND: Some requested entity (e.g., file or directory) was not
        found.  Note to server developers: if a request is denied for an
        entire class of users, such as gradual feature rollout or undocumented
        whitelist, `NOT_FOUND` may be used. If a request is denied for some
        users within a class of users, such as user-based access control,
        `PERMISSION_DENIED` must be used.  HTTP Mapping: 404 Not Found
      ALREADY_EXISTS: The entity that a client attempted to create (e.g., file
        or directory) already exists.  HTTP Mapping: 409 Conflict
      PERMISSION_DENIED: The caller does not have permission to execute the
        specified operation. `PERMISSION_DENIED` must not be used for
        rejections caused by exhausting some resource (use
        `RESOURCE_EXHAUSTED` instead for those errors). `PERMISSION_DENIED`
        must not be used if the caller can not be identified (use
        `UNAUTHENTICATED` instead for those errors). This error code does not
        imply the request is valid or the requested entity exists or satisfies
        other pre-conditions.  HTTP Mapping: 403 Forbidden
      UNAUTHENTICATED: The request does not have valid authentication
        credentials for the operation.  HTTP Mapping: 401 Unauthorized
      RESOURCE_EXHAUSTED: Some resource has been exhausted, perhaps a per-user
        quota, or perhaps the entire file system is out of space.  HTTP
        Mapping: 429 Too Many Requests
      FAILED_PRECONDITION: The operation was rejected because the system is
        not in a state required for the operation's execution.  For example,
        the directory to be deleted is non-empty, an rmdir operation is
        applied to a non-directory, etc.  Service implementors can use the
        following guidelines to decide between `FAILED_PRECONDITION`,
        `ABORTED`, and `UNAVAILABLE`:  (a) Use `UNAVAILABLE` if the client can
        retry just the failing call.  (b) Use `ABORTED` if the client should
        retry at a higher level      (e.g., when a client-specified test-and-
        set fails, indicating the      client should restart a read-modify-
        write sequence).  (c) Use `FAILED_PRECONDITION` if the client should
        not retry until      the system state has been explicitly fixed.
        E.g., if an "rmdir"      fails because the directory is non-empty,
        `FAILED_PRECONDITION`      should be returned since the client should
        not retry unless      the files are deleted from the directory.  HTTP
        Mapping: 400 Bad Request
      ABORTED: The operation was aborted, typically due to a concurrency issue
        such as a sequencer check failure or transaction abort.  See the
        guidelines above for deciding between `FAILED_PRECONDITION`,
        `ABORTED`, and `UNAVAILABLE`.  HTTP Mapping: 409 Conflict
      OUT_OF_RANGE: The operation was attempted past the valid range.  E.g.,
        seeking or reading past end-of-file.  Unlike `INVALID_ARGUMENT`, this
        error indicates a problem that may be fixed if the system state
        changes. For example, a 32-bit file system will generate
        `INVALID_ARGUMENT` if asked to read at an offset that is not in the
        range [0,2^32-1], but it will generate `OUT_OF_RANGE` if asked to read
        from an offset past the current file size.  There is a fair bit of
        overlap between `FAILED_PRECONDITION` and `OUT_OF_RANGE`.  We
        recommend using `OUT_OF_RANGE` (the more specific error) when it
        applies so that callers who are iterating through a space can easily
        look for an `OUT_OF_RANGE` error to detect when they are done.  HTTP
        Mapping: 400 Bad Request
      UNIMPLEMENTED: The operation is not implemented or is not
        supported/enabled in this service.  HTTP Mapping: 501 Not Implemented
      INTERNAL: Internal errors.  This means that some invariants expected by
        the underlying system have been broken.  This error code is reserved
        for serious errors.  HTTP Mapping: 500 Internal Server Error
      UNAVAILABLE: The service is currently unavailable.  This is most likely
        a transient condition, which can be corrected by retrying with a
        backoff. Note that it is not always safe to retry non-idempotent
        operations.  See the guidelines above for deciding between
        `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`.  HTTP Mapping:
        503 Service Unavailable
      DATA_LOSS: Unrecoverable data loss or corruption.  HTTP Mapping: 500
        Internal Server Error
    """
    OK = 0
    CANCELLED = 1
    UNKNOWN = 2
    INVALID_ARGUMENT = 3
    DEADLINE_EXCEEDED = 4
    NOT_FOUND = 5
    ALREADY_EXISTS = 6
    PERMISSION_DENIED = 7
    UNAUTHENTICATED = 8
    RESOURCE_EXHAUSTED = 9
    FAILED_PRECONDITION = 10
    ABORTED = 11
    OUT_OF_RANGE = 12
    UNIMPLEMENTED = 13
    INTERNAL = 14
    UNAVAILABLE = 15
    DATA_LOSS = 16

  cause = _messages.StringField(1)
  code = _messages.EnumField('CodeValueValuesEnum', 2)


class GenomicsOperationsCancelRequest(_messages.Message):
  r"""A GenomicsOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: The name of the operation resource to be cancelled.
  """

  cancelOperationRequest = _messages.MessageField('CancelOperationRequest', 1)
  name = _messages.StringField(2, required=True)


class GenomicsOperationsGetRequest(_messages.Message):
  r"""A GenomicsOperationsGetRequest object.

  Fields:
    name: The name of the operation resource.
  """

  name = _messages.StringField(1, required=True)


class GenomicsOperationsListRequest(_messages.Message):
  r"""A GenomicsOperationsListRequest object.

  Fields:
    filter: A string for filtering Operations. In v2alpha1, the following
      filter fields are supported&#58;  * createTime&#58; The time this job
      was created * events&#58; The set of event (names) that have occurred
      while running   the pipeline.  The &#58; operator can be used to
      determine if a   particular event has occurred. * error&#58; If the
      pipeline is running, this value is NULL.  Once the   pipeline finishes,
      the value is the standard Google error code. * labels.key or labels."key
      with space" where key is a label key. * done&#58; If the pipeline is
      running, this value is false. Once the   pipeline finishes, the value is
      true.  In v1 and v1alpha2, the following filter fields are
      supported&#58;  * projectId&#58; Required. Corresponds to
      OperationMetadata.projectId. * createTime&#58; The time this job was
      created, in seconds from the
      [epoch](http://en.wikipedia.org/wiki/Unix_time). Can use `>=` and/or
      `<=`   operators. * status&#58; Can be `RUNNING`, `SUCCESS`, `FAILURE`,
      or `CANCELED`. Only   one status may be specified. * labels.key where
      key is a label key.  Examples&#58;  * `projectId = my-project AND
      createTime >= 1432140000` * `projectId = my-project AND createTime >=
      1432140000 AND createTime <= 1432150000 AND status = RUNNING` *
      `projectId = my-project AND labels.color = *` * `projectId = my-project
      AND labels.color = red`
    name: The name of the operation's parent resource.
    pageSize: The maximum number of results to return. The maximum value is
      256.
    pageToken: The standard list page token.
  """

  filter = _messages.StringField(1)
  name = _messages.StringField(2, required=True)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)


class ListOperationsResponse(_messages.Message):
  r"""The response message for Operations.ListOperations.

  Fields:
    nextPageToken: The standard List next-page token.
    operations: A list of operations that matches the specified filter in the
      request.
  """

  nextPageToken = _messages.StringField(1)
  operations = _messages.MessageField('Operation', 2, repeated=True)


class Operation(_messages.Message):
  r"""This resource represents a long-running operation that is the result of
  a network API call.

  Messages:
    MetadataValue: An OperationMetadata or Metadata object. This will always
      be returned with the Operation.
    ResponseValue: An Empty object.

  Fields:
    done: If the value is `false`, it means the operation is still in
      progress. If `true`, the operation is completed, and either `error` or
      `response` is available.
    error: The error result of the operation in case of failure or
      cancellation.
    metadata: An OperationMetadata or Metadata object. This will always be
      returned with the Operation.
    name: The server-assigned name, which is only unique within the same
      service that originally returns it. For example&#58;
      `operations/CJHU7Oi_ChDrveSpBRjfuL-qzoWAgEw`
    response: An Empty object.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(_messages.Message):
    r"""An OperationMetadata or Metadata object. This will always be returned
    with the Operation.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(_messages.Message):
    r"""An Empty object.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = _messages.BooleanField(1)
  error = _messages.MessageField('Status', 2)
  metadata = _messages.MessageField('MetadataValue', 3)
  name = _messages.StringField(4)
  response = _messages.MessageField('ResponseValue', 5)


class OperationEvent(_messages.Message):
  r"""An event that occurred during an Operation.

  Fields:
    description: Required description of event.
    endTime: Optional time of when event finished. An event can have a start
      time and no finish time. If an event has a finish time, there must be a
      start time.
    startTime: Optional time of when event started.
  """

  description = _messages.StringField(1)
  endTime = _messages.StringField(2)
  startTime = _messages.StringField(3)


class OperationMetadata(_messages.Message):
  r"""Metadata describing an Operation.

  Messages:
    LabelsValue: Optionally provided by the caller when submitting the request
      that creates the operation.
    RequestValue: The original request that started the operation. Note that
      this will be in current version of the API. If the operation was started
      with v1beta2 API and a GetOperation is performed on v1 API, a v1 request
      will be returned.
    RuntimeMetadataValue: Runtime metadata on this Operation.

  Fields:
    clientId: This field is deprecated. Use `labels` instead. Optionally
      provided by the caller when submitting the request that creates the
      operation.
    createTime: The time at which the job was submitted to the Genomics
      service.
    endTime: The time at which the job stopped running.
    events: Optional event messages that were generated during the job's
      execution. This also contains any warnings that were generated during
      import or export.
    labels: Optionally provided by the caller when submitting the request that
      creates the operation.
    projectId: The Google Cloud Project in which the job is scoped.
    request: The original request that started the operation. Note that this
      will be in current version of the API. If the operation was started with
      v1beta2 API and a GetOperation is performed on v1 API, a v1 request will
      be returned.
    runtimeMetadata: Runtime metadata on this Operation.
    startTime: The time at which the job began to run.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Optionally provided by the caller when submitting the request that
    creates the operation.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = _messages.StringField(1)
      value = _messages.StringField(2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class RequestValue(_messages.Message):
    r"""The original request that started the operation. Note that this will
    be in current version of the API. If the operation was started with
    v1beta2 API and a GetOperation is performed on v1 API, a v1 request will
    be returned.

    Messages:
      AdditionalProperty: An additional property for a RequestValue object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a RequestValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class RuntimeMetadataValue(_messages.Message):
    r"""Runtime metadata on this Operation.

    Messages:
      AdditionalProperty: An additional property for a RuntimeMetadataValue
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a RuntimeMetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  clientId = _messages.StringField(1)
  createTime = _messages.StringField(2)
  endTime = _messages.StringField(3)
  events = _messages.MessageField('OperationEvent', 4, repeated=True)
  labels = _messages.MessageField('LabelsValue', 5)
  projectId = _messages.StringField(6)
  request = _messages.MessageField('RequestValue', 7)
  runtimeMetadata = _messages.MessageField('RuntimeMetadataValue', 8)
  startTime = _messages.StringField(9)


class PullStartedEvent(_messages.Message):
  r"""An event generated when the worker starts pulling an image.

  Fields:
    imageUri: The URI of the image that was pulled.
  """

  imageUri = _messages.StringField(1)


class PullStoppedEvent(_messages.Message):
  r"""An event generated when the worker stops pulling an image.

  Fields:
    imageUri: The URI of the image that was pulled.
  """

  imageUri = _messages.StringField(1)


class RunPipelineResponse(_messages.Message):
  r"""The response to the RunPipeline method, returned in the operation's
  result field on success.
  """



class RuntimeMetadata(_messages.Message):
  r"""Runtime metadata that will be populated in the runtimeMetadata field of
  the Operation associated with a RunPipeline execution.

  Fields:
    computeEngine: Execution information specific to Google Compute Engine.
  """

  computeEngine = _messages.MessageField('ComputeEngine', 1)


class StandardQueryParameters(_messages.Message):
  r"""Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" to include in api
      requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(_messages.Enum):
    r"""Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(_messages.Enum):
    r"""V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = _messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = _messages.StringField(2)
  alt = _messages.EnumField('AltValueValuesEnum', 3, default='json')
  callback = _messages.StringField(4)
  fields = _messages.StringField(5)
  key = _messages.StringField(6)
  oauth_token = _messages.StringField(7)
  prettyPrint = _messages.BooleanField(8, default=True)
  quotaUser = _messages.StringField(9)
  trace = _messages.StringField(10)
  uploadType = _messages.StringField(11)
  upload_protocol = _messages.StringField(12)


class Status(_messages.Message):
  r"""The `Status` type defines a logical error model that is suitable for
  different programming environments, including REST APIs and RPC APIs. It is
  used by [gRPC](https://github.com/grpc). Each `Status` message contains
  three pieces of data: error code, error message, and error details.  You can
  find out more about this error model and how to work with it in the [API
  Design Guide](https://cloud.google.com/apis/design/errors).

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: The status code, which should be an enum value of google.rpc.Code.
    details: A list of messages that carry the error details.  There is a
      common set of message types for APIs to use.
    message: A developer-facing error message, which should be in English. Any
      user-facing error message should be localized and sent in the
      google.rpc.Status.details field, or localized by the client.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(_messages.Message):
    r"""A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Properties of the object. Contains field @type
        with type URL.
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  details = _messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = _messages.StringField(3)


class UnexpectedExitStatusEvent(_messages.Message):
  r"""An event generated when the execution of a container results in a non-
  zero exit status that was not otherwise ignored. Execution will continue,
  but only actions that are flagged as `ALWAYS_RUN` will be executed. Other
  actions will be skipped.

  Fields:
    actionId: The numeric ID of the action that started the container.
    exitStatus: The exit status of the container.
  """

  actionId = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  exitStatus = _messages.IntegerField(2, variant=_messages.Variant.INT32)


class WorkerAssignedEvent(_messages.Message):
  r"""An event generated after a worker VM has been assigned to run the
  pipeline.

  Fields:
    instance: The worker's instance name.
    machineType: The machine type that was assigned for the worker.
    zone: The zone the worker is running in.
  """

  instance = _messages.StringField(1)
  machineType = _messages.StringField(2)
  zone = _messages.StringField(3)


class WorkerReleasedEvent(_messages.Message):
  r"""An event generated when the worker VM that was assigned to the pipeline
  has been released (deleted).

  Fields:
    instance: The worker's instance name.
    zone: The zone the worker was running in.
  """

  instance = _messages.StringField(1)
  zone = _messages.StringField(2)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')