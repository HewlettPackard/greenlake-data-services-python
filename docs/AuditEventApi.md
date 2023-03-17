# greenlake-data-services.AuditEventApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_get_events**](AuditEventApi.md#device_type2_get_events) | **GET** /api/v1/storage-systems/device-type2/{systemId}/events | Get all events of Nimble / Alletra 6K
[**device_type2_get_events_using_event_id**](AuditEventApi.md#device_type2_get_events_using_event_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/events/{eventId} | Get all events of Nimble / Alletra 6K identified by {eventId}


# **device_type2_get_events**
> NimbleEventsList device_type2_get_events(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all events of Nimble / Alletra 6K

Get all events of Nimble / Alletra 6K

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
api_instance = greenlake-data-services.AuditEventApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter Events by Key. (optional)
sort = 'sort_example' # str | oData query to sort Event resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all events of Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_events(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditEventApi->device_type2_get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Events by Key. | [optional] 
 **sort** | **str**| oData query to sort Event resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleEventsList**](NimbleEventsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_events_using_event_id**
> NimbleEventsWithRequestUri device_type2_get_events_using_event_id(system_id, event_id, select=select)

Get all events of Nimble / Alletra 6K identified by {eventId}

Get all events of Nimble / Alletra 6K indentified by {eventId}

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
api_instance = greenlake-data-services.AuditEventApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
event_id = 'event_id_example' # str | ID of the Event. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all events of Nimble / Alletra 6K identified by {eventId}
    api_response = api_instance.device_type2_get_events_using_event_id(system_id, event_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditEventApi->device_type2_get_events_using_event_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **event_id** | **str**| ID of the Event. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleEventsWithRequestUri**](NimbleEventsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

