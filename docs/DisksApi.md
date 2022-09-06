# greenlake_data_services.DisksApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_disk_edit**](DisksApi.md#device_type2_disk_edit) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/disks/{diskId} | Edit details of Nimble / Alletra 6K disk identified by {diskId}
[**device_type2_get_all_disks**](DisksApi.md#device_type2_get_all_disks) | **GET** /api/v1/storage-systems/device-type2/{systemId}/disks | Get all disks details by Nimble / Alletra 6K
[**device_type2_get_disk_by_id**](DisksApi.md#device_type2_get_disk_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/disks/{diskId} | Get details of Nimble / Alletra 6K disk identified by {diskId}


# **device_type2_disk_edit**
> TaskResponse device_type2_disk_edit(system_id, disk_id, nimble_edit_disk_input)

Edit details of Nimble / Alletra 6K disk identified by {diskId}

Edit details of Nimble / Alletra 6K disk identified by {diskId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import disks_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.nimble_edit_disk_input import NimbleEditDiskInput
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
    api_instance = disks_api.DisksApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    disk_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | Identifier of disk. A 42 digit hexadecimal number.
    nimble_edit_disk_input = NimbleEditDiskInput(
        disk_op="add",
        force=True,
    ) # NimbleEditDiskInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit details of Nimble / Alletra 6K disk identified by {diskId}
        api_response = api_instance.device_type2_disk_edit(system_id, disk_id, nimble_edit_disk_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling DisksApi->device_type2_disk_edit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **disk_id** | **str**| Identifier of disk. A 42 digit hexadecimal number. |
 **nimble_edit_disk_input** | [**NimbleEditDiskInput**](NimbleEditDiskInput.md)|  |

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

# **device_type2_get_all_disks**
> NimbleDisksList device_type2_get_all_disks(system_id)

Get all disks details by Nimble / Alletra 6K

Get all disks details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import disks_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_disks_list import NimbleDisksList
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
    api_instance = disks_api.DisksApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter disks by Key. (optional)
    sort = "name desc" # str | oData query to sort disks resource by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all disks details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_disks(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling DisksApi->device_type2_get_all_disks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all disks details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_disks(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling DisksApi->device_type2_get_all_disks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **limit** | **int**| Number of items to return at a time | [optional]
 **offset** | **int**| The offset of the first item in the collection to return | [optional]
 **filter** | **str**| Lucene query to filter disks by Key. | [optional]
 **sort** | **str**| oData query to sort disks resource by Key. | [optional]
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NimbleDisksList**](NimbleDisksList.md)

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

# **device_type2_get_disk_by_id**
> NimbleDiskDetails device_type2_get_disk_by_id(system_id, disk_id)

Get details of Nimble / Alletra 6K disk identified by {diskId}

Get details of Nimble / Alletra 6K disk identified by {diskId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import disks_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_disk_details import NimbleDiskDetails
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
    api_instance = disks_api.DisksApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    disk_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | Identifier of disk. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K disk identified by {diskId}
        api_response = api_instance.device_type2_get_disk_by_id(system_id, disk_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling DisksApi->device_type2_get_disk_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K disk identified by {diskId}
        api_response = api_instance.device_type2_get_disk_by_id(system_id, disk_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling DisksApi->device_type2_get_disk_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system |
 **disk_id** | **str**| Identifier of disk. A 42 digit hexadecimal number. |
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional]

### Return type

[**NimbleDiskDetails**](NimbleDiskDetails.md)

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

