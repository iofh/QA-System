"""Generated message classes for cloudasset version v1p1beta1.

The cloud asset API manages the history and inventory of cloud resources.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from apitools.base.protorpclite import messages as _messages
from apitools.base.py import encoding


package = 'cloudasset'


class AuditConfig(_messages.Message):
  r"""Specifies the audit configuration for a service. The configuration
  determines which permission types are logged, and what identities, if any,
  are exempted from logging. An AuditConfig must have one or more
  AuditLogConfigs.  If there are AuditConfigs for both `allServices` and a
  specific service, the union of the two AuditConfigs is used for that
  service: the log_types specified in each AuditConfig are enabled, and the
  exempted_members in each AuditLogConfig are exempted.  Example Policy with
  multiple AuditConfigs:      {       "audit_configs": [         {
  "service": "allServices"           "audit_log_configs": [             {
  "log_type": "DATA_READ",               "exempted_members": [
  "user:jose@example.com"               ]             },             {
  "log_type": "DATA_WRITE",             },             {
  "log_type": "ADMIN_READ",             }           ]         },         {
  "service": "sampleservice.googleapis.com"           "audit_log_configs": [
  {               "log_type": "DATA_READ",             },             {
  "log_type": "DATA_WRITE",               "exempted_members": [
  "user:aliya@example.com"               ]             }           ]         }
  ]     }  For sampleservice, this policy enables DATA_READ, DATA_WRITE and
  ADMIN_READ logging. It also exempts jose@example.com from DATA_READ logging,
  and aliya@example.com from DATA_WRITE logging.

  Fields:
    auditLogConfigs: The configuration for logging of each type of permission.
    service: Specifies a service that will be enabled for audit logging. For
      example, `storage.googleapis.com`, `cloudsql.googleapis.com`.
      `allServices` is a special value that covers all services.
  """

  auditLogConfigs = _messages.MessageField('AuditLogConfig', 1, repeated=True)
  service = _messages.StringField(2)


class AuditLogConfig(_messages.Message):
  r"""Provides the configuration for logging a type of permissions. Example:
  {       "audit_log_configs": [         {           "log_type": "DATA_READ",
  "exempted_members": [             "user:jose@example.com"           ]
  },         {           "log_type": "DATA_WRITE",         }       ]     }
  This enables 'DATA_READ' and 'DATA_WRITE' logging, while exempting
  jose@example.com from DATA_READ logging.

  Enums:
    LogTypeValueValuesEnum: The log type that this config enables.

  Fields:
    exemptedMembers: Specifies the identities that do not cause logging for
      this type of permission. Follows the same format of Binding.members.
    logType: The log type that this config enables.
  """

  class LogTypeValueValuesEnum(_messages.Enum):
    r"""The log type that this config enables.

    Values:
      LOG_TYPE_UNSPECIFIED: Default case. Should never be this.
      ADMIN_READ: Admin reads. Example: CloudIAM getIamPolicy
      DATA_WRITE: Data writes. Example: CloudSQL Users create
      DATA_READ: Data reads. Example: CloudSQL Users list
    """
    LOG_TYPE_UNSPECIFIED = 0
    ADMIN_READ = 1
    DATA_WRITE = 2
    DATA_READ = 3

  exemptedMembers = _messages.StringField(1, repeated=True)
  logType = _messages.EnumField('LogTypeValueValuesEnum', 2)


class Binding(_messages.Message):
  r"""Associates `members` with a `role`.

  Fields:
    condition: The condition that is associated with this binding. NOTE: An
      unsatisfied condition will not allow user access via current binding.
      Different bindings, including their conditions, are examined
      independently.
    members: Specifies the identities requesting access for a Cloud Platform
      resource. `members` can have the following values:  * `allUsers`: A
      special identifier that represents anyone who is    on the internet;
      with or without a Google account.  * `allAuthenticatedUsers`: A special
      identifier that represents anyone    who is authenticated with a Google
      account or a service account.  * `user:{emailid}`: An email address that
      represents a specific Google    account. For example,
      `alice@example.com` .   * `serviceAccount:{emailid}`: An email address
      that represents a service    account. For example, `my-other-
      app@appspot.gserviceaccount.com`.  * `group:{emailid}`: An email address
      that represents a Google group.    For example, `admins@example.com`.  *
      `deleted:user:{emailid}?uid={uniqueid}`: An email address (plus unique
      identifier) representing a user that has been recently deleted. For
      example, `alice@example.com?uid=123456789012345678901`. If the user is
      recovered, this value reverts to `user:{emailid}` and the recovered user
      retains the role in the binding.  *
      `deleted:serviceAccount:{emailid}?uid={uniqueid}`: An email address
      (plus    unique identifier) representing a service account that has been
      recently    deleted. For example,    `my-other-
      app@appspot.gserviceaccount.com?uid=123456789012345678901`.    If the
      service account is undeleted, this value reverts to
      `serviceAccount:{emailid}` and the undeleted service account retains the
      role in the binding.  * `deleted:group:{emailid}?uid={uniqueid}`: An
      email address (plus unique    identifier) representing a Google group
      that has been recently    deleted. For example,
      `admins@example.com?uid=123456789012345678901`. If    the group is
      recovered, this value reverts to `group:{emailid}` and the    recovered
      group retains the role in the binding.   * `domain:{domain}`: The G
      Suite domain (primary) that represents all the    users of that domain.
      For example, `google.com` or `example.com`.
    role: Role that is assigned to `members`. For example, `roles/viewer`,
      `roles/editor`, or `roles/owner`.
  """

  condition = _messages.MessageField('Expr', 1)
  members = _messages.StringField(2, repeated=True)
  role = _messages.StringField(3)


class CloudassetIamPoliciesSearchAllRequest(_messages.Message):
  r"""A CloudassetIamPoliciesSearchAllRequest object.

  Fields:
    pageSize: Optional. The page size for search result pagination. Page size
      is capped at 500 even if a larger value is given. If set to zero, server
      will pick an appropriate default. Returned results may be fewer than
      requested. When this happens, there could be more results as long as
      `next_page_token` is returned.
    pageToken: Optional. If present, retrieve the next batch of results from
      the preceding call to this method. `page_token` must be the value of
      `next_page_token` from the previous response. The values of all other
      method parameters must be identical to those in the previous call.
    query: Optional. The query statement. Examples: *
      "policy:myuser@mydomain.com" * "policy:(myuser@mydomain.com viewer)"
    scope: Required. The relative name of an asset. The search is limited to
      the resources within the `scope`. The allowed value must be: *
      Organization number (such as "organizations/123") * Folder number(such
      as "folders/1234") * Project number (such as "projects/12345") * Project
      id (such as "projects/abc")
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  query = _messages.StringField(3)
  scope = _messages.StringField(4, required=True)


class CloudassetIamPoliciesSearchRequest(_messages.Message):
  r"""A CloudassetIamPoliciesSearchRequest object.

  Fields:
    pageSize: Optional. The page size for search result pagination. Page size
      is capped at 500 even if a larger value is given. If set to zero, server
      will pick an appropriate default. Returned results may be fewer than
      requested. When this happens, there could be more results as long as
      `next_page_token` is returned.
    pageToken: Optional. If present, retrieve the next batch of results from
      the preceding call to this method. `page_token` must be the value of
      `next_page_token` from the previous response. The values of all other
      method parameters must be identical to those in the previous call.
    query: Optional. The query statement. Examples: *
      "policy:myuser@mydomain.com" * "policy:(myuser@mydomain.com viewer)"
    scope: Required. The relative name of an asset. The search is limited to
      the resources within the `scope`. The allowed value must be: *
      Organization number (such as "organizations/123") * Folder number(such
      as "folders/1234") * Project number (such as "projects/12345") * Project
      id (such as "projects/abc")
  """

  pageSize = _messages.IntegerField(1, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(2)
  query = _messages.StringField(3)
  scope = _messages.StringField(4)


class CloudassetResourcesSearchAllRequest(_messages.Message):
  r"""A CloudassetResourcesSearchAllRequest object.

  Fields:
    assetTypes: Optional. A list of asset types that this request searches
      for. If empty, it will search all the supported asset types.
    orderBy: Optional. A comma separated list of fields specifying the sorting
      order of the results. The default order is ascending. Add " desc" after
      the field name to indicate descending order. Redundant space characters
      are ignored. For example, "  foo ,  bar  desc  ".
    pageSize: Optional. The page size for search result pagination. Page size
      is capped at 500 even if a larger value is given. If set to zero, server
      will pick an appropriate default. Returned results may be fewer than
      requested. When this happens, there could be more results as long as
      `next_page_token` is returned.
    pageToken: Optional. If present, then retrieve the next batch of results
      from the preceding call to this method.  `page_token` must be the value
      of `next_page_token` from the previous response. The values of all other
      method parameters, must be identical to those in the previous call.
    query: Optional. The query statement.
    scope: Required. The relative name of an asset. The search is limited to
      the resources within the `scope`. The allowed value must be: *
      Organization number (such as "organizations/123") * Folder number(such
      as "folders/1234") * Project number (such as "projects/12345") * Project
      id (such as "projects/abc")
  """

  assetTypes = _messages.StringField(1, repeated=True)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  query = _messages.StringField(5)
  scope = _messages.StringField(6, required=True)


class CloudassetResourcesSearchRequest(_messages.Message):
  r"""A CloudassetResourcesSearchRequest object.

  Fields:
    assetTypes: Optional. A list of asset types that this request searches
      for. If empty, it will search all the supported asset types.
    orderBy: Optional. A comma separated list of fields specifying the sorting
      order of the results. The default order is ascending. Add " desc" after
      the field name to indicate descending order. Redundant space characters
      are ignored. For example, "  foo ,  bar  desc  ".
    pageSize: Optional. The page size for search result pagination. Page size
      is capped at 500 even if a larger value is given. If set to zero, server
      will pick an appropriate default. Returned results may be fewer than
      requested. When this happens, there could be more results as long as
      `next_page_token` is returned.
    pageToken: Optional. If present, then retrieve the next batch of results
      from the preceding call to this method. `page_token` must be the value
      of `next_page_token` from the previous response. The values of all other
      method parameters, must be identical to those in the previous call.
    query: Optional. The query statement.
    scope: Required. The relative name of an asset. The search is limited to
      the resources within the `scope`. The allowed value must be: *
      Organization number (such as "organizations/123") * Folder number(such
      as "folders/1234") * Project number (such as "projects/12345") * Project
      id (such as "projects/abc")
  """

  assetTypes = _messages.StringField(1, repeated=True)
  orderBy = _messages.StringField(2)
  pageSize = _messages.IntegerField(3, variant=_messages.Variant.INT32)
  pageToken = _messages.StringField(4)
  query = _messages.StringField(5)
  scope = _messages.StringField(6)


class Explanation(_messages.Message):
  r"""Explanation about the IAM policy search result.

  Messages:
    MatchedPermissionsValue: The map from roles to their included permission
      matching the permission query (e.g. containing
      `policy.role.permissions:`). A sample role string:
      "roles/compute.instanceAdmin". The roles can also be found in the
      returned `policy` bindings. Note that the map is populated only if
      requesting with a permission query.

  Fields:
    matchedPermissions: The map from roles to their included permission
      matching the permission query (e.g. containing
      `policy.role.permissions:`). A sample role string:
      "roles/compute.instanceAdmin". The roles can also be found in the
      returned `policy` bindings. Note that the map is populated only if
      requesting with a permission query.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MatchedPermissionsValue(_messages.Message):
    r"""The map from roles to their included permission matching the
    permission query (e.g. containing `policy.role.permissions:`). A sample
    role string: "roles/compute.instanceAdmin". The roles can also be found in
    the returned `policy` bindings. Note that the map is populated only if
    requesting with a permission query.

    Messages:
      AdditionalProperty: An additional property for a MatchedPermissionsValue
        object.

    Fields:
      additionalProperties: Additional properties of type
        MatchedPermissionsValue
    """

    class AdditionalProperty(_messages.Message):
      r"""An additional property for a MatchedPermissionsValue object.

      Fields:
        key: Name of the additional property.
        value: A Permissions attribute.
      """

      key = _messages.StringField(1)
      value = _messages.MessageField('Permissions', 2)

    additionalProperties = _messages.MessageField('AdditionalProperty', 1, repeated=True)

  matchedPermissions = _messages.MessageField('MatchedPermissionsValue', 1)


class Expr(_messages.Message):
  r"""Represents a textual expression in the Common Expression Language (CEL)
  syntax. CEL is a C-like expression language. The syntax and semantics of CEL
  are documented at https://github.com/google/cel-spec.  Example (Comparison):
  title: "Summary size limit"     description: "Determines if a summary is
  less than 100 chars"     expression: "document.summary.size() < 100"
  Example (Equality):      title: "Requestor is owner"     description:
  "Determines if requestor is the document owner"     expression:
  "document.owner == request.auth.claims.email"  Example (Logic):      title:
  "Public documents"     description: "Determine whether the document should
  be publicly visible"     expression: "document.type != 'private' &&
  document.type != 'internal'"  Example (Data Manipulation):      title:
  "Notification string"     description: "Create a notification string with a
  timestamp."     expression: "'New message received at ' +
  string(document.create_time)"  The exact variables and functions that may be
  referenced within an expression are determined by the service that evaluates
  it. See the service documentation for additional information.

  Fields:
    description: Optional. Description of the expression. This is a longer
      text which describes the expression, e.g. when hovered over it in a UI.
    expression: Textual representation of an expression in Common Expression
      Language syntax.
    location: Optional. String indicating the location of the expression for
      error reporting, e.g. a file name and a position in the file.
    title: Optional. Title for the expression, i.e. a short string describing
      its purpose. This can be used e.g. in UIs which allow to enter the
      expression.
  """

  description = _messages.StringField(1)
  expression = _messages.StringField(2)
  location = _messages.StringField(3)
  title = _messages.StringField(4)


class IamPolicySearchResult(_messages.Message):
  r"""The result for a IAM Policy search.

  Fields:
    explanation: Explanation about the IAM policy search result. It contains
      additional information to explain why the search result matches the
      query.
    policy: The IAM policy directly set on the given resource. Note that the
      original IAM policy can contain multiple bindings. This only contains
      the bindings that match the given query. For queries that don't contain
      a constrain on policies (e.g. an empty query), this contains all the
      bindings.
    project: The project that the associated GCP resource belongs to, in the
      form of `projects/{project_number}`. If an IAM policy is set on a
      resource (like VM instance, Cloud Storage bucket), the project field
      will indicate the project that contains the resource. If an IAM policy
      is set on a folder or orgnization, the project field will be empty.
    resource: The [full resource name](https://cloud.google.com/apis/design/re
      source_names#full_resource_name) of the resource associated with this
      IAM policy.
  """

  explanation = _messages.MessageField('Explanation', 1)
  policy = _messages.MessageField('Policy', 2)
  project = _messages.StringField(3)
  resource = _messages.StringField(4)


class Permissions(_messages.Message):
  r"""IAM permissions

  Fields:
    permissions: A list of permissions. A sample permission string:
      "compute.disk.get".
  """

  permissions = _messages.StringField(1, repeated=True)


class Policy(_messages.Message):
  r"""An Identity and Access Management (IAM) policy, which specifies access
  controls for Google Cloud resources.   A `Policy` is a collection of
  `bindings`. A `binding` binds one or more `members` to a single `role`.
  Members can be user accounts, service accounts, Google groups, and domains
  (such as G Suite). A `role` is a named list of permissions; each `role` can
  be an IAM predefined role or a user-created custom role.  Optionally, a
  `binding` can specify a `condition`, which is a logical expression that
  allows access to a resource only if the expression evaluates to `true`. A
  condition can add constraints based on attributes of the request, the
  resource, or both.  **JSON example:**      {       "bindings": [         {
  "role": "roles/resourcemanager.organizationAdmin",           "members": [
  "user:mike@example.com",             "group:admins@example.com",
  "domain:google.com",             "serviceAccount:my-project-
  id@appspot.gserviceaccount.com"           ]         },         {
  "role": "roles/resourcemanager.organizationViewer",           "members":
  ["user:eve@example.com"],           "condition": {             "title":
  "expirable access",             "description": "Does not grant access after
  Sep 2020",             "expression": "request.time <
  timestamp('2020-10-01T00:00:00.000Z')",           }         }       ],
  "etag": "BwWWja0YfJA=",       "version": 3     }  **YAML example:**
  bindings:     - members:       - user:mike@example.com       -
  group:admins@example.com       - domain:google.com       -
  serviceAccount:my-project-id@appspot.gserviceaccount.com       role:
  roles/resourcemanager.organizationAdmin     - members:       -
  user:eve@example.com       role: roles/resourcemanager.organizationViewer
  condition:         title: expirable access         description: Does not
  grant access after Sep 2020         expression: request.time <
  timestamp('2020-10-01T00:00:00.000Z')     - etag: BwWWja0YfJA=     -
  version: 3  For a description of IAM and its features, see the [IAM
  documentation](https://cloud.google.com/iam/docs/).

  Fields:
    auditConfigs: Specifies cloud audit logging configuration for this policy.
    bindings: Associates a list of `members` to a `role`. Optionally, may
      specify a `condition` that determines how and when the `bindings` are
      applied. Each of the `bindings` must contain at least one member.
    etag: `etag` is used for optimistic concurrency control as a way to help
      prevent simultaneous updates of a policy from overwriting each other. It
      is strongly suggested that systems make use of the `etag` in the read-
      modify-write cycle to perform policy updates in order to avoid race
      conditions: An `etag` is returned in the response to `getIamPolicy`, and
      systems are expected to put that etag in the request to `setIamPolicy`
      to ensure that their change will be applied to the same version of the
      policy.  **Important:** If you use IAM Conditions, you must include the
      `etag` field whenever you call `setIamPolicy`. If you omit this field,
      then IAM allows you to overwrite a version `3` policy with a version `1`
      policy, and all of the conditions in the version `3` policy are lost.
    version: Specifies the format of the policy.  Valid values are `0`, `1`,
      and `3`. Requests that specify an invalid value are rejected.  Any
      operation that affects conditional role bindings must specify version
      `3`. This requirement applies to the following operations:  * Getting a
      policy that includes a conditional role binding * Adding a conditional
      role binding to a policy * Changing a conditional role binding in a
      policy * Removing any role binding, with or without a condition, from a
      policy   that includes conditions  **Important:** If you use IAM
      Conditions, you must include the `etag` field whenever you call
      `setIamPolicy`. If you omit this field, then IAM allows you to overwrite
      a version `3` policy with a version `1` policy, and all of the
      conditions in the version `3` policy are lost.  If a policy does not
      include any conditions, operations on that policy may specify any valid
      version or leave the field unset.
  """

  auditConfigs = _messages.MessageField('AuditConfig', 1, repeated=True)
  bindings = _messages.MessageField('Binding', 2, repeated=True)
  etag = _messages.BytesField(3)
  version = _messages.IntegerField(4, variant=_messages.Variant.INT32)


class SearchAllIamPoliciesResponse(_messages.Message):
  r"""Search all IAM policies response.

  Fields:
    nextPageToken: Set if there are more results than those appearing in this
      response; to get the next set of results, call this method again, using
      this value as the `page_token`.
    results: A list of IamPolicy that match the search query. Related
      information such as the associated resource is returned along with the
      policy.
  """

  nextPageToken = _messages.StringField(1)
  results = _messages.MessageField('IamPolicySearchResult', 2, repeated=True)


class SearchAllResourcesResponse(_messages.Message):
  r"""Search all resources response.

  Fields:
    nextPageToken: If there are more results than those appearing in this
      response, then `next_page_token` is included.  To get the next set of
      results, call this method again using the value of `next_page_token` as
      `page_token`.
    results: A list of resource that match the search query.
  """

  nextPageToken = _messages.StringField(1)
  results = _messages.MessageField('StandardResourceMetadata', 2, repeated=True)


class SearchIamPoliciesResponse(_messages.Message):
  r"""Search IAM policies response.

  Fields:
    nextPageToken: Set if there are more results than those appearing in this
      response; to get the next set of results, call this method again, using
      this value as the `page_token`.
    results: A list of IamPolicy that match the search query. Related
      information such as the associated resource is returned along with the
      policy.
  """

  nextPageToken = _messages.StringField(1)
  results = _messages.MessageField('IamPolicySearchResult', 2, repeated=True)


class SearchResourcesResponse(_messages.Message):
  r"""Search resource response.

  Fields:
    nextPageToken: If there are more results than those appearing in this
      response, then `next_page_token` is included.  To get the next set of
      results, call this method again using the value of `next_page_token` as
      `page_token`.
    results: A list of resource that match the search query.
  """

  nextPageToken = _messages.StringField(1)
  results = _messages.MessageField('StandardResourceMetadata', 2, repeated=True)


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


class StandardResourceMetadata(_messages.Message):
  r"""The standard metadata of a cloud resource.

  Messages:
    LabelsValue: Labels associated with this resource.

  Fields:
    additionalAttributes: Additional searchable attributes of this resource.
      Informational only. The exact set of attributes is subject to change.
      For example: project id, DNS name etc.
    assetType: The type of this resource. For example:
      "compute.googleapis.com/Disk".
    description: One or more paragraphs of text description of this resource.
      Maximum length could be up to 1M bytes.
    displayName: The display name of this resource.
    labels: Labels associated with this resource.
    location: Location can be "global", regional like "us-east1", or zonal
      like "us-west1-b".
    name: The full resource name. For example: `//compute.googleapis.com/proje
      cts/my_project_123/zones/zone1/instances/instance1`. See [Resource Names
      ](https://cloud.google.com/apis/design/resource_names#full_resource_name
      ) for more information.
    networkTags: Network tags associated with this resource. Like labels,
      network tags are a type of annotations used to group GCP resources. See
      [Labelling GCP
      resources](lhttps://cloud.google.com/blog/products/gcp/labelling-and-
      grouping-your-google-cloud-platform-resources) for more information.
    project: The project that this resource belongs to, in the form of
      `projects/{project_number}`.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(_messages.Message):
    r"""Labels associated with this resource.

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

  additionalAttributes = _messages.StringField(1, repeated=True)
  assetType = _messages.StringField(2)
  description = _messages.StringField(3)
  displayName = _messages.StringField(4)
  labels = _messages.MessageField('LabelsValue', 5)
  location = _messages.StringField(6)
  name = _messages.StringField(7)
  networkTags = _messages.StringField(8, repeated=True)
  project = _messages.StringField(9)


encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
