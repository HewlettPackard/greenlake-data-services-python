# greenlake-data-services.HostPathsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_get_all_host_paths**](HostPathsApi.md#device_type1_get_all_host_paths) | **GET** /api/v1/storage-systems/device-type1/{systemId}/host-paths | Get details of Primera / Alletra 9K Host Paths
[**device_type1_get_host_paths_by_id**](HostPathsApi.md#device_type1_get_host_paths_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/host-paths/{hostPathId} | Get details of Primera / Alletra 9K Host Path identified by {HostPathId}


# **device_type1_get_all_host_paths**
> PrimeraHostPathList device_type1_get_all_host_paths(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K Host Paths

Get details of Primera / Alletra 9K Host Paths

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
api_instance = greenlake-data-services.HostPathsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter host path by Key. (optional)
sort = 'sort_example' # str | oData query to sort host path resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Primera / Alletra 9K Host Paths
    api_response = api_instance.device_type1_get_all_host_paths(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostPathsApi->device_type1_get_all_host_paths: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter host path by Key. | [optional] 
 **sort** | **str**| oData query to sort host path resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraHostPathList**](PrimeraHostPathList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_host_paths_by_id**
> PrimeraHostPaths device_type1_get_host_paths_by_id(system_id, host_path_id, select=select)

Get details of Primera / Alletra 9K Host Path identified by {HostPathId}

Get details of Primera / Alletra 9K Host Path identified by {HostPathId}

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
api_instance = greenlake-data-services.HostPathsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
host_path_id = 'host_path_id_example' # str | ID of the primera Host Path. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Primera / Alletra 9K Host Path identified by {HostPathId}
    api_response = api_instance.device_type1_get_host_paths_by_id(system_id, host_path_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostPathsApi->device_type1_get_host_paths_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **host_path_id** | **str**| ID of the primera Host Path. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraHostPaths**](PrimeraHostPaths.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

