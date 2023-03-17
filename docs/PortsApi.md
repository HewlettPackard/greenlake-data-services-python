# greenlake-data-services.PortsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_fc_port_edit**](PortsApi.md#device_type1_fc_port_edit) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/fc | Edit ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_iscsi_port_edit**](PortsApi.md#device_type1_iscsi_port_edit) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/edit-iscsi | Edit iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_iscsi_port_ping**](PortsApi.md#device_type1_iscsi_port_ping) | **POST** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/ping-iscsi | Ping iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_ports_clear**](PortsApi.md#device_type1_ports_clear) | **POST** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/clear | Clear the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_ports_get_by_id**](PortsApi.md#device_type1_ports_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/ports/{id} | Get details of Primera / Alletra 9K Port identified by {id}
[**device_type1_ports_list**](PortsApi.md#device_type1_ports_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/ports | Get details of Primera / Alletra 9K Ports
[**device_type1_rcip_port_edit**](PortsApi.md#device_type1_rcip_port_edit) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/edit-rcip | Edit rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_rcip_port_ping**](PortsApi.md#device_type1_rcip_port_ping) | **POST** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/ping-rcip | Ping rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type2_edit_fc_port**](PortsApi.md#device_type2_edit_fc_port) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/ports/{portId} | Edit Nimble FC Port of Nimble / Alletra 6K
[**device_type2_get_all_fibre_channel_configs**](PortsApi.md#device_type2_get_all_fibre_channel_configs) | **GET** /api/v1/storage-systems/device-type2/{systemId}/fibre-channel-configs | Get all fibre channel configs details of Nimble / Alletra 6K
[**device_type2_get_all_fibre_channel_sessions**](PortsApi.md#device_type2_get_all_fibre_channel_sessions) | **GET** /api/v1/storage-systems/device-type2/{systemId}/fibre-channel-sessions | Get all fibre channel sessions details of Nimble / Alletra 6K
[**device_type2_get_all_ports**](PortsApi.md#device_type2_get_all_ports) | **GET** /api/v1/storage-systems/device-type2/{systemId}/ports | Get all ports details of Nimble / Alletra 6K
[**device_type2_get_fibre_channel_config_by_id**](PortsApi.md#device_type2_get_fibre_channel_config_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/fibre-channel-configs/{fcConfigId} | Get fibre channel configs details of Nimble / Alletra 6K identified by {fcConfigId}.
[**device_type2_get_fibre_channel_session_by_id**](PortsApi.md#device_type2_get_fibre_channel_session_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/fibre-channel-sessions/{fcSessionId} | Get fibre channel session details of Nimble / Alletra 6K identified by {fcSessionId}.
[**device_type2_get_port_by_id**](PortsApi.md#device_type2_get_port_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/ports/{portId} | Get details of Nimble / Alletra 6K Port identified by {portId}. Fibre_channel_interfaces attributes will be shown for Fibre_channel_interface ports. Network_interfaces attributes will be shown for Network_interface ports.
[**get_device_type2_network_interface_by_id**](PortsApi.md#get_device_type2_network_interface_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/network-interfaces/{networkInterfaceId} | Get all network interfaces details by Nimble / Alletra 6K identified  by {networkInterfaceId}
[**get_device_type2_network_interfaces**](PortsApi.md#get_device_type2_network_interfaces) | **GET** /api/v1/storage-systems/device-type2/{systemId}/network-interfaces | Get all network interfaces details by Nimble / Alletra 6K
[**initialise_ports**](PortsApi.md#initialise_ports) | **POST** /api/v1/storage-systems/device-type1/{systemId}/ports/{id}/initialize | Initialize the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}
[**port_enable**](PortsApi.md#port_enable) | **POST** /api/v1/storage-systems/device-type1/{systemId}/ports/{id} | Port enable disable identified by {id} from Primera / Alletra 9K identified by {systemId}


# **device_type1_fc_port_edit**
> TaskResponse device_type1_fc_port_edit(system_id, id, port_fc_edit)

Edit ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Edit ports identified by {id} from Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the port
port_fc_edit = greenlake-data-services.PortFCEdit() # PortFCEdit | 

try:
    # Edit ports identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_fc_port_edit(system_id, id, port_fc_edit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type1_fc_port_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the port | 
 **port_fc_edit** | [**PortFCEdit**](PortFCEdit.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_iscsi_port_edit**
> TaskResponse device_type1_iscsi_port_edit(system_id, id, port_iscsi_edit)

Edit iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Edit iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the port
port_iscsi_edit = greenlake-data-services.PortISCSIEdit() # PortISCSIEdit | 

try:
    # Edit iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_iscsi_port_edit(system_id, id, port_iscsi_edit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type1_iscsi_port_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the port | 
 **port_iscsi_edit** | [**PortISCSIEdit**](PortISCSIEdit.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_iscsi_port_ping**
> TaskResponse device_type1_iscsi_port_ping(system_id, id, port_iscsi_ping)

Ping iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Ping iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the port
port_iscsi_ping = greenlake-data-services.PortISCSIPing() # PortISCSIPing | 

try:
    # Ping iscsi ports identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_iscsi_port_ping(system_id, id, port_iscsi_ping)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type1_iscsi_port_ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the port | 
 **port_iscsi_ping** | [**PortISCSIPing**](PortISCSIPing.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_ports_clear**
> TaskResponse device_type1_ports_clear(system_id, id, port_clear_input=port_clear_input)

Clear the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Clear the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the port
port_clear_input = greenlake-data-services.PortClearInput() # PortClearInput |  (optional)

try:
    # Clear the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_ports_clear(system_id, id, port_clear_input=port_clear_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type1_ports_clear: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the port | 
 **port_clear_input** | [**PortClearInput**](PortClearInput.md)|  | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_ports_get_by_id**
> PortDetails device_type1_ports_get_by_id(system_id, id, select=select)

Get details of Primera / Alletra 9K Port identified by {id}

Get details of Primera / Alletra 9K Port identified by {id}

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the port
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Primera / Alletra 9K Port identified by {id}
    api_response = api_instance.device_type1_ports_get_by_id(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type1_ports_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the port | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PortDetails**](PortDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_ports_list**
> PortsSummaryList device_type1_ports_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of Primera / Alletra 9K Ports

Get details of Primera / Alletra 9K Ports

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter ports by Key. (optional)
sort = 'sort_example' # str | oData query to sort ports by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Primera / Alletra 9K Ports
    api_response = api_instance.device_type1_ports_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type1_ports_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter ports by Key. | [optional] 
 **sort** | **str**| oData query to sort ports by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PortsSummaryList**](PortsSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_rcip_port_edit**
> TaskResponse device_type1_rcip_port_edit(system_id, id, port_rcip_edit)

Edit rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Edit rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the port
port_rcip_edit = greenlake-data-services.PortRCIPEdit() # PortRCIPEdit | 

try:
    # Edit rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_rcip_port_edit(system_id, id, port_rcip_edit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type1_rcip_port_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the port | 
 **port_rcip_edit** | [**PortRCIPEdit**](PortRCIPEdit.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_rcip_port_ping**
> TaskResponse device_type1_rcip_port_ping(system_id, id, port_rcip_ping)

Ping rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Ping rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the port
port_rcip_ping = greenlake-data-services.PortRCIPPing() # PortRCIPPing | 

try:
    # Ping rcip ports identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_rcip_port_ping(system_id, id, port_rcip_ping)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type1_rcip_port_ping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the port | 
 **port_rcip_ping** | [**PortRCIPPing**](PortRCIPPing.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_fc_port**
> TaskResponse device_type2_edit_fc_port(system_id, port_id, nimble_edit_fc_interface_input)

Edit Nimble FC Port of Nimble / Alletra 6K

Edit Nimble FC Port of Nimble / Alletra 6K

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
port_id = 'port_id_example' # str | Identifier of port. A 42 digit hexadecimal number.
nimble_edit_fc_interface_input = greenlake-data-services.NimbleEditFCInterfaceInput() # NimbleEditFCInterfaceInput | 

try:
    # Edit Nimble FC Port of Nimble / Alletra 6K
    api_response = api_instance.device_type2_edit_fc_port(system_id, port_id, nimble_edit_fc_interface_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type2_edit_fc_port: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **port_id** | **str**| Identifier of port. A 42 digit hexadecimal number. | 
 **nimble_edit_fc_interface_input** | [**NimbleEditFCInterfaceInput**](NimbleEditFCInterfaceInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_fibre_channel_configs**
> NimbleFCConfigsList device_type2_get_all_fibre_channel_configs(system_id, limit=limit, offset=offset, filter=filter, select=select)

Get all fibre channel configs details of Nimble / Alletra 6K

Get all fibre channel configs details of Nimble / Alletra 6K

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter Fibre Channel Configs by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all fibre channel configs details of Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_fibre_channel_configs(system_id, limit=limit, offset=offset, filter=filter, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type2_get_all_fibre_channel_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Fibre Channel Configs by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleFCConfigsList**](NimbleFCConfigsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_fibre_channel_sessions**
> NimbleFCSessionList device_type2_get_all_fibre_channel_sessions(system_id, limit=limit, offset=offset, filter=filter, select=select)

Get all fibre channel sessions details of Nimble / Alletra 6K

Get all fibre channel sessions details of Nimble / Alletra 6K

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter Fibre Channel Sessions by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all fibre channel sessions details of Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_fibre_channel_sessions(system_id, limit=limit, offset=offset, filter=filter, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type2_get_all_fibre_channel_sessions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Fibre Channel Sessions by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleFCSessionList**](NimbleFCSessionList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_ports**
> NimblePortsList device_type2_get_all_ports(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all ports details of Nimble / Alletra 6K

Get all ports details of Nimble / Alletra 6K

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter fibre channel interface ports by Key. (optional)
sort = 'sort_example' # str | oData query to sort fibre channel interface ports resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all ports details of Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_ports(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type2_get_all_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter fibre channel interface ports by Key. | [optional] 
 **sort** | **str**| oData query to sort fibre channel interface ports resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimblePortsList**](NimblePortsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_fibre_channel_config_by_id**
> NimblefibreChannelConfigsWithRequestUri device_type2_get_fibre_channel_config_by_id(system_id, fc_config_id, select=select)

Get fibre channel configs details of Nimble / Alletra 6K identified by {fcConfigId}.

Get fibre channel configs details of Nimble / Alletra 6K identified by {fcConfigId}.

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
fc_config_id = 'fc_config_id_example' # str | Identifier of fibre channel config. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get fibre channel configs details of Nimble / Alletra 6K identified by {fcConfigId}.
    api_response = api_instance.device_type2_get_fibre_channel_config_by_id(system_id, fc_config_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type2_get_fibre_channel_config_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **fc_config_id** | **str**| Identifier of fibre channel config. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimblefibreChannelConfigsWithRequestUri**](NimblefibreChannelConfigsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_fibre_channel_session_by_id**
> NimbleFCSessionDetailsWithRequestUri device_type2_get_fibre_channel_session_by_id(system_id, fc_session_id, select=select)

Get fibre channel session details of Nimble / Alletra 6K identified by {fcSessionId}.

Get fibre channel session details of Nimble / Alletra 6K identified by {fcSessionId}.

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
fc_session_id = 'fc_session_id_example' # str | ID of the Fibre Channel Session. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get fibre channel session details of Nimble / Alletra 6K identified by {fcSessionId}.
    api_response = api_instance.device_type2_get_fibre_channel_session_by_id(system_id, fc_session_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type2_get_fibre_channel_session_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **fc_session_id** | **str**| ID of the Fibre Channel Session. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleFCSessionDetailsWithRequestUri**](NimbleFCSessionDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_port_by_id**
> NimblePortDetails device_type2_get_port_by_id(system_id, port_id, select=select)

Get details of Nimble / Alletra 6K Port identified by {portId}. Fibre_channel_interfaces attributes will be shown for Fibre_channel_interface ports. Network_interfaces attributes will be shown for Network_interface ports.

Get details of Nimble / Alletra 6K Port identified by {portId}.

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
port_id = 'port_id_example' # str | Identifier of port. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K Port identified by {portId}. Fibre_channel_interfaces attributes will be shown for Fibre_channel_interface ports. Network_interfaces attributes will be shown for Network_interface ports.
    api_response = api_instance.device_type2_get_port_by_id(system_id, port_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->device_type2_get_port_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **port_id** | **str**| Identifier of port. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimblePortDetails**](NimblePortDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type2_network_interface_by_id**
> NimbleNetworkInterfaceWithRequestUri get_device_type2_network_interface_by_id(system_id, network_interface_id, select=select)

Get all network interfaces details by Nimble / Alletra 6K identified  by {networkInterfaceId}

Get all network interfaces details by Nimble / Alletra 6K identified by {networkInterfaceId}

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
network_interface_id = 'network_interface_id_example' # str | ID of the Network Interface. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all network interfaces details by Nimble / Alletra 6K identified  by {networkInterfaceId}
    api_response = api_instance.get_device_type2_network_interface_by_id(system_id, network_interface_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->get_device_type2_network_interface_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **network_interface_id** | **str**| ID of the Network Interface. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleNetworkInterfaceWithRequestUri**](NimbleNetworkInterfaceWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_type2_network_interfaces**
> NimbleNetworkInterfaceList get_device_type2_network_interfaces(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all network interfaces details by Nimble / Alletra 6K

Get all network interfaces details by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter Network Interface by Key. (optional)
sort = 'sort_example' # str | oData query to sort Network Interface resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all network interfaces details by Nimble / Alletra 6K
    api_response = api_instance.get_device_type2_network_interfaces(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->get_device_type2_network_interfaces: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Network Interface by Key. | [optional] 
 **sort** | **str**| oData query to sort Network Interface resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleNetworkInterfaceList**](NimbleNetworkInterfaceList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialise_ports**
> TaskResponse initialise_ports(system_id, id)

Initialize the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}

Initialize the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the port

try:
    # Initialize the details of the ports identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.initialise_ports(system_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->initialise_ports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the port | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **port_enable**
> TaskResponse port_enable(system_id, id, port_enable_input)

Port enable disable identified by {id} from Primera / Alletra 9K identified by {systemId}

Port enable disable identified by {id} from Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.PortsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the port
port_enable_input = greenlake-data-services.PortEnableInput() # PortEnableInput | 

try:
    # Port enable disable identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.port_enable(system_id, id, port_enable_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortsApi->port_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the port | 
 **port_enable_input** | [**PortEnableInput**](PortEnableInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

