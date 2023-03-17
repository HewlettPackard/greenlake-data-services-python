# greenlake-data-services.HostInitiatorsApi

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
> NimbleInitiatorsList device_type2_get_all_initiators(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all nimble initiators details by Nimble / Alletra 6K

Get all nimble initiators details by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter initiators by Key. (optional)
sort = 'sort_example' # str | oData query to sort initiators resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all nimble initiators details by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_initiators(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_initiators_by_id**
> NimbleInitiatorDetails device_type2_get_initiators_by_id(system_id, host_initiator_id, select=select)

Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorId}

Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorId}

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
host_initiator_id = 'host_initiator_id_example' # str | ID of the nimble initiator. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K Nimble Initiators identified by {hostInitiatorId}
    api_response = api_instance.device_type2_get_initiators_by_id(system_id, host_initiator_id, select=select)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_initiators_create**
> TaskResponse device_type2_initiators_create(system_id, nimble_create_initiator_input)

Create Nimble / Alletra 6K nimble initiator in system identified by {systemId}

Get all nimble initiators details by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_initiator_input = greenlake-data-services.NimbleCreateInitiatorInput() # NimbleCreateInitiatorInput | 

try:
    # Create Nimble / Alletra 6K nimble initiator in system identified by {systemId}
    api_response = api_instance.device_type2_initiators_create(system_id, nimble_create_initiator_input)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_initiators_by_id**
> TaskResponse device_type2_remove_initiators_by_id(system_id, host_initiator_id)

Remove Nimble Initiator identified by {hostInitiatorId} from Nimble / Alletra 6K

Remove Nimble Initiator identified by {hostInitiatorId} from Nimble / Alletra 6K

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
host_initiator_id = 'host_initiator_id_example' # str | Identifier of Host Initiator. A 42 digit hexadecimal number.

try:
    # Remove Nimble Initiator identified by {hostInitiatorId} from Nimble / Alletra 6K
    api_response = api_instance.device_type2_remove_initiators_by_id(system_id, host_initiator_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_create**
> HostObject host_create(create_host_input)

Create a host

Create a host

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
create_host_input = greenlake-data-services.CreateHostInput() # CreateHostInput | 

try:
    # Create a host
    api_response = api_instance.host_create(create_host_input)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_delete**
> TaskResponse host_delete(host_id, force=force)

Delete a host by {hostId}

Delete a host by {hostId}

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
host_id = 'host_id_example' # str | Id of the SC Host.
force = True # bool | Forceful delete option (optional)

try:
    # Delete a host by {hostId}
    api_response = api_instance.host_delete(host_id, force=force)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_get_by_id**
> HostDetails host_get_by_id(host_id)

Get the host details by {hostId}

Get the host details by {hostId}

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
host_id = 'host_id_example' # str | Id of the SC Host.

try:
    # Get the host details by {hostId}
    api_response = api_instance.host_get_by_id(host_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_initiator_create**
> Initiator host_initiator_create(initiator_input)

Create initiator

Create initiator

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
initiator_input = greenlake-data-services.InitiatorInput() # InitiatorInput | 

try:
    # Create initiator
    api_response = api_instance.host_initiator_create(initiator_input)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_initiator_delete**
> DeleteInitiator host_initiator_delete(initiator_id)

Delete initiator by {initiatorId}

Delete initiator by {initiatorId}

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
initiator_id = 'initiator_id_example' # str | UID of SC Initiator.

try:
    # Delete initiator by {initiatorId}
    api_response = api_instance.host_initiator_delete(initiator_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_initiator_get_by_id**
> InitiatorDetails host_initiator_get_by_id(initiator_id)

Get the initiator details by {initiatorId}

Get the initiator details by {initiatorId}

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
initiator_id = 'initiator_id_example' # str | UID of SC Initiator.

try:
    # Get the initiator details by {initiatorId}
    api_response = api_instance.host_initiator_get_by_id(initiator_id)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_initiator_list**
> InitiatorList host_initiator_list(filter=filter, sort=sort, limit=limit, offset=offset)

Get the list of initiators

Get the list of initiators

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
filter = 'filter_example' # str | oData query to filter hostservice by Key. (optional)
sort = 'sort_example' # str | oData query to sort hostservice by Key. (optional)
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)

try:
    # Get the list of initiators
    api_response = api_instance.host_initiator_list(filter=filter, sort=sort, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_list**
> HostsList host_list(filter=filter, sort=sort, limit=limit, offset=offset)

Get the list of hosts

Get the list of hosts

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
filter = 'filter_example' # str | oData query to filter hostservice by Key. (optional)
sort = 'sort_example' # str | oData query to sort hostservice by Key. (optional)
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)

try:
    # Get the list of hosts
    api_response = api_instance.host_list(filter=filter, sort=sort, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_update_by_id**
> TaskResponse host_update_by_id(host_id, update_host_input)

Update Host by {hostId}

Update host details by {hostId}

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
host_id = 'host_id_example' # str | Id of the SC Host.
update_host_input = greenlake-data-services.UpdateHostInput() # UpdateHostInput | 

try:
    # Update Host by {hostId}
    api_response = api_instance.host_update_by_id(host_id, update_host_input)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_volume_performance_history_get**
> HostStoragePerformanceHistory host_volume_performance_history_get(host_id, select=select, range=range, time_interval_min=time_interval_min, top_volumes_count=top_volumes_count)

Get the volume performance history data associated with a host identified by {uid}

Get the volume performance history data associated with a host identified by {uid}

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
host_id = 'host_id_example' # str | Id of the SC Host.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
time_interval_min = 56 # int | It defines granularity in minutes. (optional)
top_volumes_count = 56 # int | The number of top volumes to be returned, by default it will be 5 (optional)

try:
    # Get the volume performance history data associated with a host identified by {uid}
    api_response = api_instance.host_volume_performance_history_get(host_id, select=select, range=range, time_interval_min=time_interval_min, top_volumes_count=top_volumes_count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HostInitiatorsApi->host_volume_performance_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Id of the SC Host. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 
 **top_volumes_count** | **int**| The number of top volumes to be returned, by default it will be 5 | [optional] 

### Return type

[**HostStoragePerformanceHistory**](HostStoragePerformanceHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **host_volumes_get**
> HostStorageVolumes host_volumes_get(host_id, select=select)

Get details of volumes associated with a host identified by {uid}

Get details of volumes associated with a host identified by {uid}

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
api_instance = greenlake-data-services.HostInitiatorsApi(greenlake-data-services.ApiClient(configuration))
host_id = 'host_id_example' # str | Id of the SC Host.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of volumes associated with a host identified by {uid}
    api_response = api_instance.host_volumes_get(host_id, select=select)
    pprint(api_response)
except ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

