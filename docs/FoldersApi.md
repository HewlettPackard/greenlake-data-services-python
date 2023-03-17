# greenlake-data-services.FoldersApi

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
api_instance = greenlake-data-services.FoldersApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_folder_input = greenlake-data-services.NimbleCreateFolderInput() # NimbleCreateFolderInput | 

try:
    # Create Nimble / Alletra 6K folder in system identified by {systemId}
    api_response = api_instance.device_type2_folder_create(system_id, nimble_create_folder_input)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_folder_edit**
> TaskResponse device_type2_folder_edit(system_id, folder_id, nimble_edit_folder_input)

Edit details of Nimble / Alletra 6K folder identified by {folderId}

Edit details of Nimble / Alletra 6K folder identified by {folderId}

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
api_instance = greenlake-data-services.FoldersApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
folder_id = 'folder_id_example' # str | ID of the folder. A 42 digit hexadecimal number.
nimble_edit_folder_input = greenlake-data-services.NimbleEditFolderInput() # NimbleEditFolderInput | 

try:
    # Edit details of Nimble / Alletra 6K folder identified by {folderId}
    api_response = api_instance.device_type2_folder_edit(system_id, folder_id, nimble_edit_folder_input)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_folder_by_id**
> NimbleFolderDetailsWithRequestUri device_type2_get_folder_by_id(system_id, folder_id, select=select)

Get details of Nimble / Alletra 6K Folders identified by {folderId}

Get details of Nimble / Alletra 6K Folders identified by {folderId}

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
api_instance = greenlake-data-services.FoldersApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
folder_id = 'folder_id_example' # str | ID of the folder. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K Folders identified by {folderId}
    api_response = api_instance.device_type2_get_folder_by_id(system_id, folder_id, select=select)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_folder_by_id**
> TaskResponse device_type2_remove_folder_by_id(system_id, folder_id)

Remove Nimble / Alletra 6K folder identified by {folderId}

Remove Nimble / Alletra 6K folder identified by {folderId}

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
api_instance = greenlake-data-services.FoldersApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
folder_id = 'folder_id_example' # str | ID of the folder. A 42 digit hexadecimal number.

try:
    # Remove Nimble / Alletra 6K folder identified by {folderId}
    api_response = api_instance.device_type2_remove_folder_by_id(system_id, folder_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

