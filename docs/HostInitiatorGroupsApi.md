# greenlake_data_services.HostInitiatorGroupsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_get_all_host_initiator_groups**](HostInitiatorGroupsApi.md#device_type2_get_all_host_initiator_groups) | **GET** /api/v1/storage-systems/device-type2/{systemId}/host-groups | Get all nimble host initiator groups details by Nimble / Alletra 6K
[**device_type2_get_host_initiator_group_by_id**](HostInitiatorGroupsApi.md#device_type2_get_host_initiator_group_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/host-groups/{hostInitiatorGroupId} | Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}
[**device_type2_host_initiator_group_create**](HostInitiatorGroupsApi.md#device_type2_host_initiator_group_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/host-groups | Create Nimble / Alletra 6K initiator group in system identified by {systemId}
[**device_type2_remove_host_initiator_group_by_id**](HostInitiatorGroupsApi.md#device_type2_remove_host_initiator_group_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/host-groups/{hostInitiatorGroupId} | Remove initiator-groups identified by {hostInitiatorGroupId} from Nimble / Alletra 6K
[**device_type2_update_host_initiator_group_by_id**](HostInitiatorGroupsApi.md#device_type2_update_host_initiator_group_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/host-groups/{hostInitiatorGroupId} | Update initiator-groups identified by {hostInitiatorGroupId}
[**host_group_create**](HostInitiatorGroupsApi.md#host_group_create) | **POST** /api/v1/host-initiator-groups | Create a host group
[**host_group_delete**](HostInitiatorGroupsApi.md#host_group_delete) | **DELETE** /api/v1/host-initiator-groups/{hostGroupId} | Delete a host group by {hostGroupId}
[**host_group_get_by_id**](HostInitiatorGroupsApi.md#host_group_get_by_id) | **GET** /api/v1/host-initiator-groups/{hostGroupId} | Get the host group details by {hostGroupId}
[**host_group_list**](HostInitiatorGroupsApi.md#host_group_list) | **GET** /api/v1/host-initiator-groups | Get the list of host groups
[**host_group_update_by_id**](HostInitiatorGroupsApi.md#host_group_update_by_id) | **PUT** /api/v1/host-initiator-groups/{hostGroupId} | Update host group by {hostGroupId}


# **device_type2_get_all_host_initiator_groups**
> NimbleInitiatorGroupList device_type2_get_all_host_initiator_groups(system_id)

Get all nimble host initiator groups details by Nimble / Alletra 6K

Get all nimble host initiator groups details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiator_groups_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_initiator_group_list import NimbleInitiatorGroupList
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
    api_instance = host_initiator_groups_api.HostInitiatorGroupsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter initiator groups by Key. (optional)
    sort = "name desc" # str | oData query to sort initiator groups resource by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all nimble host initiator groups details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_host_initiator_groups(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->device_type2_get_all_host_initiator_groups: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all nimble host initiator groups details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_host_initiator_groups(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->device_type2_get_all_host_initiator_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]
 **filter** | **str**| Lucene query to filter initiator groups by Key. | [optional]
 **sort** | **str**| oData query to sort initiator groups resource by Key. | [optional]
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NimbleInitiatorGroupList**](NimbleInitiatorGroupList.md)

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

# **device_type2_get_host_initiator_group_by_id**
> NimbleInitiatorGroupDetails device_type2_get_host_initiator_group_by_id(system_id, host_initiator_group_id)

Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}

Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiator_groups_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_initiator_group_details import NimbleInitiatorGroupDetails
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
    api_instance = host_initiator_groups_api.HostInitiatorGroupsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    host_initiator_group_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | Identifier of initiator group. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}
        api_response = api_instance.device_type2_get_host_initiator_group_by_id(system_id, host_initiator_group_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->device_type2_get_host_initiator_group_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}
        api_response = api_instance.device_type2_get_host_initiator_group_by_id(system_id, host_initiator_group_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->device_type2_get_host_initiator_group_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **host_initiator_group_id** | **str**| Identifier of initiator group. A 42 digit hexadecimal number. |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NimbleInitiatorGroupDetails**](NimbleInitiatorGroupDetails.md)

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

# **device_type2_host_initiator_group_create**
> TaskResponse device_type2_host_initiator_group_create(system_id, nimble_create_initiator_group_input)

Create Nimble / Alletra 6K initiator group in system identified by {systemId}

Create Nimble / Alletra 6K initiator group in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiator_groups_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_create_initiator_group_input import NimbleCreateInitiatorGroupInput
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
    api_instance = host_initiator_groups_api.HostInitiatorGroupsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_create_initiator_group_input = NimbleCreateInitiatorGroupInput(
        access_protocol="iscsi",
        app_uuid="rfc4122.943f7dc1-5853-497c-b530-f689ccf1bf18",
        description="99.9999% availability",
        fc_initiators=[
            NimbleFCInitiator(
                alias="vegaalias",
                id="0b1c9973433673c3db000000000000000000000001",
                wwpn="0b1c9973433673c3db000000000000000000000001",
            ),
        ],
        fc_tdz_ports=[
            NimbleFCTdzPorts(
                array_name="myobject-5",
                fc_name="myobject-5",
            ),
        ],
        host_type="myobject-5",
        iscsi_initiators=[
            NimbleISCSIInitiator(
                id="021c9973433673c3db000000000000000000000001",
                ip_address="xx.xxx.xx.xx",
                iqn="vegaiqn",
                label="vega",
            ),
        ],
        metadata=[
            NimbleMetadata(
                key="vega-key",
                value="vega-value",
            ),
        ],
        name="myobject-5",
        target_subnets=[
            NimbleTargetSubnets(
                id="021c9973433673c3db000000000000000000000003",
                label="myobject-5",
            ),
        ],
    ) # NimbleCreateInitiatorGroupInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create Nimble / Alletra 6K initiator group in system identified by {systemId}
        api_response = api_instance.device_type2_host_initiator_group_create(system_id, nimble_create_initiator_group_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->device_type2_host_initiator_group_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **nimble_create_initiator_group_input** | [**NimbleCreateInitiatorGroupInput**](NimbleCreateInitiatorGroupInput.md)|  |

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

# **device_type2_remove_host_initiator_group_by_id**
> TaskResponse device_type2_remove_host_initiator_group_by_id(system_id, host_initiator_group_id)

Remove initiator-groups identified by {hostInitiatorGroupId} from Nimble / Alletra 6K

Remove initiator-groups identified by {hostInitiatorGroupId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiator_groups_api
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
    api_instance = host_initiator_groups_api.HostInitiatorGroupsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    host_initiator_group_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | Identifier of initiator group. A 42 digit hexadecimal number.

    # example passing only required values which don't have defaults set
    try:
        # Remove initiator-groups identified by {hostInitiatorGroupId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_host_initiator_group_by_id(system_id, host_initiator_group_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->device_type2_remove_host_initiator_group_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **host_initiator_group_id** | **str**| Identifier of initiator group. A 42 digit hexadecimal number. |

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

# **device_type2_update_host_initiator_group_by_id**
> TaskResponse device_type2_update_host_initiator_group_by_id(system_id, host_initiator_group_id, nimble_edit_initiator_group_input)

Update initiator-groups identified by {hostInitiatorGroupId}

Update initiator-groups identified by {hostInitiatorGroupId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiator_groups_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_edit_initiator_group_input import NimbleEditInitiatorGroupInput
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
    api_instance = host_initiator_groups_api.HostInitiatorGroupsApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    host_initiator_group_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | Identifier of initiator group. A 42 digit hexadecimal number.
    nimble_edit_initiator_group_input = NimbleEditInitiatorGroupInput(
        app_uuid="rfc4122.943f7dc1-5853-497c-b530-f689ccf1bf18",
        description="99.9999% availability",
        fc_initiators=[
            NimbleFCInitiator(
                alias="vegaalias",
                id="0b1c9973433673c3db000000000000000000000001",
                wwpn="0b1c9973433673c3db000000000000000000000001",
            ),
        ],
        fc_tdz_ports=[
            NimbleFCTdzPorts(
                array_name="myobject-5",
                fc_name="myobject-5",
            ),
        ],
        host_type="myobject-5",
        iscsi_initiators=[
            NimbleISCSIInitiator(
                id="021c9973433673c3db000000000000000000000001",
                ip_address="xx.xxx.xx.xx",
                iqn="vegaiqn",
                label="vega",
            ),
        ],
        metadata=[
            NimbleMetadata(
                key="vega-key",
                value="vega-value",
            ),
        ],
        name="myobject-5",
        target_subnets=[
            NimbleTargetSubnets(
                id="021c9973433673c3db000000000000000000000003",
                label="myobject-5",
            ),
        ],
    ) # NimbleEditInitiatorGroupInput | 

    # example passing only required values which don't have defaults set
    try:
        # Update initiator-groups identified by {hostInitiatorGroupId}
        api_response = api_instance.device_type2_update_host_initiator_group_by_id(system_id, host_initiator_group_id, nimble_edit_initiator_group_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->device_type2_update_host_initiator_group_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **host_initiator_group_id** | **str**| Identifier of initiator group. A 42 digit hexadecimal number. |
 **nimble_edit_initiator_group_input** | [**NimbleEditInitiatorGroupInput**](NimbleEditInitiatorGroupInput.md)|  |

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

# **host_group_create**
> HostGroupObject host_group_create(create_host_group_input)

Create a host group

Create a host group

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiator_groups_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.host_group_object import HostGroupObject
from greenlake_data_services.model.create_host_group_input import CreateHostGroupInput
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
    api_instance = host_initiator_groups_api.HostInitiatorGroupsApi(api_client)
    create_host_group_input = CreateHostGroupInput(
        comment="host-group-comment",
        host_ids=[
            "host_ids_example",
        ],
        hosts_to_create=[
            CreateHostInput(
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
            ),
        ],
        name="host-group1",
        user_created=True,
    ) # CreateHostGroupInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create a host group
        api_response = api_instance.host_group_create(create_host_group_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->host_group_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_host_group_input** | [**CreateHostGroupInput**](CreateHostGroupInput.md)|  |

### Return type

[**HostGroupObject**](HostGroupObject.md)

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

# **host_group_delete**
> TaskResponse host_group_delete(host_group_id)

Delete a host group by {hostGroupId}

Delete a host group by {hostGroupId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiator_groups_api
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
    api_instance = host_initiator_groups_api.HostInitiatorGroupsApi(api_client)
    host_group_id = "e789e756496246859fde6c132b2091d3" # str | Id of the host Group.
    force = True # bool | Forceful delete option (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete a host group by {hostGroupId}
        api_response = api_instance.host_group_delete(host_group_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->host_group_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a host group by {hostGroupId}
        api_response = api_instance.host_group_delete(host_group_id, force=force)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->host_group_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_group_id** | **str**| Id of the host Group. |
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

# **host_group_get_by_id**
> HostGroupDetails host_group_get_by_id(host_group_id)

Get the host group details by {hostGroupId}

Get the host group details by {hostGroupId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiator_groups_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.host_group_details import HostGroupDetails
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
    api_instance = host_initiator_groups_api.HostInitiatorGroupsApi(api_client)
    host_group_id = "e789e756496246859fde6c132b2091d3" # str | Id of the host Group.

    # example passing only required values which don't have defaults set
    try:
        # Get the host group details by {hostGroupId}
        api_response = api_instance.host_group_get_by_id(host_group_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->host_group_get_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_group_id** | **str**| Id of the host Group. |

### Return type

[**HostGroupDetails**](HostGroupDetails.md)

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

# **host_group_list**
> HostGroupsList host_group_list()

Get the list of host groups

Get the list of host groups

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiator_groups_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.host_groups_list import HostGroupsList
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
    api_instance = host_initiator_groups_api.HostInitiatorGroupsApi(api_client)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | oData query to filter hostservice by Key. (optional)
    sort = "name desc" # str | oData query to sort hostservice by Key. (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of host groups
        api_response = api_instance.host_group_list(filter=filter, sort=sort, limit=limit, offset=offset)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->host_group_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| oData query to filter hostservice by Key. | [optional]
 **sort** | **str**| oData query to sort hostservice by Key. | [optional]
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]

### Return type

[**HostGroupsList**](HostGroupsList.md)

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

# **host_group_update_by_id**
> TaskResponse host_group_update_by_id(host_group_id, update_host_group_input)

Update host group by {hostGroupId}

Update host group details by {hostGroupId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import host_initiator_groups_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.update_host_group_input import UpdateHostGroupInput
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
    api_instance = host_initiator_groups_api.HostInitiatorGroupsApi(api_client)
    host_group_id = "e789e756496246859fde6c132b2091d3" # str | Id of the host Group.
    update_host_group_input = UpdateHostGroupInput(
        host_proximity_values=[
            HostProximityValue(
                group_name="RCGName",
                group_uid="rcg1",
                host_id="12345",
                host_name="host1",
                proximity_system_name="primary",
                system_name="system1",
                system_uid="SGH014XGSP",
                target_name="system2",
                target_system_id="7CE751P312",
            ),
        ],
        hosts_to_create=[
            CreateHostInput(
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
            ),
        ],
        name="host-group1",
        removed_hosts=[
            "removed_hosts_example",
        ],
        updated_hosts=[
            "updated_hosts_example",
        ],
    ) # UpdateHostGroupInput | 

    # example passing only required values which don't have defaults set
    try:
        # Update host group by {hostGroupId}
        api_response = api_instance.host_group_update_by_id(host_group_id, update_host_group_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling HostInitiatorGroupsApi->host_group_update_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_group_id** | **str**| Id of the host Group. |
 **update_host_group_input** | [**UpdateHostGroupInput**](UpdateHostGroupInput.md)|  |

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

