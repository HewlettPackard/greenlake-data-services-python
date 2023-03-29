# greenlake_data_services.ControllersApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_node_batteries_get_by_id**](ControllersApi.md#device_type1_node_batteries_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/nodes-batteries/{id} | Get details of Primera / Alletra 9K Node Battery identified by {nodeId} and {id}
[**device_type1_node_batteries_list**](ControllersApi.md#device_type1_node_batteries_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/nodes-batteries | Get details of Primera / Alletra 9K Node Batteries identified by {nodeId}
[**device_type1_node_cards_get_by_id**](ControllersApi.md#device_type1_node_cards_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-cards/{id} | Get details of Primera / Alletra 9K Node Card identified by {nodeId} and {id}
[**device_type1_node_cards_list**](ControllersApi.md#device_type1_node_cards_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-cards | Get details of Primera / Alletra 9K Node Cards identified by {nodeId}
[**device_type1_node_component_performance_statistics_get**](ControllersApi.md#device_type1_node_component_performance_statistics_get) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/component-performance-statistics | Get component performance statistics details of Primera / Alletra 9K node idenfified by {nodeId}
[**device_type1_node_cpus_get_by_id**](ControllersApi.md#device_type1_node_cpus_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-cpus/{id} | Get details of Primera / Alletra 9K Node Cpu identified by {nodeId} and {id}
[**device_type1_node_cpus_list**](ControllersApi.md#device_type1_node_cpus_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-cpus | Get details of Primera / Alletra 9K Node Cpus identified by {nodeId}
[**device_type1_node_drives_get_by_id**](ControllersApi.md#device_type1_node_drives_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-drives/{id} | Get details of Primera / Alletra 9K Node Drive identified by {nodeId} and {id}
[**device_type1_node_drives_list**](ControllersApi.md#device_type1_node_drives_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-drives | Get details of Primera / Alletra 9K Node Drives identified by {nodeId}
[**device_type1_node_mcus_get_by_id**](ControllersApi.md#device_type1_node_mcus_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-mcus/{id} | Get details of Primera / Alletra 9K Node Mcu identified by {nodeId} and {id}
[**device_type1_node_mcus_list**](ControllersApi.md#device_type1_node_mcus_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-mcus | Get details of Primera / Alletra 9K Node Mcus identified by {nodeId}
[**device_type1_node_mems_get_by_id**](ControllersApi.md#device_type1_node_mems_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-mems/{id} | Get details of Primera / Alletra 9K Node Memory identified by {nodeId} and {id}
[**device_type1_node_mems_list**](ControllersApi.md#device_type1_node_mems_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-mems | Get details of Primera / Alletra 9K Node Memories identified by {nodeId}
[**device_type1_node_powers_get_by_id**](ControllersApi.md#device_type1_node_powers_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-powers/{id} | Get details of Primera / Alletra 9K Node Power Supply identified by {nodeId} and {id}
[**device_type1_node_powers_list**](ControllersApi.md#device_type1_node_powers_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-powers | Get details of Primera / Alletra 9K Node Power Supplies identified by {nodeId}
[**device_type1_nodes_get_by_id**](ControllersApi.md#device_type1_nodes_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes/{id} | Get details of Primera / Alletra 9K Node identified by {id}
[**device_type1_nodes_list**](ControllersApi.md#device_type1_nodes_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/nodes | Get details of Primera / Alletra 9K Nodes
[**device_type2_controller_halt**](ControllersApi.md#device_type2_controller_halt) | **POST** /api/v1/storage-systems/device-type2/{systemId}/controllers/{controllerId}/actions/halt | Perform halt of Nimble / Alletra 6K controller identified by {controllerId}
[**device_type2_get_all_controllers**](ControllersApi.md#device_type2_get_all_controllers) | **GET** /api/v1/storage-systems/device-type2/{systemId}/controllers | Get all controllers details by Nimble / Alletra 6K
[**device_type2_get_controller_by_id**](ControllersApi.md#device_type2_get_controller_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/controllers/{controllerId} | Get details of Nimble / Alletra 6K Controller identified by {controllerId}
[**node_powers_locate_pcmbby_id**](ControllersApi.md#node_powers_locate_pcmbby_id) | **POST** /api/v1/storage-systems/device-type1/{systemId}/nodes/{nodeId}/node-powers/{id} | Locate PCBM of Primera / Alletra 9K identified by {id}
[**nodes_locate_by_id**](ControllersApi.md#nodes_locate_by_id) | **POST** /api/v1/storage-systems/device-type1/{systemId}/nodes/{id} | Locate node of Primera / Alletra 9K identified by {id}


# **device_type1_node_batteries_get_by_id**
> NodeBatteryDetails device_type1_node_batteries_get_by_id(system_id, node_id, id)

Get details of Primera / Alletra 9K Node Battery identified by {nodeId} and {id}

Get details of Primera / Alletra 9K Node Battery identified by {nodeId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.node_battery_details import NodeBatteryDetails
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | Primary ID of the node
    id = "8621946048c1cb24bdfc57e9b3b460ac" # str | UID of the node battery
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Battery identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_batteries_get_by_id(system_id, node_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_batteries_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Battery identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_batteries_get_by_id(system_id, node_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_batteries_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| Primary ID of the node |
 **id** | **str**| UID of the node battery |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodeBatteryDetails**](NodeBatteryDetails.md)

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

# **device_type1_node_batteries_list**
> NodeBatteriesSummaryList device_type1_node_batteries_list(system_id, node_id)

Get details of Primera / Alletra 9K Node Batteries identified by {nodeId}

Get details of Primera / Alletra 9K Node Batteries identified by {nodeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.node_batteries_summary_list import NodeBatteriesSummaryList
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | Primary ID of the node
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "systemUid eq 7CE751P312" # str | oData query to filter nodes resource by key. (optional)
    sort = "systemId desc" # str | oData query to sort nodes resource by key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Batteries identified by {nodeId}
        api_response = api_instance.device_type1_node_batteries_list(system_id, node_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_batteries_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Batteries identified by {nodeId}
        api_response = api_instance.device_type1_node_batteries_list(system_id, node_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_batteries_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| Primary ID of the node |
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]
 **filter** | **str**| oData query to filter nodes resource by key. | [optional]
 **sort** | **str**| oData query to sort nodes resource by key. | [optional]
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodeBatteriesSummaryList**](NodeBatteriesSummaryList.md)

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

# **device_type1_node_cards_get_by_id**
> NodeCardDetails device_type1_node_cards_get_by_id(system_id, node_id, id)

Get details of Primera / Alletra 9K Node Card identified by {nodeId} and {id}

Get details of Primera / Alletra 9K Node Card identified by {nodeId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.node_card_details import NodeCardDetails
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    id = "9aeec8a12315995e1efc340a79b6b5bd" # str | UID of the node Card
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Card identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_cards_get_by_id(system_id, node_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_cards_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Card identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_cards_get_by_id(system_id, node_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_cards_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| UID of the node |
 **id** | **str**| UID of the node Card |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodeCardDetails**](NodeCardDetails.md)

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

# **device_type1_node_cards_list**
> NodeCardsSummaryList device_type1_node_cards_list(system_id, node_id)

Get details of Primera / Alletra 9K Node Cards identified by {nodeId}

Get details of Primera / Alletra 9K Node Cards identified by {nodeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.node_cards_summary_list import NodeCardsSummaryList
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "systemUid eq 7CE751P312" # str | oData query to filter nodes resource by key. (optional)
    sort = "systemId desc" # str | oData query to sort nodes resource by key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Cards identified by {nodeId}
        api_response = api_instance.device_type1_node_cards_list(system_id, node_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_cards_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Cards identified by {nodeId}
        api_response = api_instance.device_type1_node_cards_list(system_id, node_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_cards_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| UID of the node |
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]
 **filter** | **str**| oData query to filter nodes resource by key. | [optional]
 **sort** | **str**| oData query to sort nodes resource by key. | [optional]
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodeCardsSummaryList**](NodeCardsSummaryList.md)

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

# **device_type1_node_component_performance_statistics_get**
> NodePerfStats device_type1_node_component_performance_statistics_get(system_id, node_id)

Get component performance statistics details of Primera / Alletra 9K node idenfified by {nodeId}

Get component performance statistics details of Primera / Alletra 9K node idenfified by {nodeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.node_perf_stats import NodePerfStats
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get component performance statistics details of Primera / Alletra 9K node idenfified by {nodeId}
        api_response = api_instance.device_type1_node_component_performance_statistics_get(system_id, node_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_component_performance_statistics_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get component performance statistics details of Primera / Alletra 9K node idenfified by {nodeId}
        api_response = api_instance.device_type1_node_component_performance_statistics_get(system_id, node_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_component_performance_statistics_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| UID of the node |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodePerfStats**](NodePerfStats.md)

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

# **device_type1_node_cpus_get_by_id**
> NodesCpuDetails device_type1_node_cpus_get_by_id(system_id, node_id, id)

Get details of Primera / Alletra 9K Node Cpu identified by {nodeId} and {id}

Get details of Primera / Alletra 9K Node Cpu identified by {nodeId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nodes_cpu_details import NodesCpuDetails
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    id = "60c3831bf1e682693d0319c10333af92" # str | UID of the node Cpu
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Cpu identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_cpus_get_by_id(system_id, node_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_cpus_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Cpu identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_cpus_get_by_id(system_id, node_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_cpus_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| UID of the node |
 **id** | **str**| UID of the node Cpu |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodesCpuDetails**](NodesCpuDetails.md)

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

# **device_type1_node_cpus_list**
> NodeCpusSummaryList device_type1_node_cpus_list(system_id, node_id)

Get details of Primera / Alletra 9K Node Cpus identified by {nodeId}

Get details of Primera / Alletra 9K Node Cpus identified by {nodeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.node_cpus_summary_list import NodeCpusSummaryList
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "systemUid eq 7CE751P312" # str | oData query to filter nodes resource by key. (optional)
    sort = "systemId desc" # str | oData query to sort nodes resource by key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Cpus identified by {nodeId}
        api_response = api_instance.device_type1_node_cpus_list(system_id, node_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_cpus_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Cpus identified by {nodeId}
        api_response = api_instance.device_type1_node_cpus_list(system_id, node_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_cpus_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| UID of the node |
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]
 **filter** | **str**| oData query to filter nodes resource by key. | [optional]
 **sort** | **str**| oData query to sort nodes resource by key. | [optional]
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodeCpusSummaryList**](NodeCpusSummaryList.md)

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

# **device_type1_node_drives_get_by_id**
> NodeDriveDetails device_type1_node_drives_get_by_id(system_id, node_id, id)

Get details of Primera / Alletra 9K Node Drive identified by {nodeId} and {id}

Get details of Primera / Alletra 9K Node Drive identified by {nodeId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.node_drive_details import NodeDriveDetails
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    id = "b7b233212d3ed5608da55539a7008b5b" # str | UID of the node drive
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Drive identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_drives_get_by_id(system_id, node_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_drives_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Drive identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_drives_get_by_id(system_id, node_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_drives_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| UID of the node |
 **id** | **str**| UID of the node drive |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodeDriveDetails**](NodeDriveDetails.md)

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

# **device_type1_node_drives_list**
> NodeDrivesSummaryList device_type1_node_drives_list(system_id, node_id)

Get details of Primera / Alletra 9K Node Drives identified by {nodeId}

Get details of Primera / Alletra 9K Node Drives identified by {nodeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.node_drives_summary_list import NodeDrivesSummaryList
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "systemUid eq 7CE751P312" # str | oData query to filter nodes resource by key. (optional)
    sort = "systemId desc" # str | oData query to sort nodes resource by key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Drives identified by {nodeId}
        api_response = api_instance.device_type1_node_drives_list(system_id, node_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_drives_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Drives identified by {nodeId}
        api_response = api_instance.device_type1_node_drives_list(system_id, node_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_drives_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| UID of the node |
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]
 **filter** | **str**| oData query to filter nodes resource by key. | [optional]
 **sort** | **str**| oData query to sort nodes resource by key. | [optional]
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodeDrivesSummaryList**](NodeDrivesSummaryList.md)

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

# **device_type1_node_mcus_get_by_id**
> NodeMcuDetails device_type1_node_mcus_get_by_id(system_id, node_id, id)

Get details of Primera / Alletra 9K Node Mcu identified by {nodeId} and {id}

Get details of Primera / Alletra 9K Node Mcu identified by {nodeId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.node_mcu_details import NodeMcuDetails
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    id = "be97ad7351f8562440c909460061d0cb" # str | UID of the node Mcu
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Mcu identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_mcus_get_by_id(system_id, node_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_mcus_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Mcu identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_mcus_get_by_id(system_id, node_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_mcus_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| UID of the node |
 **id** | **str**| UID of the node Mcu |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodeMcuDetails**](NodeMcuDetails.md)

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

# **device_type1_node_mcus_list**
> NodeMcusSummaryList device_type1_node_mcus_list(system_id, node_id)

Get details of Primera / Alletra 9K Node Mcus identified by {nodeId}

Get details of Primera / Alletra 9K Node Mcus identified by {nodeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.node_mcus_summary_list import NodeMcusSummaryList
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "systemUid eq 7CE751P312" # str | oData query to filter nodes resource by key. (optional)
    sort = "systemId desc" # str | oData query to sort nodes resource by key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Mcus identified by {nodeId}
        api_response = api_instance.device_type1_node_mcus_list(system_id, node_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_mcus_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Mcus identified by {nodeId}
        api_response = api_instance.device_type1_node_mcus_list(system_id, node_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_mcus_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| UID of the node |
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]
 **filter** | **str**| oData query to filter nodes resource by key. | [optional]
 **sort** | **str**| oData query to sort nodes resource by key. | [optional]
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodeMcusSummaryList**](NodeMcusSummaryList.md)

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

# **device_type1_node_mems_get_by_id**
> NodeMemoryDetails device_type1_node_mems_get_by_id(system_id, node_id, id)

Get details of Primera / Alletra 9K Node Memory identified by {nodeId} and {id}

Get details of Primera / Alletra 9K Node Memory identified by {nodeId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.node_memory_details import NodeMemoryDetails
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    id = "cc43b7fdca33ea82d84e0ca260940483" # str | UID of the node Memory
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Memory identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_mems_get_by_id(system_id, node_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_mems_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Memory identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_mems_get_by_id(system_id, node_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_mems_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| UID of the node |
 **id** | **str**| UID of the node Memory |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodeMemoryDetails**](NodeMemoryDetails.md)

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

# **device_type1_node_mems_list**
> NodesMemorySummaryList device_type1_node_mems_list(system_id, node_id)

Get details of Primera / Alletra 9K Node Memories identified by {nodeId}

Get details of Primera / Alletra 9K Node Memories identified by {nodeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nodes_memory_summary_list import NodesMemorySummaryList
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "systemUid eq 7CE751P312" # str | oData query to filter nodes resource by key. (optional)
    sort = "systemId desc" # str | oData query to sort nodes resource by key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Memories identified by {nodeId}
        api_response = api_instance.device_type1_node_mems_list(system_id, node_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_mems_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Memories identified by {nodeId}
        api_response = api_instance.device_type1_node_mems_list(system_id, node_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_mems_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| UID of the node |
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]
 **filter** | **str**| oData query to filter nodes resource by key. | [optional]
 **sort** | **str**| oData query to sort nodes resource by key. | [optional]
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodesMemorySummaryList**](NodesMemorySummaryList.md)

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

# **device_type1_node_powers_get_by_id**
> NodePowerSupplyDetails device_type1_node_powers_get_by_id(system_id, node_id, id)

Get details of Primera / Alletra 9K Node Power Supply identified by {nodeId} and {id}

Get details of Primera / Alletra 9K Node Power Supply identified by {nodeId} and {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.node_power_supply_details import NodePowerSupplyDetails
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | Primary ID of the node
    id = "1f9624301fd2f5ecef723c6ecd17c377" # str | UID of the node Power Supply
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Power Supply identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_powers_get_by_id(system_id, node_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_powers_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Power Supply identified by {nodeId} and {id}
        api_response = api_instance.device_type1_node_powers_get_by_id(system_id, node_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_powers_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| Primary ID of the node |
 **id** | **str**| UID of the node Power Supply |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodePowerSupplyDetails**](NodePowerSupplyDetails.md)

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

# **device_type1_node_powers_list**
> NodesPowerSummaryList device_type1_node_powers_list(system_id, node_id)

Get details of Primera / Alletra 9K Node Power Supplies identified by {nodeId}

Get details of Primera / Alletra 9K Node Power Supplies identified by {nodeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nodes_power_summary_list import NodesPowerSummaryList
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | Primary ID of the node
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "systemUid eq 7CE751P312" # str | oData query to filter nodes resource by key. (optional)
    sort = "systemId desc" # str | oData query to sort nodes resource by key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node Power Supplies identified by {nodeId}
        api_response = api_instance.device_type1_node_powers_list(system_id, node_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_powers_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node Power Supplies identified by {nodeId}
        api_response = api_instance.device_type1_node_powers_list(system_id, node_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_node_powers_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| Primary ID of the node |
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]
 **filter** | **str**| oData query to filter nodes resource by key. | [optional]
 **sort** | **str**| oData query to sort nodes resource by key. | [optional]
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodesPowerSummaryList**](NodesPowerSummaryList.md)

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

# **device_type1_nodes_get_by_id**
> NodeDetails device_type1_nodes_get_by_id(system_id, id)

Get details of Primera / Alletra 9K Node identified by {id}

Get details of Primera / Alletra 9K Node identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.node_details import NodeDetails
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Node identified by {id}
        api_response = api_instance.device_type1_nodes_get_by_id(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_nodes_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Node identified by {id}
        api_response = api_instance.device_type1_nodes_get_by_id(system_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_nodes_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **id** | **str**| UID of the node |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodeDetails**](NodeDetails.md)

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

# **device_type1_nodes_list**
> NodesSummaryList device_type1_nodes_list(system_id)

Get details of Primera / Alletra 9K Nodes

Get details of Primera / Alletra 9K Nodes

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nodes_summary_list import NodesSummaryList
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "systemUid eq 7CE751P312" # str | oData query to filter nodes resource by key. (optional)
    sort = "systemId desc" # str | oData query to sort nodes resource by key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Nodes
        api_response = api_instance.device_type1_nodes_list(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_nodes_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Nodes
        api_response = api_instance.device_type1_nodes_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type1_nodes_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]
 **filter** | **str**| oData query to filter nodes resource by key. | [optional]
 **sort** | **str**| oData query to sort nodes resource by key. | [optional]
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NodesSummaryList**](NodesSummaryList.md)

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

# **device_type2_controller_halt**
> TaskResponse device_type2_controller_halt(system_id, controller_id)

Perform halt of Nimble / Alletra 6K controller identified by {controllerId}

Perform halt of Nimble / Alletra 6K controller identified by {controllerId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    controller_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the controller. A 42 digit hexadecimal number.

    # example passing only required values which don't have defaults set
    try:
        # Perform halt of Nimble / Alletra 6K controller identified by {controllerId}
        api_response = api_instance.device_type2_controller_halt(system_id, controller_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type2_controller_halt: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **controller_id** | **str**| ID of the controller. A 42 digit hexadecimal number. |

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

# **device_type2_get_all_controllers**
> NimbleControllerList device_type2_get_all_controllers(system_id)

Get all controllers details by Nimble / Alletra 6K

Get all controllers details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_controller_list import NimbleControllerList
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter controllers by Key. (optional)
    sort = "name desc" # str | oData query to sort controllers resource by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all controllers details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_controllers(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type2_get_all_controllers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all controllers details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_controllers(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type2_get_all_controllers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]
 **filter** | **str**| Lucene query to filter controllers by Key. | [optional]
 **sort** | **str**| oData query to sort controllers resource by Key. | [optional]
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NimbleControllerList**](NimbleControllerList.md)

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

# **device_type2_get_controller_by_id**
> NimbleControllerDetailsWithRequestUri device_type2_get_controller_by_id(system_id, controller_id)

Get details of Nimble / Alletra 6K Controller identified by {controllerId}

Get details of Nimble / Alletra 6K Controller identified by {controllerId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_controller_details_with_request_uri import NimbleControllerDetailsWithRequestUri
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    controller_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the controller. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K Controller identified by {controllerId}
        api_response = api_instance.device_type2_get_controller_by_id(system_id, controller_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type2_get_controller_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K Controller identified by {controllerId}
        api_response = api_instance.device_type2_get_controller_by_id(system_id, controller_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->device_type2_get_controller_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **controller_id** | **str**| ID of the controller. A 42 digit hexadecimal number. |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NimbleControllerDetailsWithRequestUri**](NimbleControllerDetailsWithRequestUri.md)

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

# **node_powers_locate_pcmbby_id**
> TaskResponse node_powers_locate_pcmbby_id(system_id, node_id, id, locate_input)

Locate PCBM of Primera / Alletra 9K identified by {id}

Locate PCBM of Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.locate_input import LocateInput
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    node_id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | Primary ID of the node
    id = "1f9624301fd2f5ecef723c6ecd17c377" # str | UID of the node Power Supply
    locate_input = LocateInput(
        locate=True,
    ) # LocateInput | 

    # example passing only required values which don't have defaults set
    try:
        # Locate PCBM of Primera / Alletra 9K identified by {id}
        api_response = api_instance.node_powers_locate_pcmbby_id(system_id, node_id, id, locate_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->node_powers_locate_pcmbby_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **node_id** | **str**| Primary ID of the node |
 **id** | **str**| UID of the node Power Supply |
 **locate_input** | [**LocateInput**](LocateInput.md)|  |

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

# **nodes_locate_by_id**
> TaskResponse nodes_locate_by_id(system_id, id, locate_input)

Locate node of Primera / Alletra 9K identified by {id}

Locate node of Primera / Alletra 9K identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import controllers_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.locate_input import LocateInput
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
    api_instance = controllers_api.ControllersApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "e9d353bf98fc1a6bdb90b824e3ca14b5" # str | UID of the node
    locate_input = LocateInput(
        locate=True,
    ) # LocateInput | 

    # example passing only required values which don't have defaults set
    try:
        # Locate node of Primera / Alletra 9K identified by {id}
        api_response = api_instance.nodes_locate_by_id(system_id, id, locate_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling ControllersApi->nodes_locate_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system |
 **id** | **str**| UID of the node |
 **locate_input** | [**LocateInput**](LocateInput.md)|  |

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

