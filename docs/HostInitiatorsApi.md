# greenlake_data_services.HostInitiatorsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_get_all_initiators**](HostInitiatorsApi.md#device_type2_get_all_initiators) | **GET** /api/v1/storage-systems/device-type2/{systemId}/host-initiators | Get all nimble initiators details by Nimble / Alletra 6K
[**device_type2_get_initiators_by_id**](HostInitiatorsApi.md#device_type2_get_initiators_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/host-initiators/{hostInitiatorId} | Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorId}
[**device_type2_initiators_create**](HostInitiatorsApi.md#device_type2_initiators_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/host-initiators | Create Nimble / Alletra 6K nimble initiator in system identified by {systemId}
[**device_type2_remove_initiators_by_id**](HostInitiatorsApi.md#device_type2_remove_initiators_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/host-initiators/{hostInitiatorId} | Remove Nimble Initiator identified by {hostInitiatorId} from Nimble / Alletra 6K
[**host_create**](HostInitiatorsApi.md#host_create) | **POST** /api/v1/host-initiators | Create a host
[**host_delete**](HostInitiatorsApi.md#host_delete) | **DELETE** /api/v1/host-initiators/{hostId} | Delete a host by {hostId}
[**host_get_by_id**](HostInitiatorsApi.md#host_get_by_id) | **GET** /api/v1/host-initiators/{hostId} | Get the host details by {hostId}
[**host_initiator_create**](HostInitiatorsApi.md#host_initiator_create) | **POST** /api/v1/initiators | Create initiator
[**host_initiator_delete**](HostInitiatorsApi.md#host_initiator_delete) | **DELETE** /api/v1/initiators/{initiatorId} | Delete initiator by {initiatorId}
[**host_initiator_get_by_id**](HostInitiatorsApi.md#host_initiator_get_by_id) | **GET** /api/v1/initiators/{initiatorId} | Get the initiator details by {initiatorId}
[**host_initiator_list**](HostInitiatorsApi.md#host_initiator_list) | **GET** /api/v1/initiators | Get the list of initiators
[**host_list**](HostInitiatorsApi.md#host_list) | **GET** /api/v1/host-initiators | Get the list of hosts
[**host_update_by_id**](HostInitiatorsApi.md#host_update_by_id) | **PUT** /api/v1/host-initiators/{hostId} | Update Host by {hostId}
[**host_volume_performance_history_get**](HostInitiatorsApi.md#host_volume_performance_history_get) | **GET** /api/v1/host-initiators/{hostId}/storage-performance-history | Get the volume performance history data associated with a host identified by {uid}
[**host_volumes_get**](HostInitiatorsApi.md#host_volumes_get) | **GET** /api/v1/host-initiators/{hostId}/volumes | Get details of volumes associated with a host identified by {uid}


# **device_type2_get_all_initiators**
> NimbleInitiatorsList device_type2_get_all_initiators(system_id)

Get all nimble initiators details by Nimble / Alletra 6K

Get all nimble initiators details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_initiators_list import NimbleInitiatorsList
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter initiators by Key. (optional)
    sort = "initiator_group_name desc" # str | oData query to sort initiators resource by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all nimble initiators details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_initiators(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->device_type2_get_all_initiators: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all nimble initiators details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_initiators(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->device_type2_get_all_initiators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]
 **filter** | **str**| Lucene query to filter initiators by Key. | [optional]
 **sort** | **str**| oData query to sort initiators resource by Key. | [optional]
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NimbleInitiatorsList**](NimbleInitiatorsList.md)

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

# **device_type2_get_initiators_by_id**
> NimbleInitiatorDetails device_type2_get_initiators_by_id(system_id, host_initiator_id)

Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorId}

Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_initiator_details import NimbleInitiatorDetails
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    host_initiator_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the nimble initiator. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorId}
        api_response = api_instance.device_type2_get_initiators_by_id(system_id, host_initiator_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->device_type2_get_initiators_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorId}
        api_response = api_instance.device_type2_get_initiators_by_id(system_id, host_initiator_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->device_type2_get_initiators_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **host_initiator_id** | **str**| ID of the nimble initiator. A 42 digit hexadecimal number. |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NimbleInitiatorDetails**](NimbleInitiatorDetails.md)

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

# **device_type2_initiators_create**
> TaskResponse device_type2_initiators_create(system_id, nimble_create_initiator_input)

Create Nimble / Alletra 6K nimble initiator in system identified by {systemId}

Get all nimble initiators details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_create_initiator_input import NimbleCreateInitiatorInput
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_create_initiator_input = NimbleCreateInitiatorInput(
        access_protocol="iscsi",
        alias="my_initiator-4",
        chapuser_id="011c9973433673c3db000000000000000000000000",
        initiator_group_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        ip_address="iqn.2007-11.com.storage:zmytestvol1-v0df0fe6f7dc7bb16.0000016b.70374579",
        iqn="iqn.2007-11.com.storage:zmytestvol1-v0df0fe6f7dc7bb16.0000016b.70374579",
        label="myobject-5",
        override_existing_alias=True,
        wwpn="af:32:f1:20:bc:ba:43:1a",
    ) # NimbleCreateInitiatorInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create Nimble / Alletra 6K nimble initiator in system identified by {systemId}
        api_response = api_instance.device_type2_initiators_create(system_id, nimble_create_initiator_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->device_type2_initiators_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **nimble_create_initiator_input** | [**NimbleCreateInitiatorInput**](NimbleCreateInitiatorInput.md)|  |

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

# **device_type2_remove_initiators_by_id**
> TaskResponse device_type2_remove_initiators_by_id(system_id, host_initiator_id)

Remove Nimble Initiator identified by {hostInitiatorId} from Nimble / Alletra 6K

Remove Nimble Initiator identified by {hostInitiatorId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    host_initiator_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of Host Initiator. A 42 digit hexadecimal number.

    # example passing only required values which don't have defaults set
    try:
        # Remove Nimble Initiator identified by {hostInitiatorId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_initiators_by_id(system_id, host_initiator_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->device_type2_remove_initiators_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **host_initiator_id** | **str**| Identifier of Host Initiator. A 42 digit hexadecimal number. |

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

# **host_create**
> HostObject host_create(create_host_input)

Create a host

Create a host

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.create_host_input import CreateHostInput
from greenlake_data_services.model.host_object import HostObject
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    create_host_input = CreateHostInput(
        comment="comment1",
        contact="sanjay@hpe.com",
        fqdn="host1.hpe.com",
        host_group_ids=[
            "host_group_ids_example",
        ],
        initiator_ids=[
            "initiator_ids_example",
        ],
        initiators_to_create=[
            InitiatorInput(
                address="100008F1EABFE61C",
                driver_version="4.1",
                firmware_version="10.0",
                hba_model="model-5",
                host_speed=1000,
                ip_address="15.212.100.100",
                name="init1",
                protocol="iSCSI",
                vendor="hpe",
            ),
        ],
        ip_address="15.212.100.100",
        location="India",
        model="model1",
        name="host1",
        operating_system="Windows Server",
        persona="AIX-Legacy",
        protocol="protocol1",
        subnet="255.255.255.0",
        user_created=True,
    ) # CreateHostInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create a host
        api_response = api_instance.host_create(create_host_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_host_input** | [**CreateHostInput**](CreateHostInput.md)|  |

### Return type

[**HostObject**](HostObject.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_delete**
> TaskResponse host_delete(host_id)

Delete a host by {hostId}

Delete a host by {hostId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    host_id = "2b09e744496246859fde6c132b2091d3" # str | Id of the SC Host.
    force = True # bool | Forceful delete option (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a host by {hostId}
        api_response = api_instance.host_delete(host_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a host by {hostId}
        api_response = api_instance.host_delete(host_id, force=force)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the SC Host. |
 **force** | **bool**| Forceful delete option | [optional]

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

# **host_get_by_id**
> HostDetails host_get_by_id(host_id)

Get the host details by {hostId}

Get the host details by {hostId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.host_details import HostDetails
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    host_id = "2b09e744496246859fde6c132b2091d3" # str | Id of the SC Host.

    # example passing only required values which don't have defaults set
    try:
        # Get the host details by {hostId}
        api_response = api_instance.host_get_by_id(host_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the SC Host. |

### Return type

[**HostDetails**](HostDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - Current entity tag for the selected resource <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_initiator_create**
> Initiator host_initiator_create(initiator_input)

Create initiator

Create initiator

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.initiator_input import InitiatorInput
from greenlake_data_services.model.initiator import Initiator
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    initiator_input = InitiatorInput(
        address="100008F1EABFE61C",
        driver_version="4.1",
        firmware_version="10.0",
        hba_model="model-5",
        host_speed=1000,
        ip_address="15.212.100.100",
        name="init1",
        protocol="iSCSI",
        vendor="hpe",
    ) # InitiatorInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create initiator
        api_response = api_instance.host_initiator_create(initiator_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_initiator_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initiator_input** | [**InitiatorInput**](InitiatorInput.md)|  |

### Return type

[**Initiator**](Initiator.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_initiator_delete**
> DeleteInitiator host_initiator_delete(initiator_id)

Delete initiator by {initiatorId}

Delete initiator by {initiatorId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.delete_initiator import DeleteInitiator
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    initiator_id = "e789e756496246859fde6c132b2091d3" # str | UID of SC Initiator.

    # example passing only required values which don't have defaults set
    try:
        # Delete initiator by {initiatorId}
        api_response = api_instance.host_initiator_delete(initiator_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_initiator_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initiator_id** | **str**| UID of SC Initiator. |

### Return type

[**DeleteInitiator**](DeleteInitiator.md)

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

# **host_initiator_get_by_id**
> InitiatorDetails host_initiator_get_by_id(initiator_id)

Get the initiator details by {initiatorId}

Get the initiator details by {initiatorId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.initiator_details import InitiatorDetails
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    initiator_id = "e789e756496246859fde6c132b2091d3" # str | UID of SC Initiator.

    # example passing only required values which don't have defaults set
    try:
        # Get the initiator details by {initiatorId}
        api_response = api_instance.host_initiator_get_by_id(initiator_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_initiator_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **initiator_id** | **str**| UID of SC Initiator. |

### Return type

[**InitiatorDetails**](InitiatorDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - Current entity tag for the selected resource <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_initiator_list**
> InitiatorList host_initiator_list()

Get the list of initiators

Get the list of initiators

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.initiator_list import InitiatorList
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | oData query to filter hostservice by Key. (optional)
    sort = "name desc" # str | oData query to sort hostservice by Key. (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of initiators
        api_response = api_instance.host_initiator_list(filter=filter, sort=sort, limit=limit, offset=offset)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_initiator_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| oData query to filter hostservice by Key. | [optional]
 **sort** | **str**| oData query to sort hostservice by Key. | [optional]
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]

### Return type

[**InitiatorList**](InitiatorList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - Current entity tag for the selected resource <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_list**
> HostsList host_list()

Get the list of hosts

Get the list of hosts

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.hosts_list import HostsList
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | oData query to filter hostservice by Key. (optional)
    sort = "name desc" # str | oData query to sort hostservice by Key. (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of hosts
        api_response = api_instance.host_list(filter=filter, sort=sort, limit=limit, offset=offset)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| oData query to filter hostservice by Key. | [optional]
 **sort** | **str**| oData query to sort hostservice by Key. | [optional]
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]

### Return type

[**HostsList**](HostsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  * ETag - Current entity tag for the selected resource <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_update_by_id**
> TaskResponse host_update_by_id(host_id, update_host_input)

Update Host by {hostId}

Update host details by {hostId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from greenlake_data_services.model.update_host_input import UpdateHostInput
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    host_id = "2b09e744496246859fde6c132b2091d3" # str | Id of the SC Host.
    update_host_input = UpdateHostInput(
        initiators_to_create=[
            InitiatorInput(
                address="100008F1EABFE61C",
                driver_version="4.1",
                firmware_version="10.0",
                hba_model="model-5",
                host_speed=1000,
                ip_address="15.212.100.100",
                name="init1",
                protocol="iSCSI",
                vendor="hpe",
            ),
        ],
        name="host1",
        updated_initiators=[
            "updated_initiators_example",
        ],
    ) # UpdateHostInput | 

    # example passing only required values which don't have defaults set
    try:
        # Update Host by {hostId}
        api_response = api_instance.host_update_by_id(host_id, update_host_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_update_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the SC Host. |
 **update_host_input** | [**UpdateHostInput**](UpdateHostInput.md)|  |

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

# **host_volume_performance_history_get**
> HostStoragePerformanceHistory host_volume_performance_history_get(host_id)

Get the volume performance history data associated with a host identified by {uid}

Get the volume performance history data associated with a host identified by {uid}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.host_storage_performance_history import HostStoragePerformanceHistory
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    host_id = "2b09e744496246859fde6c132b2091d3" # str | Id of the SC Host.
    select = "latencyMetricsDataMs" # str | Query to select only the required parameters, separated by . if nested (optional)
    range = "startTime eq 1605063600 and endTime eq 1605186000" # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 1440 # int | It defines granularity in minutes. (optional) if omitted the server will use the default value of 1440
    top_volumes_count = 5 # int | The number of top volumes to be returned, by default it will be 5 (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the volume performance history data associated with a host identified by {uid}
        api_response = api_instance.host_volume_performance_history_get(host_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_volume_performance_history_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the volume performance history data associated with a host identified by {uid}
        api_response = api_instance.host_volume_performance_history_get(host_id, select=select, range=range, time_interval_min=time_interval_min, top_volumes_count=top_volumes_count)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_volume_performance_history_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the SC Host. |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]
 **range** | **str**| range will define start and end time in which query has to be made. | [optional]
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] if omitted the server will use the default value of 1440
 **top_volumes_count** | **int**| The number of top volumes to be returned, by default it will be 5 | [optional]

### Return type

[**HostStoragePerformanceHistory**](HostStoragePerformanceHistory.md)

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

# **host_volumes_get**
> HostStorageVolumes host_volumes_get(host_id)

Get details of volumes associated with a host identified by {uid}

Get details of volumes associated with a host identified by {uid}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiators_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.host_storage_volumes import HostStorageVolumes
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
    api_instance = host_initiators_api.HostInitiatorsApi(api_client)
    host_id = "2b09e744496246859fde6c132b2091d3" # str | Id of the SC Host.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of volumes associated with a host identified by {uid}
        api_response = api_instance.host_volumes_get(host_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_volumes_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of volumes associated with a host identified by {uid}
        api_response = api_instance.host_volumes_get(host_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorsApi->host_volumes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the SC Host. |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**HostStorageVolumes**](HostStorageVolumes.md)

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

