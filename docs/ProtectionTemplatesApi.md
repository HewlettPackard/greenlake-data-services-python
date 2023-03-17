# greenlake-data-services.ProtectionTemplatesApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_create_protection_template**](ProtectionTemplatesApi.md#device_type2_create_protection_template) | **POST** /api/v1/storage-systems/device-type2/{systemId}/protection-templates | Create protection template on Nimble / Alletra 6K in system identified by {systemId}
[**device_type2_edit_protection_template**](ProtectionTemplatesApi.md#device_type2_edit_protection_template) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/protection-templates/{protectionTemplateId} | Edit details of Nimble / Alletra 6K Protection-templates identified by {protectionTemplateId}
[**device_type2_get_all_protection_templates**](ProtectionTemplatesApi.md#device_type2_get_all_protection_templates) | **GET** /api/v1/storage-systems/device-type2/{systemId}/protection-templates | Get all protection-templates details by Nimble / Alletra 6K
[**device_type2_get_protection_template_by_id**](ProtectionTemplatesApi.md#device_type2_get_protection_template_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/protection-templates/{protectionTemplateId} | Get details of Nimble / Alletra 6K protection-templates identified by {protectionTemplateId}
[**device_type2_remove_protection_template**](ProtectionTemplatesApi.md#device_type2_remove_protection_template) | **POST** /api/v1/storage-systems/device-type2/{systemId}/protection-templates/remove | Remove protection templates for Nimble / Alletra 6K


# **device_type2_create_protection_template**
> TaskResponse device_type2_create_protection_template(system_id, nimble_create_protection_template_input)

Create protection template on Nimble / Alletra 6K in system identified by {systemId}

Create protection template on Nimble / Alletra 6K in system identified by {systemId}

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
api_instance = greenlake-data-services.ProtectionTemplatesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_protection_template_input = greenlake-data-services.NimbleCreateProtectionTemplateInput() # NimbleCreateProtectionTemplateInput | 

try:
    # Create protection template on Nimble / Alletra 6K in system identified by {systemId}
    api_response = api_instance.device_type2_create_protection_template(system_id, nimble_create_protection_template_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectionTemplatesApi->device_type2_create_protection_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_protection_template_input** | [**NimbleCreateProtectionTemplateInput**](NimbleCreateProtectionTemplateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_protection_template**
> TaskResponse device_type2_edit_protection_template(system_id, protection_template_id, nimble_edit_protection_template_input)

Edit details of Nimble / Alletra 6K Protection-templates identified by {protectionTemplateId}

Edit  details of Nimble / Alletra 6K Protection-templates identified by {protectionTemplateId}

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
api_instance = greenlake-data-services.ProtectionTemplatesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
protection_template_id = 'protection_template_id_example' # str | ID of the Protection Template. A 42 digit hexadecimal number.
nimble_edit_protection_template_input = greenlake-data-services.NimbleEditProtectionTemplateInput() # NimbleEditProtectionTemplateInput | 

try:
    # Edit details of Nimble / Alletra 6K Protection-templates identified by {protectionTemplateId}
    api_response = api_instance.device_type2_edit_protection_template(system_id, protection_template_id, nimble_edit_protection_template_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectionTemplatesApi->device_type2_edit_protection_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **protection_template_id** | **str**| ID of the Protection Template. A 42 digit hexadecimal number. | 
 **nimble_edit_protection_template_input** | [**NimbleEditProtectionTemplateInput**](NimbleEditProtectionTemplateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_protection_templates**
> NimbleProtectionTemplateList device_type2_get_all_protection_templates(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all protection-templates details by Nimble / Alletra 6K

Get all protection-templates details by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.ProtectionTemplatesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter Protection Template  by Key. (optional)
sort = 'sort_example' # str | oData query to sort Protection Template  resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all protection-templates details by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_protection_templates(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectionTemplatesApi->device_type2_get_all_protection_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Protection Template  by Key. | [optional] 
 **sort** | **str**| oData query to sort Protection Template  resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleProtectionTemplateList**](NimbleProtectionTemplateList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_protection_template_by_id**
> NimbleProtectionTemplateDetailsWithRequestUri device_type2_get_protection_template_by_id(system_id, protection_template_id, select=select)

Get details of Nimble / Alletra 6K protection-templates identified by {protectionTemplateId}

Get details of Nimble / Alletra 6K protection-templates identified by {protectionTemplateId}

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
api_instance = greenlake-data-services.ProtectionTemplatesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
protection_template_id = 'protection_template_id_example' # str | ID of the Protection Template. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K protection-templates identified by {protectionTemplateId}
    api_response = api_instance.device_type2_get_protection_template_by_id(system_id, protection_template_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectionTemplatesApi->device_type2_get_protection_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **protection_template_id** | **str**| ID of the Protection Template. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleProtectionTemplateDetailsWithRequestUri**](NimbleProtectionTemplateDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_protection_template**
> TaskResponse device_type2_remove_protection_template(system_id, remove_protection_templates)

Remove protection templates for Nimble / Alletra 6K

Remove protection templates for Nimble / Alletra 6K

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
api_instance = greenlake-data-services.ProtectionTemplatesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
remove_protection_templates = greenlake-data-services.RemoveProtectionTemplates() # RemoveProtectionTemplates | 

try:
    # Remove protection templates for Nimble / Alletra 6K
    api_response = api_instance.device_type2_remove_protection_template(system_id, remove_protection_templates)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectionTemplatesApi->device_type2_remove_protection_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **remove_protection_templates** | [**RemoveProtectionTemplates**](RemoveProtectionTemplates.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

