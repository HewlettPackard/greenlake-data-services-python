# greenlake_data_services.PerformanceTemplatesApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_get_all_performance_policies**](PerformanceTemplatesApi.md#device_type2_get_all_performance_policies) | **GET** /api/v1/storage-systems/device-type2/{systemId}/performance-policies | Get all performance-policies details by Nimble / Alletra 6K
[**device_type2_get_performance_policy_by_id**](PerformanceTemplatesApi.md#device_type2_get_performance_policy_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/performance-policies/{performancePolicyId} | Get details of Nimble / Alletra 6K performance-policy identified by {performancePolicyId}
[**device_type2_performance_policy_create**](PerformanceTemplatesApi.md#device_type2_performance_policy_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/performance-policies | Create Nimble / Alletra 6K performance policy in a system identified by {systemId}
[**device_type2_performance_policy_edit**](PerformanceTemplatesApi.md#device_type2_performance_policy_edit) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/performance-policies/{performancePolicyId} | Edit details of Nimble / Alletra 6K performance policy identified by {performancePolicyId}
[**device_type2_remove_perf_policy_id**](PerformanceTemplatesApi.md#device_type2_remove_perf_policy_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/performance-policies/{performancePolicyId} | Remove performance-policies identified by {performancePolicyId} from Nimble / Alletra 6K


# **device_type2_get_all_performance_policies**
> NimblePerformancePolicyList device_type2_get_all_performance_policies(system_id)

Get all performance-policies details by Nimble / Alletra 6K

Get all performance-policies details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import performance_templates_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_performance_policy_list import NimblePerformancePolicyList
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
    api_instance = performance_templates_api.PerformanceTemplatesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter performance Policy by Key. (optional)
    sort = "name desc" # str | oData query to sort performance Policy resource by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all performance-policies details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_performance_policies(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling PerformanceTemplatesApi->device_type2_get_all_performance_policies: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all performance-policies details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_performance_policies(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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

# **device_type2_get_performance_policy_by_id**
> NimblePerformancePolicyDetailsWithRequestUri device_type2_get_performance_policy_by_id(system_id, performance_policy_id)

Get details of Nimble / Alletra 6K performance-policy identified by {performancePolicyId}

Get details of Nimble / Alletra 6K performance-policy identified by {performancePolicyId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import performance_templates_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.nimble_performance_policy_details_with_request_uri import NimblePerformancePolicyDetailsWithRequestUri
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
    api_instance = performance_templates_api.PerformanceTemplatesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    performance_policy_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the performance Policy. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K performance-policy identified by {performancePolicyId}
        api_response = api_instance.device_type2_get_performance_policy_by_id(system_id, performance_policy_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling PerformanceTemplatesApi->device_type2_get_performance_policy_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K performance-policy identified by {performancePolicyId}
        api_response = api_instance.device_type2_get_performance_policy_by_id(system_id, performance_policy_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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

# **device_type2_performance_policy_create**
> TaskResponse device_type2_performance_policy_create(system_id, nimble_create_performance_policy_input)

Create Nimble / Alletra 6K performance policy in a system identified by {systemId}

Create Nimble / Alletra 6K performance policy in a system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import performance_templates_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_create_performance_policy_input import NimbleCreatePerformancePolicyInput
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
    api_instance = performance_templates_api.PerformanceTemplatesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_create_performance_policy_input = NimbleCreatePerformancePolicyInput(
        app_category="Unassigned",
        block_size=4096,
        cache=True,
        cache_policy="normal",
        compress=True,
        dedupe_enabled=False,
        description="99.9999% availability",
        name="SQL Server Logs",
        space_policy="offline",
    ) # NimbleCreatePerformancePolicyInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create Nimble / Alletra 6K performance policy in a system identified by {systemId}
        api_response = api_instance.device_type2_performance_policy_create(system_id, nimble_create_performance_policy_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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

# **device_type2_performance_policy_edit**
> TaskResponse device_type2_performance_policy_edit(system_id, performance_policy_id, nimble_edit_performance_policy_input)

Edit details of Nimble / Alletra 6K performance policy identified by {performancePolicyId}

Edit details of Nimble / Alletra 6K performance policy identified by {performancePolicyId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import performance_templates_api
from greenlake_data_services.model.nimble_edit_performance_policy_input import NimbleEditPerformancePolicyInput
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
    api_instance = performance_templates_api.PerformanceTemplatesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    performance_policy_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the performance Policy. A 42 digit hexadecimal number.
    nimble_edit_performance_policy_input = NimbleEditPerformancePolicyInput(
        app_category="Unassigned",
        cache=True,
        cache_policy="normal",
        compress=True,
        dedupe_enabled=False,
        description="99.9999% availability",
        name="SQL Server Logs",
        space_policy="offline",
    ) # NimbleEditPerformancePolicyInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit details of Nimble / Alletra 6K performance policy identified by {performancePolicyId}
        api_response = api_instance.device_type2_performance_policy_edit(system_id, performance_policy_id, nimble_edit_performance_policy_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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

# **device_type2_remove_perf_policy_id**
> TaskResponse device_type2_remove_perf_policy_id(system_id, performance_policy_id)

Remove performance-policies identified by {performancePolicyId} from Nimble / Alletra 6K

Remove performance-policies identified by {performancePolicyId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import performance_templates_api
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
    api_instance = performance_templates_api.PerformanceTemplatesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    performance_policy_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the performance Policy. A 42 digit hexadecimal number.

    # example passing only required values which don't have defaults set
    try:
        # Remove performance-policies identified by {performancePolicyId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_perf_policy_id(system_id, performance_policy_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

