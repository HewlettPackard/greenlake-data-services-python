# greenlake-data-services.StorageSystemsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_application_summary_get**](StorageSystemsApi.md#device_type1_application_summary_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/application-summary | Get Application Summary for a storage system Primera / Alletra 9K
[**device_type1_get_system_performance_statistics**](StorageSystemsApi.md#device_type1_get_system_performance_statistics) | **GET** /api/v1/storage-systems/device-type1/{systemId}/performance-statistics | Get performance statistics for a storage system Primera / Alletra 9K
[**device_type1_qo_s_performance_statistics_get_by_target_name**](StorageSystemsApi.md#device_type1_qo_s_performance_statistics_get_by_target_name) | **GET** /api/v1/storage-systems/device-type1/{systemId}/targets/{targetName}/performance-history | Get QoS performance trend data of Primera / Alletra 9K target identified by {targetName}
[**device_type1_qo_s_policy_get_by_system_id**](StorageSystemsApi.md#device_type1_qo_s_policy_get_by_system_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/qos-policy | Get QoS policy data for a storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_recommendations_get**](StorageSystemsApi.md#device_type1_recommendations_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/recommendations | Get recommendations for a storage system Primera / Alletra 9K
[**device_type1_system_capacity_history_get**](StorageSystemsApi.md#device_type1_system_capacity_history_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/capacity-history | Get capacity trend data for a storage system Primera / Alletra 9K
[**device_type1_system_capacity_summary_get**](StorageSystemsApi.md#device_type1_system_capacity_summary_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/capacity-summary | Get system capacity for a storage system Primera / Alletra 9K
[**device_type1_system_component_performance_statistics_get**](StorageSystemsApi.md#device_type1_system_component_performance_statistics_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/component-performance-statistics | Get component performance statistics details for a storage system Primera / Alletra 9K idenfified by {systemId}
[**device_type1_system_get_by_id**](StorageSystemsApi.md#device_type1_system_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{id} | Get Primera / Alletra 9K object identified by {id}
[**device_type1_system_performance_history_get**](StorageSystemsApi.md#device_type1_system_performance_history_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/performance-history | Get performance trend data for a storage system Primera / Alletra 9K
[**device_type1_systems_list**](StorageSystemsApi.md#device_type1_systems_list) | **GET** /api/v1/storage-systems/device-type1 | Get all Primera / Alletra 9K storage systems
[**device_type2_array_failover**](StorageSystemsApi.md#device_type2_array_failover) | **POST** /api/v1/storage-systems/device-type2/{systemId}/arrays/{arrayId}/actions/failover | Perform failover of Nimble / Alletra 6K array identified by {arrayId}
[**device_type2_create_array**](StorageSystemsApi.md#device_type2_create_array) | **POST** /api/v1/storage-systems/device-type2/{systemId}/arrays | Create Nimble / Alletra 6K array identified by {systemId}
[**device_type2_delete_array_by_id**](StorageSystemsApi.md#device_type2_delete_array_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/arrays/{arrayId} | Delete Nimble / Alletra 6K array identified by {arrayId}
[**device_type2_edit_array_by_id**](StorageSystemsApi.md#device_type2_edit_array_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/arrays/{arrayId} | Edit  details of Nimble / Alletra 6K array identified by {arrayId}
[**device_type2_edit_storage_system_settings_by_id**](StorageSystemsApi.md#device_type2_edit_storage_system_settings_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId} | Edit settings of Nimble / Alletra 6K system identified by {systemId}
[**device_type2_get_application_capacity_statistics_by_id**](StorageSystemsApi.md#device_type2_get_application_capacity_statistics_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/applications/{id}/capacity-stats | Get capacity stats of Application identified by {id} for a storage system Nimble / Alletra 6K
[**device_type2_get_applications_capacity_statistics**](StorageSystemsApi.md#device_type2_get_applications_capacity_statistics) | **GET** /api/v1/storage-systems/device-type2/{systemId}/applications/capacity-stats | Get capacity stats of Applications for a storage system Nimble / Alletra 6K
[**device_type2_get_storage_system**](StorageSystemsApi.md#device_type2_get_storage_system) | **GET** /api/v1/storage-systems/device-type2 | Get all storage systems by Nimble / Alletra 6K
[**device_type2_get_storage_system_by_id**](StorageSystemsApi.md#device_type2_get_storage_system_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId} | Get Nimble / Alletra 6K object identified by {systemId}
[**device_type2_get_storage_system_capacity_history**](StorageSystemsApi.md#device_type2_get_storage_system_capacity_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/capacity-history | Get capacity trend data for a storage system Nimble / Alletra 6K
[**device_type2_get_storage_system_performance_history**](StorageSystemsApi.md#device_type2_get_storage_system_performance_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/performance-history | Get performance trend data for a storage system Nimble / Alletra 6K
[**device_type2_merge_groups**](StorageSystemsApi.md#device_type2_merge_groups) | **POST** /api/v1/storage-systems/device-type2/{systemId}/actions/merge | Perform group merge with the specified group.
[**get_device_type**](StorageSystemsApi.md#get_device_type) | **GET** /api/v1/storage-systems/storage-types | Get all device types
[**get_device_type2_array_by_id**](StorageSystemsApi.md#get_device_type2_array_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/arrays/{arrayId} | Get details of Nimble / Alletra 6K array identified by {arrayId}
[**get_device_type2_arrays**](StorageSystemsApi.md#get_device_type2_arrays) | **GET** /api/v1/storage-systems/device-type2/{systemId}/arrays | Get all arrays details by Nimble / Alletra 6K
[**get_device_type2_uninitialized_array_by_id**](StorageSystemsApi.md#get_device_type2_uninitialized_array_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/uninitialized-arrays/{uninitializedArrayId} | Get  uninitialized arrays details by Nimble / Alletra 6K  identified  by {uninitializedArrayId}
[**get_device_type2_uninitialized_arrays**](StorageSystemsApi.md#get_device_type2_uninitialized_arrays) | **POST** /api/v1/storage-systems/device-type2/{systemId}/uninitialized-arrays | Get all uninitialized arrays details by Nimble / Alletra 6K
[**provisioning_recommendations**](StorageSystemsApi.md#provisioning_recommendations) | **POST** /api/v1/storage-systems/provisioning-recommendations | provisioning recommendations
[**system_get_by_id**](StorageSystemsApi.md#system_get_by_id) | **GET** /api/v1/storage-systems/{id} | Get storage system object identified by {id}
[**system_locate**](StorageSystemsApi.md#system_locate) | **POST** /api/v1/storage-systems/device-type1/{id} | Locate system of Primera / Alletra 9K
[**systems_list**](StorageSystemsApi.md#systems_list) | **GET** /api/v1/storage-systems | Get all storage systems


# **device_type1_application_summary_get**
> ApplicationSummary device_type1_application_summary_get(system_id)

Get Application Summary for a storage system Primera / Alletra 9K

Get Application Summary for a storage system Primera / Alletra 9K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system

try:
    # Get Application Summary for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_application_summary_get(system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type1_application_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 

### Return type

[**ApplicationSummary**](ApplicationSummary.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_system_performance_statistics**
> SystemPerformance device_type1_get_system_performance_statistics(system_id, select=select)

Get performance statistics for a storage system Primera / Alletra 9K

Get performance statistics for a storage system Primera / Alletra 9K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get performance statistics for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_get_system_performance_statistics(system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type1_get_system_performance_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**SystemPerformance**](SystemPerformance.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_qo_s_performance_statistics_get_by_target_name**
> QosPerformanceHistory device_type1_qo_s_performance_statistics_get_by_target_name(system_id, target_name, select=select, range=range, time_interval_min=time_interval_min)

Get QoS performance trend data of Primera / Alletra 9K target identified by {targetName}

Get QoS performance trend data of Primera / Alletra 9K target identified by {targetName}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
target_name = 'target_name_example' # str | targetName will define the QoS target name in which query has to be made.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
time_interval_min = 56 # int | It defines granularity in minutes. (optional)

try:
    # Get QoS performance trend data of Primera / Alletra 9K target identified by {targetName}
    api_response = api_instance.device_type1_qo_s_performance_statistics_get_by_target_name(system_id, target_name, select=select, range=range, time_interval_min=time_interval_min)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type1_qo_s_performance_statistics_get_by_target_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **target_name** | **str**| targetName will define the QoS target name in which query has to be made. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**QosPerformanceHistory**](QosPerformanceHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_qo_s_policy_get_by_system_id**
> QosPolicy device_type1_qo_s_policy_get_by_system_id(system_id, limit=limit, offset=offset, select=select, range=range, target_name=target_name, target_type=target_type)

Get QoS policy data for a storage system Primera / Alletra 9K identified by {systemId}

Get QoS policy data for a storage system Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
target_name = 'target_name_example' # str | targetName will define the QoS target name in which query has to be made. (optional)
target_type = 'target_type_example' # str | targetType will define the QoS target type in which query has to be made. (optional)

try:
    # Get QoS policy data for a storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_qo_s_policy_get_by_system_id(system_id, limit=limit, offset=offset, select=select, range=range, target_name=target_name, target_type=target_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type1_qo_s_policy_get_by_system_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **target_name** | **str**| targetName will define the QoS target name in which query has to be made. | [optional] 
 **target_type** | **str**| targetType will define the QoS target type in which query has to be made. | [optional] 

### Return type

[**QosPolicy**](QosPolicy.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_recommendations_get**
> Recommendation device_type1_recommendations_get(system_id, select=select)

Get recommendations for a storage system Primera / Alletra 9K

Get recommendations for a storage system Primera / Alletra 9K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get recommendations for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_recommendations_get(system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type1_recommendations_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**Recommendation**](Recommendation.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_capacity_history_get**
> CapacityHistory device_type1_system_capacity_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)

Get capacity trend data for a storage system Primera / Alletra 9K

Get capacity trend data for a storage system Primera / Alletra 9K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
time_interval_min = 56 # int | It defines granularity in minutes. (optional)

try:
    # Get capacity trend data for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_system_capacity_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type1_system_capacity_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**CapacityHistory**](CapacityHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_capacity_summary_get**
> Syscapacity device_type1_system_capacity_summary_get(system_id, select=select)

Get system capacity for a storage system Primera / Alletra 9K

Get system capacity for a storage system Primera / Alletra 9K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get system capacity for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_system_capacity_summary_get(system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type1_system_capacity_summary_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**Syscapacity**](Syscapacity.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_component_performance_statistics_get**
> PerfStats device_type1_system_component_performance_statistics_get(system_id, select=select)

Get component performance statistics details for a storage system Primera / Alletra 9K idenfified by {systemId}

Get component performance statistics details for a storage system Primera / Alletra 9K idenfified by {systemId}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get component performance statistics details for a storage system Primera / Alletra 9K idenfified by {systemId}
    api_response = api_instance.device_type1_system_component_performance_statistics_get(system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type1_system_component_performance_statistics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PerfStats**](PerfStats.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_get_by_id**
> PrimeraStorageSystemDetail device_type1_system_get_by_id(id, select=select)

Get Primera / Alletra 9K object identified by {id}

Get Primera / Alletra 9K object identified by {id}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
id = 'id_example' # str | Serial number of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get Primera / Alletra 9K object identified by {id}
    api_response = api_instance.device_type1_system_get_by_id(id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type1_system_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Serial number of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraStorageSystemDetail**](PrimeraStorageSystemDetail.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_performance_history_get**
> SystemPerformanceHistory device_type1_system_performance_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)

Get performance trend data for a storage system Primera / Alletra 9K

Get performance trend data for a storage system Primera / Alletra 9K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
time_interval_min = 56 # int | It defines granularity in minutes. (optional)

try:
    # Get performance trend data for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_system_performance_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type1_system_performance_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**SystemPerformanceHistory**](SystemPerformanceHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_systems_list**
> PrimeraStorageSystemList device_type1_systems_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all Primera / Alletra 9K storage systems

Get all Primera / Alletra 9K storage systems

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter systems by Key. (optional)
sort = 'sort_example' # str | Query to sort the response with specified key and order (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all Primera / Alletra 9K storage systems
    api_response = api_instance.device_type1_systems_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type1_systems_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter systems by Key. | [optional] 
 **sort** | **str**| Query to sort the response with specified key and order | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraStorageSystemList**](PrimeraStorageSystemList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_array_failover**
> TaskResponse device_type2_array_failover(system_id, array_id, nimble_array_failover_input)

Perform failover of Nimble / Alletra 6K array identified by {arrayId}

Perform failover of Nimble / Alletra 6K array identified by {arrayId}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
array_id = 'array_id_example' # str | ID of the array.
nimble_array_failover_input = greenlake-data-services.NimbleArrayFailoverInput() # NimbleArrayFailoverInput | 

try:
    # Perform failover of Nimble / Alletra 6K array identified by {arrayId}
    api_response = api_instance.device_type2_array_failover(system_id, array_id, nimble_array_failover_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type2_array_failover: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **array_id** | **str**| ID of the array. | 
 **nimble_array_failover_input** | [**NimbleArrayFailoverInput**](NimbleArrayFailoverInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_create_array**
> TaskResponse device_type2_create_array(system_id, nimble_create_array_input)

Create Nimble / Alletra 6K array identified by {systemId}

Create Nimble / Alletra 6K array identified by {systemId}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_array_input = greenlake-data-services.NimbleCreateArrayInput() # NimbleCreateArrayInput | 

try:
    # Create Nimble / Alletra 6K array identified by {systemId}
    api_response = api_instance.device_type2_create_array(system_id, nimble_create_array_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type2_create_array: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_array_input** | [**NimbleCreateArrayInput**](NimbleCreateArrayInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_delete_array_by_id**
> TaskResponse device_type2_delete_array_by_id(system_id, array_id)

Delete Nimble / Alletra 6K array identified by {arrayId}

Delete Nimble / Alletra 6K array identified by {arrayId}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
array_id = 'array_id_example' # str | ID of the array.

try:
    # Delete Nimble / Alletra 6K array identified by {arrayId}
    api_response = api_instance.device_type2_delete_array_by_id(system_id, array_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type2_delete_array_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **array_id** | **str**| ID of the array. | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_array_by_id**
> TaskResponse device_type2_edit_array_by_id(system_id, array_id, nimble_edit_array_input)

Edit  details of Nimble / Alletra 6K array identified by {arrayId}

Edit  details of Nimble / Alletra 6K array identified by {arrayId}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
array_id = 'array_id_example' # str | ID of the array.
nimble_edit_array_input = greenlake-data-services.NimbleEditArrayInput() # NimbleEditArrayInput | 

try:
    # Edit  details of Nimble / Alletra 6K array identified by {arrayId}
    api_response = api_instance.device_type2_edit_array_by_id(system_id, array_id, nimble_edit_array_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type2_edit_array_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **array_id** | **str**| ID of the array. | 
 **nimble_edit_array_input** | [**NimbleEditArrayInput**](NimbleEditArrayInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_storage_system_settings_by_id**
> TaskResponse device_type2_edit_storage_system_settings_by_id(system_id, nimble_edit_group_input)

Edit settings of Nimble / Alletra 6K system identified by {systemId}

Edit settings of Nimble / Alletra 6K system identified by {systemId}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_edit_group_input = greenlake-data-services.NimbleEditGroupInput() # NimbleEditGroupInput | 

try:
    # Edit settings of Nimble / Alletra 6K system identified by {systemId}
    api_response = api_instance.device_type2_edit_storage_system_settings_by_id(system_id, nimble_edit_group_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type2_edit_storage_system_settings_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_edit_group_input** | [**NimbleEditGroupInput**](NimbleEditGroupInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_application_capacity_statistics_by_id**
> NimbleSpaceDomainDetailsWithRequestUri device_type2_get_application_capacity_statistics_by_id(system_id, id, select=select)

Get capacity stats of Application identified by {id} for a storage system Nimble / Alletra 6K

Get capacity stats of Application identified by {id} for a storage system Nimble / Alletra 6K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
id = 'id_example' # str | ID of the application-summery. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get capacity stats of Application identified by {id} for a storage system Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_application_capacity_statistics_by_id(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type2_get_application_capacity_statistics_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **id** | **str**| ID of the application-summery. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleSpaceDomainDetailsWithRequestUri**](NimbleSpaceDomainDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_applications_capacity_statistics**
> NimbleSpaceDomainList device_type2_get_applications_capacity_statistics(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get capacity stats of Applications for a storage system Nimble / Alletra 6K

Get capacity stats of Applications for a storage system Nimble / Alletra 6K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter application summery by Key. (optional)
sort = 'sort_example' # str | oData query to sort application summery resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get capacity stats of Applications for a storage system Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_applications_capacity_statistics(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type2_get_applications_capacity_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter application summery by Key. | [optional] 
 **sort** | **str**| oData query to sort application summery resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleSpaceDomainList**](NimbleSpaceDomainList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_storage_system**
> NimbleStorageSystemSummaryList device_type2_get_storage_system(limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all storage systems by Nimble / Alletra 6K

Get all storage systems by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter systems by Key. (optional)
sort = 'sort_example' # str | Lucene query to sort systems by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all storage systems by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_storage_system(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type2_get_storage_system: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter systems by Key. | [optional] 
 **sort** | **str**| Lucene query to sort systems by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleStorageSystemSummaryList**](NimbleStorageSystemSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_storage_system_by_id**
> NimbleStorageSystemDetailsWithRequestUri device_type2_get_storage_system_by_id(system_id, select=select)

Get Nimble / Alletra 6K object identified by {systemId}

Get Nimble / Alletra 6K object identified by {systemId}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get Nimble / Alletra 6K object identified by {systemId}
    api_response = api_instance.device_type2_get_storage_system_by_id(system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type2_get_storage_system_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleStorageSystemDetailsWithRequestUri**](NimbleStorageSystemDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_storage_system_capacity_history**
> NimblecapacityHistory device_type2_get_storage_system_capacity_history(system_id, select=select, range=range, time_interval_min=time_interval_min)

Get capacity trend data for a storage system Nimble / Alletra 6K

Get capacity trend data for a storage system Nimble / Alletra 6K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
time_interval_min = 56 # int | It defines granularity in minutes. (optional)

try:
    # Get capacity trend data for a storage system Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_storage_system_capacity_history(system_id, select=select, range=range, time_interval_min=time_interval_min)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type2_get_storage_system_capacity_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**NimblecapacityHistory**](NimblecapacityHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_storage_system_performance_history**
> SysPerformanceHistory device_type2_get_storage_system_performance_history(system_id, select=select, range=range, time_interval_min=time_interval_min)

Get performance trend data for a storage system Nimble / Alletra 6K

Get performance trend data for a storage system Nimble / Alletra 6K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
time_interval_min = 56 # int | It defines granularity in minutes. (optional)

try:
    # Get performance trend data for a storage system Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_storage_system_performance_history(system_id, select=select, range=range, time_interval_min=time_interval_min)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type2_get_storage_system_performance_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**SysPerformanceHistory**](SysPerformanceHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_merge_groups**
> TaskResponse device_type2_merge_groups(system_id, nimble_merge_groups_input)

Perform group merge with the specified group.

Perform group merge with the specified group.

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_merge_groups_input = greenlake-data-services.NimbleMergeGroupsInput() # NimbleMergeGroupsInput | 

try:
    # Perform group merge with the specified group.
    api_response = api_instance.device_type2_merge_groups(system_id, nimble_merge_groups_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->device_type2_merge_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_merge_groups_input** | [**NimbleMergeGroupsInput**](NimbleMergeGroupsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type**
> StorageTypes get_device_type()

Get all device types

Get all device types

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))

try:
    # Get all device types
    api_response = api_instance.get_device_type()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->get_device_type: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**StorageTypes**](StorageTypes.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type2_array_by_id**
> NimbleArrayDetailsWithRequestUri get_device_type2_array_by_id(system_id, array_id, select=select)

Get details of Nimble / Alletra 6K array identified by {arrayId}

Get details of Nimble / Alletra 6K array identified by {arrayId}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
array_id = 'array_id_example' # str | ID of the array.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K array identified by {arrayId}
    api_response = api_instance.get_device_type2_array_by_id(system_id, array_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->get_device_type2_array_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **array_id** | **str**| ID of the array. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleArrayDetailsWithRequestUri**](NimbleArrayDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type2_arrays**
> NimbleNewArrayList get_device_type2_arrays(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all arrays details by Nimble / Alletra 6K

Get all arrays details by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter array by Key. (optional)
sort = 'sort_example' # str | oData query to sort array resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all arrays details by Nimble / Alletra 6K
    api_response = api_instance.get_device_type2_arrays(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->get_device_type2_arrays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter array by Key. | [optional] 
 **sort** | **str**| oData query to sort array resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleNewArrayList**](NimbleNewArrayList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type2_uninitialized_array_by_id**
> NimbleUninitializedArrayWithRequestUri get_device_type2_uninitialized_array_by_id(system_id, uninitialized_array_id, nimble_uninitialized_array_input, select=select)

Get  uninitialized arrays details by Nimble / Alletra 6K  identified  by {uninitializedArrayId}

Get uninitialized arrays details by Nimble / Alletra 6K identified  by {uninitializedArrayId}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
uninitialized_array_id = 'uninitialized_array_id_example' # str | ID of the uninitialized Array.A 42 digit hexadecimal number.
nimble_uninitialized_array_input = greenlake-data-services.NimbleUninitializedArrayInput() # NimbleUninitializedArrayInput | 
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get  uninitialized arrays details by Nimble / Alletra 6K  identified  by {uninitializedArrayId}
    api_response = api_instance.get_device_type2_uninitialized_array_by_id(system_id, uninitialized_array_id, nimble_uninitialized_array_input, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->get_device_type2_uninitialized_array_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **uninitialized_array_id** | **str**| ID of the uninitialized Array.A 42 digit hexadecimal number. | 
 **nimble_uninitialized_array_input** | [**NimbleUninitializedArrayInput**](NimbleUninitializedArrayInput.md)|  | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleUninitializedArrayWithRequestUri**](NimbleUninitializedArrayWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type2_uninitialized_arrays**
> NimbleUninitializedArrayResponse get_device_type2_uninitialized_arrays(system_id)

Get all uninitialized arrays details by Nimble / Alletra 6K

Get all uninitialized arrays details by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system

try:
    # Get all uninitialized arrays details by Nimble / Alletra 6K
    api_response = api_instance.get_device_type2_uninitialized_arrays(system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->get_device_type2_uninitialized_arrays: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 

### Return type

[**NimbleUninitializedArrayResponse**](NimbleUninitializedArrayResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provisioning_recommendations**
> StorageSystemRecommendationList provisioning_recommendations(recommendation_input)

provisioning recommendations

provisioning recommendations

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
recommendation_input = greenlake-data-services.RecommendationInput() # RecommendationInput | 

try:
    # provisioning recommendations
    api_response = api_instance.provisioning_recommendations(recommendation_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->provisioning_recommendations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommendation_input** | [**RecommendationInput**](RecommendationInput.md)|  | 

### Return type

[**StorageSystemRecommendationList**](StorageSystemRecommendationList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_by_id**
> StorageSystemDetail system_get_by_id(id, select=select)

Get storage system object identified by {id}

Get storage system object identified by {id}

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
id = 'id_example' # str | Serial number of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get storage system object identified by {id}
    api_response = api_instance.system_get_by_id(id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->system_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Serial number of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**StorageSystemDetail**](StorageSystemDetail.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_locate**
> TaskResponse system_locate(id, sys_locate_input)

Locate system of Primera / Alletra 9K

Locate system of Primera / Alletra 9K

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
id = 'id_example' # str | Serial number of the device-type1 storage system
sys_locate_input = greenlake-data-services.SysLocateInput() # SysLocateInput | 

try:
    # Locate system of Primera / Alletra 9K
    api_response = api_instance.system_locate(id, sys_locate_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->system_locate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Serial number of the device-type1 storage system | 
 **sys_locate_input** | [**SysLocateInput**](SysLocateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_list**
> StorageSystemSummaryList systems_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all storage systems

Get all storage systems

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
api_instance = greenlake-data-services.StorageSystemsApi(greenlake-data-services.ApiClient(configuration))
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter systems by Key. (optional)
sort = 'sort_example' # str | Query to sort the response with specified key and order (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all storage systems
    api_response = api_instance.systems_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StorageSystemsApi->systems_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter systems by Key. | [optional] 
 **sort** | **str**| Query to sort the response with specified key and order | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**StorageSystemSummaryList**](StorageSystemSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

