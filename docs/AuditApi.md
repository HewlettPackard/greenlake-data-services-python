# greenlake-data-services.AuditApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**audit_events_get**](AuditApi.md#audit_events_get) | **GET** /api/v1/audit-events | GET audit-events


# **audit_events_get**
> AuditResults audit_events_get(filter=filter, limit=limit, offset=offset, sort=sort, select=select)

GET audit-events

returns the audit events

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.AuditApi(greenlake-data-services.ApiClient(configuration))
filter = 'filter_example' # str | Filter criteria - e.g. state eq Failure and occurredAt gt 2020-09-08T16:51:33Z (optional)
limit = 56 # int | The number of results to return (optional)
offset = 56 # int | The number of results to skip (optional)
sort = 'sort_example' # str | A comma separated list of properties to sort by, followed by a direction  indicator (\"asc\" or \"desc\"). If no direction indicator is specified the  default order is ascending. - e.g. state,version desc. Currently only support sorting by 1 property per request (optional)
select = 'select_example' # str | A list of properties to include in the response. Currently only support returning of all fields. (optional)

try:
    # GET audit-events
    api_response = api_instance.audit_events_get(filter=filter, limit=limit, offset=offset, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

