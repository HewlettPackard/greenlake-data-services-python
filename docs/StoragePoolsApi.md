# greenlake-data-services.StoragePoolsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_storage_pool_get_by_id**](StoragePoolsApi.md#device_type1_storage_pool_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/storage-pools/{id} | Get details of Primera / Alletra 9K storage-pool identified by {id}
[**device_type1_storage_pool_list**](StoragePoolsApi.md#device_type1_storage_pool_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/storage-pools | Get all storage-pools details by Primera / Alletra 9K
[**device_type1_storage_pool_volume_get_by_id**](StoragePoolsApi.md#device_type1_storage_pool_volume_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/storage-pools/{id}/volumes | Get all volumes for storage-pool identified by {uuid} of Primera / Alletra 9K
[**device_type2_create_pool**](StoragePoolsApi.md#device_type2_create_pool) | **POST** /api/v1/storage-systems/device-type2/{systemId}/storage-pools | Create storage pool from Nimble / Alletra 6K  system identified by {systemId}
[**device_type2_edit_pool_detail_by_id**](StoragePoolsApi.md#device_type2_edit_pool_detail_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId} | Edit details of Nimble / Alletra 6K pool identified by {storagePoolId}
[**device_type2_get_all_pool_details**](StoragePoolsApi.md#device_type2_get_all_pool_details) | **GET** /api/v1/storage-systems/device-type2/{systemId}/storage-pools | Get all pools details by Nimble / Alletra 6K
[**device_type2_get_pool_capacity_history**](StoragePoolsApi.md#device_type2_get_pool_capacity_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId}/capacity-history | Get storage pool capacity trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}
[**device_type2_get_pool_detail_by_id**](StoragePoolsApi.md#device_type2_get_pool_detail_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId} | Get details of Nimble / Alletra 6K pool identified by {storagePoolId}
[**device_type2_get_pool_performance_history**](StoragePoolsApi.md#device_type2_get_pool_performance_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId}/performance-history | Get performance trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}
[**device_type2_get_pool_performance_statistics**](StoragePoolsApi.md#device_type2_get_pool_performance_statistics) | **GET** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId}/performance-statistics | Get performance statistics of Nimble / Alletra 6K storage pool identified by {storagePoolId}
[**device_type2_merge_pool_by_id**](StoragePoolsApi.md#device_type2_merge_pool_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId}/actions/merge | Merge pool identified by {storagePoolId} from Nimble / Alletra 6K
[**device_type2_remove_pool_by_id**](StoragePoolsApi.md#device_type2_remove_pool_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/storage-pools/{storagePoolId} | Delete pool identified by {storagePoolId} from Nimble / Alletra 6K
[**storage_pool_volumes_list**](StoragePoolsApi.md#storage_pool_volumes_list) | **GET** /api/v1/storage-systems/{systemId}/storage-pools/{id}/volumes | Get all volumes for storage-pool identified by {id}
[**storage_pools_get_by_id**](StoragePoolsApi.md#storage_pools_get_by_id) | **GET** /api/v1/storage-systems/{systemId}/storage-pools/{id} | Get details of storage pools identified by {id}
[**storage_pools_list**](StoragePoolsApi.md#storage_pools_list) | **GET** /api/v1/storage-systems/{systemId}/storage-pools | Get all storage pools for a device {systemId}


# **device_type1_storage_pool_get_by_id**
> PrimeraPoolDetails device_type1_storage_pool_get_by_id(system_id, id, select=select)

Get details of Primera / Alletra 9K storage-pool identified by {id}

Get details of Primera / Alletra 9K storage-pool identified by {id}

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | Identifier of pool. A 32 digit number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Primera / Alletra 9K storage-pool identified by {id}
    api_response = api_instance.device_type1_storage_pool_get_by_id(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->device_type1_storage_pool_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| Identifier of pool. A 32 digit number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraPoolDetails**](PrimeraPoolDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_storage_pool_list**
> PrimeraPoolsSummaryList device_type1_storage_pool_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all storage-pools details by Primera / Alletra 9K

Get all storage-pools details by Primera / Alletra 9K

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter pools by Key. (optional)
sort = 'sort_example' # str | oData query to sort pools by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all storage-pools details by Primera / Alletra 9K
    api_response = api_instance.device_type1_storage_pool_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->device_type1_storage_pool_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter pools by Key. | [optional] 
 **sort** | **str**| oData query to sort pools by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraPoolsSummaryList**](PrimeraPoolsSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_storage_pool_volume_get_by_id**
> PrimeraVolumesList device_type1_storage_pool_volume_get_by_id(system_id, id, select=select)

Get all volumes for storage-pool identified by {uuid} of Primera / Alletra 9K

Get all volumes for storage-pool identified by {uuid} of Primera / Alletra 9K

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | Identifier of pool. A 32 digit number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all volumes for storage-pool identified by {uuid} of Primera / Alletra 9K
    api_response = api_instance.device_type1_storage_pool_volume_get_by_id(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->device_type1_storage_pool_volume_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| Identifier of pool. A 32 digit number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraVolumesList**](PrimeraVolumesList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_create_pool**
> TaskResponse device_type2_create_pool(system_id, nimble_create_pool_input)

Create storage pool from Nimble / Alletra 6K  system identified by {systemId}

Create storage pool from Nimble / Alletra 6K  system identified by {systemId}

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_pool_input = greenlake-data-services.NimbleCreatePoolInput() # NimbleCreatePoolInput | 

try:
    # Create storage pool from Nimble / Alletra 6K  system identified by {systemId}
    api_response = api_instance.device_type2_create_pool(system_id, nimble_create_pool_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->device_type2_create_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_pool_input** | [**NimbleCreatePoolInput**](NimbleCreatePoolInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_pool_detail_by_id**
> TaskResponse device_type2_edit_pool_detail_by_id(system_id, storage_pool_id, nimble_edit_pool_input)

Edit details of Nimble / Alletra 6K pool identified by {storagePoolId}

Edit details of Nimble / Alletra 6K pool identified by {storagePoolId}

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
storage_pool_id = 'storage_pool_id_example' # str | Identifier of pool. A 42 digit hexadecimal number.
nimble_edit_pool_input = greenlake-data-services.NimbleEditPoolInput() # NimbleEditPoolInput | 

try:
    # Edit details of Nimble / Alletra 6K pool identified by {storagePoolId}
    api_response = api_instance.device_type2_edit_pool_detail_by_id(system_id, storage_pool_id, nimble_edit_pool_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->device_type2_edit_pool_detail_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of pool. A 42 digit hexadecimal number. | 
 **nimble_edit_pool_input** | [**NimbleEditPoolInput**](NimbleEditPoolInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_pool_details**
> NimblePoolsList device_type2_get_all_pool_details(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all pools details by Nimble / Alletra 6K

Get all pools details by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter pools by Key. (optional)
sort = 'sort_example' # str | oData query to sort pools resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all pools details by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_pool_details(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->device_type2_get_all_pool_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter pools by Key. | [optional] 
 **sort** | **str**| oData query to sort pools resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimblePoolsList**](NimblePoolsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_pool_capacity_history**
> PoolCapacityHistory device_type2_get_pool_capacity_history(system_id, storage_pool_id, select=select, range=range, time_interval_min=time_interval_min)

Get storage pool capacity trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}

Get storage pool capacity trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
storage_pool_id = 'storage_pool_id_example' # str | Identifier of storage pool. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
time_interval_min = 56 # int | It defines granularity in minutes. (optional)

try:
    # Get storage pool capacity trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}
    api_response = api_instance.device_type2_get_pool_capacity_history(system_id, storage_pool_id, select=select, range=range, time_interval_min=time_interval_min)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->device_type2_get_pool_capacity_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of storage pool. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**PoolCapacityHistory**](PoolCapacityHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_pool_detail_by_id**
> NimblePoolDetailsWithRequestUri device_type2_get_pool_detail_by_id(system_id, storage_pool_id, select=select)

Get details of Nimble / Alletra 6K pool identified by {storagePoolId}

Get details of Nimble / Alletra 6K pool identified by {storagePoolId}

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
storage_pool_id = 'storage_pool_id_example' # str | Identifier of pool. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K pool identified by {storagePoolId}
    api_response = api_instance.device_type2_get_pool_detail_by_id(system_id, storage_pool_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->device_type2_get_pool_detail_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of pool. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimblePoolDetailsWithRequestUri**](NimblePoolDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_pool_performance_history**
> StoragePoolPerformanceHistory device_type2_get_pool_performance_history(system_id, storage_pool_id, select=select, range=range, time_interval_min=time_interval_min)

Get performance trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}

Get performance trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
storage_pool_id = 'storage_pool_id_example' # str | Identifier of storage pool. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
time_interval_min = 56 # int | It defines granularity in minutes. (optional)

try:
    # Get performance trend data of Nimble / Alletra 6K storage pool identified by {storagePoolId}
    api_response = api_instance.device_type2_get_pool_performance_history(system_id, storage_pool_id, select=select, range=range, time_interval_min=time_interval_min)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->device_type2_get_pool_performance_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of storage pool. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**StoragePoolPerformanceHistory**](StoragePoolPerformanceHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_pool_performance_statistics**
> StoragePoolPerformance device_type2_get_pool_performance_statistics(system_id, storage_pool_id, select=select)

Get performance statistics of Nimble / Alletra 6K storage pool identified by {storagePoolId}

Get performance statistics of Nimble / Alletra 6K storage pool identified by {storagePoolId}

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
storage_pool_id = 'storage_pool_id_example' # str | Identifier of storage pool. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get performance statistics of Nimble / Alletra 6K storage pool identified by {storagePoolId}
    api_response = api_instance.device_type2_get_pool_performance_statistics(system_id, storage_pool_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->device_type2_get_pool_performance_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of storage pool. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**StoragePoolPerformance**](StoragePoolPerformance.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_merge_pool_by_id**
> TaskResponse device_type2_merge_pool_by_id(system_id, storage_pool_id, nimble_merge_pool_input)

Merge pool identified by {storagePoolId} from Nimble / Alletra 6K

Merge pool identified by {storagePoolId} from Nimble / Alletra 6K

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
storage_pool_id = 'storage_pool_id_example' # str | Identifier of pool. A 42 digit hexadecimal number.
nimble_merge_pool_input = greenlake-data-services.NimbleMergePoolInput() # NimbleMergePoolInput | 

try:
    # Merge pool identified by {storagePoolId} from Nimble / Alletra 6K
    api_response = api_instance.device_type2_merge_pool_by_id(system_id, storage_pool_id, nimble_merge_pool_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->device_type2_merge_pool_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of pool. A 42 digit hexadecimal number. | 
 **nimble_merge_pool_input** | [**NimbleMergePoolInput**](NimbleMergePoolInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_pool_by_id**
> TaskResponse device_type2_remove_pool_by_id(system_id, storage_pool_id)

Delete pool identified by {storagePoolId} from Nimble / Alletra 6K

Delete pool identified by {storagePoolId} from Nimble / Alletra 6K

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
storage_pool_id = 'storage_pool_id_example' # str | Identifier of pool. A 42 digit hexadecimal number.

try:
    # Delete pool identified by {storagePoolId} from Nimble / Alletra 6K
    api_response = api_instance.device_type2_remove_pool_by_id(system_id, storage_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->device_type2_remove_pool_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **storage_pool_id** | **str**| Identifier of pool. A 42 digit hexadecimal number. | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pool_volumes_list**
> FleetVolumesList storage_pool_volumes_list(system_id, id, select=select)

Get all volumes for storage-pool identified by {id}

Get all volumes for storage-pool identified by {id}

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | Identifier of pool. A 32 digit number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all volumes for storage-pool identified by {id}
    api_response = api_instance.storage_pool_volumes_list(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->storage_pool_volumes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| Identifier of pool. A 32 digit number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetVolumesList**](FleetVolumesList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pools_get_by_id**
> FleetPoolDetails storage_pools_get_by_id(system_id, id, select=select)

Get details of storage pools identified by {id}

Get details of storage pools identified by {id}

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | Identifier of pool. A 32 digit number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of storage pools identified by {id}
    api_response = api_instance.storage_pools_get_by_id(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->storage_pools_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| Identifier of pool. A 32 digit number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetPoolDetails**](FleetPoolDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **storage_pools_list**
> StoragePoolsFleetSummaryList storage_pools_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all storage pools for a device {systemId}

Get all storage pools for a device {systemId}

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
api_instance = greenlake-data-services.StoragePoolsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter pools by Key. (optional)
sort = 'sort_example' # str | oData query to sort pools by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all storage pools for a device {systemId}
    api_response = api_instance.storage_pools_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StoragePoolsApi->storage_pools_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter pools by Key. | [optional] 
 **sort** | **str**| oData query to sort pools by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**StoragePoolsFleetSummaryList**](StoragePoolsFleetSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

