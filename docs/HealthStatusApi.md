# greenlake-data-services.HealthStatusApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_get_health_status**](HealthStatusApi.md#device_type2_get_health_status) | **GET** /api/v1/storage-systems/device-type2/{systemId}/health-status | Get details of  Nimble / Alletra 6K health status
[**device_type2_get_health_status_using_health_id**](HealthStatusApi.md#device_type2_get_health_status_using_health_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/health-status/{healthStatusId} | Get details of  Nimble / Alletra 6K health status identified by {healthStatusId}


# **device_type2_get_health_status**
> NimbleHealthStatusList device_type2_get_health_status(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of  Nimble / Alletra 6K health status

Get details of  Nimble / Alletra 6K health status

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
api_instance = greenlake-data-services.HealthStatusApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter health status by Key. (optional)
sort = 'sort_example' # str | oData query to sort health status resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of  Nimble / Alletra 6K health status
    api_response = api_instance.device_type2_get_health_status(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthStatusApi->device_type2_get_health_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter health status by Key. | [optional] 
 **sort** | **str**| oData query to sort health status resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleHealthStatusList**](NimbleHealthStatusList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_health_status_using_health_id**
> NimbleHealthStatusDetailsWithRequestUri device_type2_get_health_status_using_health_id(system_id, health_status_id, select=select)

Get details of  Nimble / Alletra 6K health status identified by {healthStatusId}

Get details of Nimble / Alletra 6K health status identified by {healthStatusId}

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
api_instance = greenlake-data-services.HealthStatusApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
health_status_id = 'health_status_id_example' # str | Identifier of health status. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of  Nimble / Alletra 6K health status identified by {healthStatusId}
    api_response = api_instance.device_type2_get_health_status_using_health_id(system_id, health_status_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthStatusApi->device_type2_get_health_status_using_health_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **health_status_id** | **str**| Identifier of health status. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleHealthStatusDetailsWithRequestUri**](NimbleHealthStatusDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

