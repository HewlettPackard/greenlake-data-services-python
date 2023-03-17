# greenlake-data-services.TasksApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_task**](TasksApi.md#get_task) | **GET** /api/v1/tasks/{id} | Returns details of a specific task
[**list_tasks**](TasksApi.md#list_tasks) | **GET** /api/v1/tasks | Returns a list of tasks accessible by the user


# **get_task**
> Task get_task(id)

Returns details of a specific task

Returns the task with the given id.

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
api_instance = greenlake-data-services.TasksApi(greenlake-data-services.ApiClient(configuration))
id = 'id_example' # str | The UUID of the object

try:
    # Returns details of a specific task
    api_response = api_instance.get_task(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->get_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The UUID of the object | 

### Return type

[**Task**](Task.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tasks**
> TaskList list_tasks(offset=offset, limit=limit, filter=filter)

Returns a list of tasks accessible by the user

Returns a list of tasks that are visible to the user. The response can be paged by using the limit and offset query parameters and filtered, sorted and ordered by using the filter, sortby and orderby query parameters. 

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
api_instance = greenlake-data-services.TasksApi(greenlake-data-services.ApiClient(configuration))
offset = 56 # int | The offset query parameter should be used in conjunction with limit for paging, e.g.: offset=30&&limit=10. The offset is the number of items from the beginning of the result set to the first item included in the response.  (optional)
limit = 56 # int | The limit query parameter should be used in conjunction with offset for paging, e.g.: offset=30&&limit=10. The limit is the maximum number of items to include in the response.  (optional)
filter = 'filter_example' # str | The expression to filter responses. (optional)

try:
    # Returns a list of tasks accessible by the user
    api_response = api_instance.list_tasks(offset=offset, limit=limit, filter=filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TasksApi->list_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset query parameter should be used in conjunction with limit for paging, e.g.: offset&#x3D;30&amp;&amp;limit&#x3D;10. The offset is the number of items from the beginning of the result set to the first item included in the response.  | [optional] 
 **limit** | **int**| The limit query parameter should be used in conjunction with offset for paging, e.g.: offset&#x3D;30&amp;&amp;limit&#x3D;10. The limit is the maximum number of items to include in the response.  | [optional] 
 **filter** | **str**| The expression to filter responses. | [optional] 

### Return type

[**TaskList**](TaskList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

