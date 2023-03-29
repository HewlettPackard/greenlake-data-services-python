# greenlake_data_services.AuditApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audit_events_get**](AuditApi.md#audit_events_get) | **GET** /api/v1/audit-events | GET audit-events


# **audit_events_get**
> AuditResults audit_events_get()

GET audit-events

returns the audit events

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import audit_api
from greenlake_data_services.model.audit_internal_server_error import AuditInternalServerError
from greenlake_data_services.model.audit_user_forbidden import AuditUserForbidden
from greenlake_data_services.model.audit_bad_request import AuditBadRequest
from greenlake_data_services.model.audit_results import AuditResults
from greenlake_data_services.model.audit_service_unavailable import AuditServiceUnavailable
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = audit_api.AuditApi(api_client)
    filter = "filter_example" # str | Filter criteria - e.g. state eq Failure and occurredAt gt 2020-09-08T16:51:33Z (optional)
    limit = 1 # int | The number of results to return (optional)
    offset = 1 # int | The number of results to skip (optional)
    sort = "sort_example" # str | A comma separated list of properties to sort by, followed by a direction  indicator (\"asc\" or \"desc\"). If no direction indicator is specified the  default order is ascending. - e.g. state,version desc. Currently only support sorting by 1 property per request (optional)
    select = "select_example" # str | A list of properties to include in the response. Currently only support returning of all fields. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GET audit-events
        api_response = api_instance.audit_events_get(filter=filter, limit=limit, offset=offset, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling AuditApi->audit_events_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filter criteria - e.g. state eq Failure and occurredAt gt 2020-09-08T16:51:33Z | [optional]
 **limit** | **int**| The number of results to return | [optional]
 **offset** | **int**| The number of results to skip | [optional]
 **sort** | **str**| A comma separated list of properties to sort by, followed by a direction  indicator (\&quot;asc\&quot; or \&quot;desc\&quot;). If no direction indicator is specified the  default order is ascending. - e.g. state,version desc. Currently only support sorting by 1 property per request | [optional]
 **select** | **str**| A list of properties to include in the response. Currently only support returning of all fields. | [optional]

### Return type

[**AuditResults**](AuditResults.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | An invalid request was received. |  -  |
**403** | The requesting user was not permitted to access this resource. |  -  |
**500** | An internal error occurred. |  -  |
**503** | Audit or Dependent Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

