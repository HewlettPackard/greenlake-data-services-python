# greenlake-data-services.HostInitiatorGroupsApi

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
> NimbleInitiatorGroupList device_type2_get_all_host_initiator_groups(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all nimble host initiator groups details by Nimble / Alletra 6K

Get all nimble host initiator groups details by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.HostInitiatorGroupsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter initiator groups by Key. (optional)
sort = 'sort_example' # str | oData query to sort initiator groups resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all nimble host initiator groups details by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_host_initiator_groups(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_host_initiator_group_by_id**
> NimbleInitiatorGroupDetails device_type2_get_host_initiator_group_by_id(system_id, host_initiator_group_id, select=select)

Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}

Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}

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
api_instance = greenlake-data-services.HostInitiatorGroupsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
host_initiator_group_id = 'host_initiator_group_id_example' # str | Identifier of initiator group. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorGroupId}
    api_response = api_instance.device_type2_get_host_initiator_group_by_id(system_id, host_initiator_group_id, select=select)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_host_initiator_group_create**
> TaskResponse device_type2_host_initiator_group_create(system_id, nimble_create_initiator_group_input)

Create Nimble / Alletra 6K initiator group in system identified by {systemId}

Create Nimble / Alletra 6K initiator group in system identified by {systemId}

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
api_instance = greenlake-data-services.HostInitiatorGroupsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_initiator_group_input = greenlake-data-services.NimbleCreateInitiatorGroupInput() # NimbleCreateInitiatorGroupInput | 

try:
    # Create Nimble / Alletra 6K initiator group in system identified by {systemId}
    api_response = api_instance.device_type2_host_initiator_group_create(system_id, nimble_create_initiator_group_input)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_host_initiator_group_by_id**
> TaskResponse device_type2_remove_host_initiator_group_by_id(system_id, host_initiator_group_id)

Remove initiator-groups identified by {hostInitiatorGroupId} from Nimble / Alletra 6K

Remove initiator-groups identified by {hostInitiatorGroupId} from Nimble / Alletra 6K

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
api_instance = greenlake-data-services.HostInitiatorGroupsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
host_initiator_group_id = 'host_initiator_group_id_example' # str | Identifier of initiator group. A 42 digit hexadecimal number.

try:
    # Remove initiator-groups identified by {hostInitiatorGroupId} from Nimble / Alletra 6K
    api_response = api_instance.device_type2_remove_host_initiator_group_by_id(system_id, host_initiator_group_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_update_host_initiator_group_by_id**
> TaskResponse device_type2_update_host_initiator_group_by_id(system_id, host_initiator_group_id, nimble_edit_initiator_group_input)

Update initiator-groups identified by {hostInitiatorGroupId}

Update initiator-groups identified by {hostInitiatorGroupId}

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
api_instance = greenlake-data-services.HostInitiatorGroupsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
host_initiator_group_id = 'host_initiator_group_id_example' # str | Identifier of initiator group. A 42 digit hexadecimal number.
nimble_edit_initiator_group_input = greenlake-data-services.NimbleEditInitiatorGroupInput() # NimbleEditInitiatorGroupInput | 

try:
    # Update initiator-groups identified by {hostInitiatorGroupId}
    api_response = api_instance.device_type2_update_host_initiator_group_by_id(system_id, host_initiator_group_id, nimble_edit_initiator_group_input)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_group_create**
> HostGroupObject host_group_create(create_host_group_input)

Create a host group

Create a host group

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
api_instance = greenlake-data-services.HostInitiatorGroupsApi(greenlake-data-services.ApiClient(configuration))
create_host_group_input = greenlake-data-services.CreateHostGroupInput() # CreateHostGroupInput | 

try:
    # Create a host group
    api_response = api_instance.host_group_create(create_host_group_input)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_group_delete**
> TaskResponse host_group_delete(host_group_id, force=force)

Delete a host group by {hostGroupId}

Delete a host group by {hostGroupId}

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
api_instance = greenlake-data-services.HostInitiatorGroupsApi(greenlake-data-services.ApiClient(configuration))
host_group_id = 'host_group_id_example' # str | Id of the host Group.
force = True # bool | Forceful delete option (optional)

try:
    # Delete a host group by {hostGroupId}
    api_response = api_instance.host_group_delete(host_group_id, force=force)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_group_get_by_id**
> HostGroupDetails host_group_get_by_id(host_group_id)

Get the host group details by {hostGroupId}

Get the host group details by {hostGroupId}

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
api_instance = greenlake-data-services.HostInitiatorGroupsApi(greenlake-data-services.ApiClient(configuration))
host_group_id = 'host_group_id_example' # str | Id of the host Group.

try:
    # Get the host group details by {hostGroupId}
    api_response = api_instance.host_group_get_by_id(host_group_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_group_list**
> HostGroupsList host_group_list(filter=filter, sort=sort, limit=limit, offset=offset)

Get the list of host groups

Get the list of host groups

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
api_instance = greenlake-data-services.HostInitiatorGroupsApi(greenlake-data-services.ApiClient(configuration))
filter = 'filter_example' # str | oData query to filter hostservice by Key. (optional)
sort = 'sort_example' # str | oData query to sort hostservice by Key. (optional)
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)

try:
    # Get the list of host groups
    api_response = api_instance.host_group_list(filter=filter, sort=sort, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_group_update_by_id**
> TaskResponse host_group_update_by_id(host_group_id, update_host_group_input)

Update host group by {hostGroupId}

Update host group details by {hostGroupId}

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
api_instance = greenlake-data-services.HostInitiatorGroupsApi(greenlake-data-services.ApiClient(configuration))
host_group_id = 'host_group_id_example' # str | Id of the host Group.
update_host_group_input = greenlake-data-services.UpdateHostGroupInput() # UpdateHostGroupInput | 

try:
    # Update host group by {hostGroupId}
    api_response = api_instance.host_group_update_by_id(host_group_id, update_host_group_input)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

