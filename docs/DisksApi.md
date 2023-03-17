# greenlake-data-services.DisksApi

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
api_instance = greenlake-data-services.DisksApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
disk_id = 'disk_id_example' # str | Identifier of disk. A 42 digit hexadecimal number.
nimble_edit_disk_input = greenlake-data-services.NimbleEditDiskInput() # NimbleEditDiskInput | 

try:
    # Edit details of Nimble / Alletra 6K disk identified by {diskId}
    api_response = api_instance.device_type2_disk_edit(system_id, disk_id, nimble_edit_disk_input)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_disks**
> NimbleDisksList device_type2_get_all_disks(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all disks details by Nimble / Alletra 6K

Get all disks details by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.DisksApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter disks by Key. (optional)
sort = 'sort_example' # str | oData query to sort disks resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all disks details by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_disks(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_disk_by_id**
> NimbleDiskDetails device_type2_get_disk_by_id(system_id, disk_id, select=select)

Get details of Nimble / Alletra 6K disk identified by {diskId}

Get details of Nimble / Alletra 6K disk identified by {diskId}

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
api_instance = greenlake-data-services.DisksApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
disk_id = 'disk_id_example' # str | Identifier of disk. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K disk identified by {diskId}
    api_response = api_instance.device_type2_get_disk_by_id(system_id, disk_id, select=select)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

