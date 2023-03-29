# greenlake_data_services.FoldersApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_folder_create**](FoldersApi.md#device_type2_folder_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/folders | Create Nimble / Alletra 6K folder in system identified by {systemId}
[**device_type2_folder_edit**](FoldersApi.md#device_type2_folder_edit) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/folders/{folderId} | Edit details of Nimble / Alletra 6K folder identified by {folderId}
[**device_type2_get_folder_by_id**](FoldersApi.md#device_type2_get_folder_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/folders/{folderId} | Get details of Nimble / Alletra 6K Folders identified by {folderId}
[**device_type2_remove_folder_by_id**](FoldersApi.md#device_type2_remove_folder_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/folders/{folderId} | Remove Nimble / Alletra 6K folder identified by {folderId}


# **device_type2_folder_create**
> TaskResponse device_type2_folder_create(system_id, nimble_create_folder_input)

Create Nimble / Alletra 6K folder in system identified by {systemId}

Create Nimble / Alletra 6K folder in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import folders_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from greenlake_data_services.model.nimble_create_folder_input import NimbleCreateFolderInput
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
    api_instance = folders_api.FoldersApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_create_folder_input = NimbleCreateFolderInput(
        access_protocol="iscsi",
        agent_type="openstack",
        appserver_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        description="99.9999% availability",
        inherited_vol_perfpol_id="030a259996ae869835000000000000000000000001",
        limit_iops=-1,
        limit_mbps=-1,
        limit_size_bytes=-1,
        name="myobject-5",
        overdraft_limit_pct=0,
        pool_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        provisioned_limit_size_bytes=-1,
    ) # NimbleCreateFolderInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create Nimble / Alletra 6K folder in system identified by {systemId}
        api_response = api_instance.device_type2_folder_create(system_id, nimble_create_folder_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling FoldersApi->device_type2_folder_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **nimble_create_folder_input** | [**NimbleCreateFolderInput**](NimbleCreateFolderInput.md)|  |

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

# **device_type2_folder_edit**
> TaskResponse device_type2_folder_edit(system_id, folder_id, nimble_edit_folder_input)

Edit details of Nimble / Alletra 6K folder identified by {folderId}

Edit details of Nimble / Alletra 6K folder identified by {folderId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import folders_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_edit_folder_input import NimbleEditFolderInput
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
    api_instance = folders_api.FoldersApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    folder_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the folder. A 42 digit hexadecimal number.
    nimble_edit_folder_input = NimbleEditFolderInput(
        appserver_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        description="99.9999% availability",
        inherited_vol_perfpol_id="030a259996ae869835000000000000000000000001",
        limit_iops=-1,
        limit_mbps=-1,
        limit_size_bytes=-1,
        name="myobject-5",
        overdraft_limit_pct=0,
        provisioned_limit_size_bytes=-1,
    ) # NimbleEditFolderInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit details of Nimble / Alletra 6K folder identified by {folderId}
        api_response = api_instance.device_type2_folder_edit(system_id, folder_id, nimble_edit_folder_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling FoldersApi->device_type2_folder_edit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **folder_id** | **str**| ID of the folder. A 42 digit hexadecimal number. |
 **nimble_edit_folder_input** | [**NimbleEditFolderInput**](NimbleEditFolderInput.md)|  |

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

# **device_type2_get_folder_by_id**
> NimbleFolderDetailsWithRequestUri device_type2_get_folder_by_id(system_id, folder_id)

Get details of Nimble / Alletra 6K Folders identified by {folderId}

Get details of Nimble / Alletra 6K Folders identified by {folderId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import folders_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_folder_details_with_request_uri import NimbleFolderDetailsWithRequestUri
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
    api_instance = folders_api.FoldersApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    folder_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the folder. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K Folders identified by {folderId}
        api_response = api_instance.device_type2_get_folder_by_id(system_id, folder_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling FoldersApi->device_type2_get_folder_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K Folders identified by {folderId}
        api_response = api_instance.device_type2_get_folder_by_id(system_id, folder_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling FoldersApi->device_type2_get_folder_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **folder_id** | **str**| ID of the folder. A 42 digit hexadecimal number. |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NimbleFolderDetailsWithRequestUri**](NimbleFolderDetailsWithRequestUri.md)

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

# **device_type2_remove_folder_by_id**
> TaskResponse device_type2_remove_folder_by_id(system_id, folder_id)

Remove Nimble / Alletra 6K folder identified by {folderId}

Remove Nimble / Alletra 6K folder identified by {folderId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import folders_api
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
    api_instance = folders_api.FoldersApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    folder_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the folder. A 42 digit hexadecimal number.

    # example passing only required values which don't have defaults set
    try:
        # Remove Nimble / Alletra 6K folder identified by {folderId}
        api_response = api_instance.device_type2_remove_folder_by_id(system_id, folder_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling FoldersApi->device_type2_remove_folder_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **folder_id** | **str**| ID of the folder. A 42 digit hexadecimal number. |

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

