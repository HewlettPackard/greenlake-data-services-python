# greenlake-data-services.PerformanceTemplatesApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_get_all_performance_policies**](PerformanceTemplatesApi.md#device_type2_get_all_performance_policies) | **GET** /api/v1/storage-systems/device-type2/{systemId}/performance-policies | Get all performance-policies details by Nimble / Alletra 6K
[**device_type2_get_performance_policy_by_id**](PerformanceTemplatesApi.md#device_type2_get_performance_policy_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/performance-policies/{performancePolicyId} | Get details of Nimble / Alletra 6K performance-policy identified by {performancePolicyId}
[**device_type2_performance_policy_create**](PerformanceTemplatesApi.md#device_type2_performance_policy_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/performance-policies | Create Nimble / Alletra 6K performance policy in a system identified by {systemId}
[**device_type2_performance_policy_edit**](PerformanceTemplatesApi.md#device_type2_performance_policy_edit) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/performance-policies/{performancePolicyId} | Edit details of Nimble / Alletra 6K performance policy identified by {performancePolicyId}
[**device_type2_remove_perf_policy_id**](PerformanceTemplatesApi.md#device_type2_remove_perf_policy_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/performance-policies/{performancePolicyId} | Remove performance-policies identified by {performancePolicyId} from Nimble / Alletra 6K


# **device_type2_get_all_performance_policies**
> NimblePerformancePolicyList device_type2_get_all_performance_policies(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all performance-policies details by Nimble / Alletra 6K

Get all performance-policies details by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.PerformanceTemplatesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter performance Policy by Key. (optional)
sort = 'sort_example' # str | oData query to sort performance Policy resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all performance-policies details by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_performance_policies(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceTemplatesApi->device_type2_get_all_performance_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter performance Policy by Key. | [optional] 
 **sort** | **str**| oData query to sort performance Policy resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimblePerformancePolicyList**](NimblePerformancePolicyList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_performance_policy_by_id**
> NimblePerformancePolicyDetailsWithRequestUri device_type2_get_performance_policy_by_id(system_id, performance_policy_id, select=select)

Get details of Nimble / Alletra 6K performance-policy identified by {performancePolicyId}

Get details of Nimble / Alletra 6K performance-policy identified by {performancePolicyId}

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
api_instance = greenlake-data-services.PerformanceTemplatesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
performance_policy_id = 'performance_policy_id_example' # str | ID of the performance Policy. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K performance-policy identified by {performancePolicyId}
    api_response = api_instance.device_type2_get_performance_policy_by_id(system_id, performance_policy_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceTemplatesApi->device_type2_get_performance_policy_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **performance_policy_id** | **str**| ID of the performance Policy. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimblePerformancePolicyDetailsWithRequestUri**](NimblePerformancePolicyDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_performance_policy_create**
> TaskResponse device_type2_performance_policy_create(system_id, nimble_create_performance_policy_input)

Create Nimble / Alletra 6K performance policy in a system identified by {systemId}

Create Nimble / Alletra 6K performance policy in a system identified by {systemId}

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
api_instance = greenlake-data-services.PerformanceTemplatesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_performance_policy_input = greenlake-data-services.NimbleCreatePerformancePolicyInput() # NimbleCreatePerformancePolicyInput | 

try:
    # Create Nimble / Alletra 6K performance policy in a system identified by {systemId}
    api_response = api_instance.device_type2_performance_policy_create(system_id, nimble_create_performance_policy_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceTemplatesApi->device_type2_performance_policy_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_performance_policy_input** | [**NimbleCreatePerformancePolicyInput**](NimbleCreatePerformancePolicyInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_performance_policy_edit**
> TaskResponse device_type2_performance_policy_edit(system_id, performance_policy_id, nimble_edit_performance_policy_input)

Edit details of Nimble / Alletra 6K performance policy identified by {performancePolicyId}

Edit details of Nimble / Alletra 6K performance policy identified by {performancePolicyId}

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
api_instance = greenlake-data-services.PerformanceTemplatesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
performance_policy_id = 'performance_policy_id_example' # str | ID of the performance Policy. A 42 digit hexadecimal number.
nimble_edit_performance_policy_input = greenlake-data-services.NimbleEditPerformancePolicyInput() # NimbleEditPerformancePolicyInput | 

try:
    # Edit details of Nimble / Alletra 6K performance policy identified by {performancePolicyId}
    api_response = api_instance.device_type2_performance_policy_edit(system_id, performance_policy_id, nimble_edit_performance_policy_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceTemplatesApi->device_type2_performance_policy_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **performance_policy_id** | **str**| ID of the performance Policy. A 42 digit hexadecimal number. | 
 **nimble_edit_performance_policy_input** | [**NimbleEditPerformancePolicyInput**](NimbleEditPerformancePolicyInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_perf_policy_id**
> TaskResponse device_type2_remove_perf_policy_id(system_id, performance_policy_id)

Remove performance-policies identified by {performancePolicyId} from Nimble / Alletra 6K

Remove performance-policies identified by {performancePolicyId} from Nimble / Alletra 6K

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
api_instance = greenlake-data-services.PerformanceTemplatesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
performance_policy_id = 'performance_policy_id_example' # str | ID of the performance Policy. A 42 digit hexadecimal number.

try:
    # Remove performance-policies identified by {performancePolicyId} from Nimble / Alletra 6K
    api_response = api_instance.device_type2_remove_perf_policy_id(system_id, performance_policy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PerformanceTemplatesApi->device_type2_remove_perf_policy_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **performance_policy_id** | **str**| ID of the performance Policy. A 42 digit hexadecimal number. | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

