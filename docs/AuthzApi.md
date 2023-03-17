# greenlake-data-services.AuthzApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_controls**](AuthzApi.md#get_access_controls) | **GET** /api/v1/access-controls | Get User Accessible Resources
[**get_resource_types**](AuthzApi.md#get_resource_types) | **GET** /api/v1/resource-types | Get resource types with read permissions


# **get_access_controls**
> AccessControlsResponse get_access_controls(permission=permission)

Get User Accessible Resources

Retun a list of user permissions.  The returned list of permissions will be based upon the supplied filter.  If no filter was supplied, all user permissions will be returned. It is also possible to request all resource type with certain permission type (ex. ALL.read)

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
api_instance = greenlake-data-services.AuthzApi(greenlake-data-services.ApiClient(configuration))
permission = ['permission_example'] # list[str] | List of permissions, each of which, has the form \"resource type.permission\" (ex. volume.read,volume.write). The word \"ANY\" can be used as a wild card for the resource type (ex. ANY.read). Omitting the permission parameters is equivalent to asking for all user permissions. (optional)

try:
    # Get User Accessible Resources
    api_response = api_instance.get_access_controls(permission=permission)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthzApi->get_access_controls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **permission** | [**list[str]**](str.md)| List of permissions, each of which, has the form \&quot;resource type.permission\&quot; (ex. volume.read,volume.write). The word \&quot;ANY\&quot; can be used as a wild card for the resource type (ex. ANY.read). Omitting the permission parameters is equivalent to asking for all user permissions. | [optional] 

### Return type

[**AccessControlsResponse**](AccessControlsResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resource_types**
> ResourceTypesResponse get_resource_types()

Get resource types with read permissions

Return resource types on which the user has a read permission.  The returned list will be based upon the supplied filter.  If no filter was provided, all resource types for which the user has a read permission on will be returned

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
api_instance = greenlake-data-services.AuthzApi(greenlake-data-services.ApiClient(configuration))

try:
    # Get resource types with read permissions
    api_response = api_instance.get_resource_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthzApi->get_resource_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ResourceTypesResponse**](ResourceTypesResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

