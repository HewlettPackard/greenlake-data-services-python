# greenlake_data_services.StorageSystemsApi

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

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.application_summary import ApplicationSummary
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system

    # example passing only required values which don't have defaults set
    try:
        # Get Application Summary for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_application_summary_get(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_system_performance_statistics**
> SystemPerformance device_type1_get_system_performance_statistics(system_id)

Get performance statistics for a storage system Primera / Alletra 9K

Get performance statistics for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.system_performance import SystemPerformance
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get performance statistics for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_get_system_performance_statistics(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type1_get_system_performance_statistics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get performance statistics for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_get_system_performance_statistics(system_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_qo_s_performance_statistics_get_by_target_name**
> QosPerformanceHistory device_type1_qo_s_performance_statistics_get_by_target_name(system_id, target_name)

Get QoS performance trend data of Primera / Alletra 9K target identified by {targetName}

Get QoS performance trend data of Primera / Alletra 9K target identified by {targetName}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.qos_performance_history import QosPerformanceHistory
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    target_name = "targetName eq volume1" # str | targetName will define the QoS target name in which query has to be made.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    range = "startTime eq 1605063600 and endTime eq 1605186000" # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get QoS performance trend data of Primera / Alletra 9K target identified by {targetName}
        api_response = api_instance.device_type1_qo_s_performance_statistics_get_by_target_name(system_id, target_name)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type1_qo_s_performance_statistics_get_by_target_name: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get QoS performance trend data of Primera / Alletra 9K target identified by {targetName}
        api_response = api_instance.device_type1_qo_s_performance_statistics_get_by_target_name(system_id, target_name, select=select, range=range, time_interval_min=time_interval_min)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_qo_s_policy_get_by_system_id**
> QosPolicy device_type1_qo_s_policy_get_by_system_id(system_id)

Get QoS policy data for a storage system Primera / Alletra 9K identified by {systemId}

Get QoS policy data for a storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.qos_policy import QosPolicy
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    range = "startTime eq 1605063600 and endTime eq 1605186000" # str | range will define start and end time in which query has to be made. (optional)
    target_name = "targetName eq volume1" # str | targetName will define the QoS target name in which query has to be made. (optional)
    target_type = "targetType eq vv" # str | targetType will define the QoS target type in which query has to be made. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get QoS policy data for a storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_qo_s_policy_get_by_system_id(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type1_qo_s_policy_get_by_system_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get QoS policy data for a storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_qo_s_policy_get_by_system_id(system_id, limit=limit, offset=offset, select=select, range=range, target_name=target_name, target_type=target_type)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_recommendations_get**
> Recommendation device_type1_recommendations_get(system_id)

Get recommendations for a storage system Primera / Alletra 9K

Get recommendations for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.recommendation import Recommendation
from greenlake_data_services.model.error import Error
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get recommendations for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_recommendations_get(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type1_recommendations_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get recommendations for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_recommendations_get(system_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_capacity_history_get**
> CapacityHistory device_type1_system_capacity_history_get(system_id)

Get capacity trend data for a storage system Primera / Alletra 9K

Get capacity trend data for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.capacity_history import CapacityHistory
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    range = "startTime eq 1605063600 and endTime eq 1605186000" # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get capacity trend data for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_system_capacity_history_get(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type1_system_capacity_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get capacity trend data for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_system_capacity_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_capacity_summary_get**
> Syscapacity device_type1_system_capacity_summary_get(system_id)

Get system capacity for a storage system Primera / Alletra 9K

Get system capacity for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.syscapacity import Syscapacity
from greenlake_data_services.model.error import Error
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get system capacity for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_system_capacity_summary_get(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type1_system_capacity_summary_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get system capacity for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_system_capacity_summary_get(system_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_component_performance_statistics_get**
> PerfStats device_type1_system_component_performance_statistics_get(system_id)

Get component performance statistics details for a storage system Primera / Alletra 9K idenfified by {systemId}

Get component performance statistics details for a storage system Primera / Alletra 9K idenfified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.perf_stats import PerfStats
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get component performance statistics details for a storage system Primera / Alletra 9K idenfified by {systemId}
        api_response = api_instance.device_type1_system_component_performance_statistics_get(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type1_system_component_performance_statistics_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get component performance statistics details for a storage system Primera / Alletra 9K idenfified by {systemId}
        api_response = api_instance.device_type1_system_component_performance_statistics_get(system_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_get_by_id**
> PrimeraStorageSystemDetail device_type1_system_get_by_id(id)

Get Primera / Alletra 9K object identified by {id}

Get Primera / Alletra 9K object identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.primera_storage_system_detail import PrimeraStorageSystemDetail
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    id = "SGH029VBHV" # str | Serial number of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Primera / Alletra 9K object identified by {id}
        api_response = api_instance.device_type1_system_get_by_id(id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type1_system_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Primera / Alletra 9K object identified by {id}
        api_response = api_instance.device_type1_system_get_by_id(id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_system_performance_history_get**
> SystemPerformanceHistory device_type1_system_performance_history_get(system_id)

Get performance trend data for a storage system Primera / Alletra 9K

Get performance trend data for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.system_performance_history import SystemPerformanceHistory
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    range = "startTime eq 1605063600 and endTime eq 1605186000" # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get performance trend data for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_system_performance_history_get(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type1_system_performance_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get performance trend data for a storage system Primera / Alletra 9K
        api_response = api_instance.device_type1_system_performance_history_get(system_id, select=select, range=range, time_interval_min=time_interval_min)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_systems_list**
> PrimeraStorageSystemList device_type1_systems_list()

Get all Primera / Alletra 9K storage systems

Get all Primera / Alletra 9K storage systems

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.primera_storage_system_list import PrimeraStorageSystemList
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "name eq VEGA_CB1507_8400_2N_150" # str | oData query to filter systems by Key. (optional)
    sort = "id asc,name desc" # str | Query to sort the response with specified key and order (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all Primera / Alletra 9K storage systems
        api_response = api_instance.device_type1_systems_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_array_failover**
> TaskResponse device_type2_array_failover(system_id, array_id, nimble_array_failover_input)

Perform failover of Nimble / Alletra 6K array identified by {arrayId}

Perform failover of Nimble / Alletra 6K array identified by {arrayId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_array_failover_input import NimbleArrayFailoverInput
from greenlake_data_services.model.task_response import TaskResponse
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    array_id = "001df0fe6f7dc7bb16000000000000000000004817" # str | ID of the array.
    nimble_array_failover_input = NimbleArrayFailoverInput(
        force=False,
    ) # NimbleArrayFailoverInput | 

    # example passing only required values which don't have defaults set
    try:
        # Perform failover of Nimble / Alletra 6K array identified by {arrayId}
        api_response = api_instance.device_type2_array_failover(system_id, array_id, nimble_array_failover_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_create_array**
> TaskResponse device_type2_create_array(system_id, nimble_create_array_input)

Create Nimble / Alletra 6K array identified by {systemId}

Create Nimble / Alletra 6K array identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from greenlake_data_services.model.nimble_create_array_input import NimbleCreateArrayInput
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_create_array_input = NimbleCreateArrayInput(
        allow_lower_limits=False,
        create_pool=False,
        ctrlr_a_support_ip="128.0.0.1",
        ctrlr_b_support_ip="128.0.0.1",
        dedupe_disabled=False,
        name="NimbleArray",
        nic_list=[
            NICDetails(
                data_ip="128.0.0.1",
                name="NICName",
                subnet_label="255.255.255.0",
                tagged=True,
            ),
        ],
        pool_description="99.9999% availability",
        pool_name="myobject-5",
        secondary_mgmt_ip="128.0.0.1",
        serial="AC-109084",
    ) # NimbleCreateArrayInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create Nimble / Alletra 6K array identified by {systemId}
        api_response = api_instance.device_type2_create_array(system_id, nimble_create_array_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_delete_array_by_id**
> TaskResponse device_type2_delete_array_by_id(system_id, array_id)

Delete Nimble / Alletra 6K array identified by {arrayId}

Delete Nimble / Alletra 6K array identified by {arrayId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    array_id = "001df0fe6f7dc7bb16000000000000000000004817" # str | ID of the array.

    # example passing only required values which don't have defaults set
    try:
        # Delete Nimble / Alletra 6K array identified by {arrayId}
        api_response = api_instance.device_type2_delete_array_by_id(system_id, array_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_array_by_id**
> TaskResponse device_type2_edit_array_by_id(system_id, array_id, nimble_edit_array_input)

Edit  details of Nimble / Alletra 6K array identified by {arrayId}

Edit  details of Nimble / Alletra 6K array identified by {arrayId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.nimble_edit_array_input import NimbleEditArrayInput
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    array_id = "001df0fe6f7dc7bb16000000000000000000004817" # str | ID of the array.
    nimble_edit_array_input = NimbleEditArrayInput(
        name="NimbleArray",
    ) # NimbleEditArrayInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit  details of Nimble / Alletra 6K array identified by {arrayId}
        api_response = api_instance.device_type2_edit_array_by_id(system_id, array_id, nimble_edit_array_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_storage_system_settings_by_id**
> TaskResponse device_type2_edit_storage_system_settings_by_id(system_id, nimble_edit_group_input)

Edit settings of Nimble / Alletra 6K system identified by {systemId}

Edit settings of Nimble / Alletra 6K system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_edit_group_input import NimbleEditGroupInput
from greenlake_data_services.model.task_response import TaskResponse
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_edit_group_input = NimbleEditGroupInput(
        auto_switchover_enabled=True,
        autoclean_unmanaged_snapshots_enabled=False,
        autoclean_unmanaged_snapshots_ttl_unit=0,
        cc_mode_enabled=False,
        date=1598267193,
        default_iscsi_target_scope="group",
        group_snapshot_ttl=0,
        group_target_name="iqn.2007-11.com.abc:g1a1-g00000000000004d3",
        name="myobject-5",
        ntp_server="0.abc.pool.ntp.org",
        tdz_enabled=False,
        tdz_prefix="peerzone",
        timezone="America/Los_Angeles",
        tlsv1_enabled=False,
    ) # NimbleEditGroupInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit settings of Nimble / Alletra 6K system identified by {systemId}
        api_response = api_instance.device_type2_edit_storage_system_settings_by_id(system_id, nimble_edit_group_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_application_capacity_statistics_by_id**
> NimbleSpaceDomainDetailsWithRequestUri device_type2_get_application_capacity_statistics_by_id(system_id, id)

Get capacity stats of Application identified by {id} for a storage system Nimble / Alletra 6K

Get capacity stats of Application identified by {id} for a storage system Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.nimble_space_domain_details_with_request_uri import NimbleSpaceDomainDetailsWithRequestUri
from greenlake_data_services.model.error import Error
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the application-summery. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get capacity stats of Application identified by {id} for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_application_capacity_statistics_by_id(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type2_get_application_capacity_statistics_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get capacity stats of Application identified by {id} for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_application_capacity_statistics_by_id(system_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_applications_capacity_statistics**
> NimbleSpaceDomainList device_type2_get_applications_capacity_statistics(system_id)

Get capacity stats of Applications for a storage system Nimble / Alletra 6K

Get capacity stats of Applications for a storage system Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_space_domain_list import NimbleSpaceDomainList
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter application summery by Key. (optional)
    sort = "name desc" # str | oData query to sort application summery resource by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get capacity stats of Applications for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_applications_capacity_statistics(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type2_get_applications_capacity_statistics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get capacity stats of Applications for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_applications_capacity_statistics(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_storage_system**
> NimbleStorageSystemSummaryList device_type2_get_storage_system()

Get all storage systems by Nimble / Alletra 6K

Get all storage systems by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_storage_system_summary_list import NimbleStorageSystemSummaryList
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "NAME eq g1a1" # str | Lucene query to filter systems by Key. (optional)
    sort = "name desc" # str | Lucene query to sort systems by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all storage systems by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_storage_system(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_storage_system_by_id**
> NimbleStorageSystemDetailsWithRequestUri device_type2_get_storage_system_by_id(system_id)

Get Nimble / Alletra 6K object identified by {systemId}

Get Nimble / Alletra 6K object identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_storage_system_details_with_request_uri import NimbleStorageSystemDetailsWithRequestUri
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Nimble / Alletra 6K object identified by {systemId}
        api_response = api_instance.device_type2_get_storage_system_by_id(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type2_get_storage_system_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Nimble / Alletra 6K object identified by {systemId}
        api_response = api_instance.device_type2_get_storage_system_by_id(system_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_storage_system_capacity_history**
> NimblecapacityHistory device_type2_get_storage_system_capacity_history(system_id)

Get capacity trend data for a storage system Nimble / Alletra 6K

Get capacity trend data for a storage system Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimblecapacity_history import NimblecapacityHistory
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    range = "startTime eq 1605063600 and endTime eq 1605186000" # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get capacity trend data for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_storage_system_capacity_history(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type2_get_storage_system_capacity_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get capacity trend data for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_storage_system_capacity_history(system_id, select=select, range=range, time_interval_min=time_interval_min)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_storage_system_performance_history**
> SysPerformanceHistory device_type2_get_storage_system_performance_history(system_id)

Get performance trend data for a storage system Nimble / Alletra 6K

Get performance trend data for a storage system Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.sys_performance_history import SysPerformanceHistory
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    range = "startTime eq 1605063600 and endTime eq 1605186000" # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get performance trend data for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_storage_system_performance_history(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->device_type2_get_storage_system_performance_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get performance trend data for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_storage_system_performance_history(system_id, select=select, range=range, time_interval_min=time_interval_min)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_merge_groups**
> TaskResponse device_type2_merge_groups(system_id, nimble_merge_groups_input)

Perform group merge with the specified group.

Perform group merge with the specified group.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_merge_groups_input import NimbleMergeGroupsInput
from greenlake_data_services.model.task_response import TaskResponse
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_merge_groups_input = NimbleMergeGroupsInput(
        force=True,
        skip_secondary_mgmt_ip=True,
        src_group_ip="123.12.12.32",
        src_group_name="group1",
        src_passphrase="passphrase-91",
        src_password="password1",
        src_username="admin",
    ) # NimbleMergeGroupsInput | 

    # example passing only required values which don't have defaults set
    try:
        # Perform group merge with the specified group.
        api_response = api_instance.device_type2_merge_groups(system_id, nimble_merge_groups_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type**
> StorageTypes get_device_type()

Get all device types

Get all device types

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.storage_types import StorageTypes
from greenlake_data_services.model.error import Error
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get all device types
        api_response = api_instance.get_device_type()
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type2_array_by_id**
> NimbleArrayDetailsWithRequestUri get_device_type2_array_by_id(system_id, array_id)

Get details of Nimble / Alletra 6K array identified by {arrayId}

Get details of Nimble / Alletra 6K array identified by {arrayId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_array_details_with_request_uri import NimbleArrayDetailsWithRequestUri
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    array_id = "001df0fe6f7dc7bb16000000000000000000004817" # str | ID of the array.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K array identified by {arrayId}
        api_response = api_instance.get_device_type2_array_by_id(system_id, array_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->get_device_type2_array_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K array identified by {arrayId}
        api_response = api_instance.get_device_type2_array_by_id(system_id, array_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type2_arrays**
> NimbleNewArrayList get_device_type2_arrays(system_id)

Get all arrays details by Nimble / Alletra 6K

Get all arrays details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_new_array_list import NimbleNewArrayList
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter array by Key. (optional)
    sort = "name desc" # str | oData query to sort array resource by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all arrays details by Nimble / Alletra 6K
        api_response = api_instance.get_device_type2_arrays(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->get_device_type2_arrays: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all arrays details by Nimble / Alletra 6K
        api_response = api_instance.get_device_type2_arrays(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type2_uninitialized_array_by_id**
> NimbleUninitializedArrayWithRequestUri get_device_type2_uninitialized_array_by_id(system_id, uninitialized_array_id, nimble_uninitialized_array_input)

Get  uninitialized arrays details by Nimble / Alletra 6K  identified  by {uninitializedArrayId}

Get uninitialized arrays details by Nimble / Alletra 6K identified  by {uninitializedArrayId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.nimble_uninitialized_array_input import NimbleUninitializedArrayInput
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_uninitialized_array_with_request_uri import NimbleUninitializedArrayWithRequestUri
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    uninitialized_array_id = "c463732d6436306437370000000000000000000000" # str | ID of the uninitialized Array.A 42 digit hexadecimal number.
    nimble_uninitialized_array_input = NimbleUninitializedArrayInput(
        id="c463732d6436306437370000000000000000000000",
    ) # NimbleUninitializedArrayInput | 
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get  uninitialized arrays details by Nimble / Alletra 6K  identified  by {uninitializedArrayId}
        api_response = api_instance.get_device_type2_uninitialized_array_by_id(system_id, uninitialized_array_id, nimble_uninitialized_array_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->get_device_type2_uninitialized_array_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get  uninitialized arrays details by Nimble / Alletra 6K  identified  by {uninitializedArrayId}
        api_response = api_instance.get_device_type2_uninitialized_array_by_id(system_id, uninitialized_array_id, nimble_uninitialized_array_input, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type2_uninitialized_arrays**
> NimbleUninitializedArrayResponse get_device_type2_uninitialized_arrays(system_id)

Get all uninitialized arrays details by Nimble / Alletra 6K

Get all uninitialized arrays details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_uninitialized_array_response import NimbleUninitializedArrayResponse
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system

    # example passing only required values which don't have defaults set
    try:
        # Get all uninitialized arrays details by Nimble / Alletra 6K
        api_response = api_instance.get_device_type2_uninitialized_arrays(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provisioning_recommendations**
> StorageSystemRecommendationList provisioning_recommendations(recommendation_input)

provisioning recommendations

provisioning recommendations

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.recommendation_input import RecommendationInput
from greenlake_data_services.model.storage_system_recommendation_list import StorageSystemRecommendationList
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    recommendation_input = RecommendationInput(
        host_group_id="a7c4e6593f51d0b98f0e40d7e6df04fd",
        product_family="product_family_example",
        size_mib=16384,
    ) # RecommendationInput | 

    # example passing only required values which don't have defaults set
    try:
        # provisioning recommendations
        api_response = api_instance.provisioning_recommendations(recommendation_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_get_by_id**
> StorageSystemDetail system_get_by_id(id)

Get storage system object identified by {id}

Get storage system object identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.storage_system_detail import StorageSystemDetail
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    id = "SGH029VBHV" # str | Serial number of the device-type1 storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get storage system object identified by {id}
        api_response = api_instance.system_get_by_id(id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling StorageSystemsApi->system_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get storage system object identified by {id}
        api_response = api_instance.system_get_by_id(id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_locate**
> TaskResponse system_locate(id, sys_locate_input)

Locate system of Primera / Alletra 9K

Locate system of Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.sys_locate_input import SysLocateInput
from greenlake_data_services.model.task_response import TaskResponse
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    id = "SGH029VBHV" # str | Serial number of the device-type1 storage system
    sys_locate_input = SysLocateInput(
        locate_enabled=True,
    ) # SysLocateInput | 

    # example passing only required values which don't have defaults set
    try:
        # Locate system of Primera / Alletra 9K
        api_response = api_instance.system_locate(id, sys_locate_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **systems_list**
> StorageSystemSummaryList systems_list()

Get all storage systems

Get all storage systems

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import storage_systems_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.storage_system_summary_list import StorageSystemSummaryList
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
    api_instance = storage_systems_api.StorageSystemsApi(api_client)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "name eq VEGA_CB1507_8400_2N_150" # str | oData query to filter systems by Key. (optional)
    sort = "id asc,name desc" # str | Query to sort the response with specified key and order (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all storage systems
        api_response = api_instance.systems_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

