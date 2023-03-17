# greenlake-data-services.IssuesApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_issue**](IssuesApi.md#get_issue) | **GET** /api/v1/issues/{id} | Returns the active issue with the given Id
[**list_issues**](IssuesApi.md#list_issues) | **GET** /api/v1/issues | Returns a list of active issues associated with the account, scoped by the user&#39;s permissions


# **get_issue**
> IssueDetails get_issue(id, select=select)

Returns the active issue with the given Id

Returns the active issue (state=\"CREATED\") associated with the account (retrieved from the request headers) and with given Id

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
api_instance = greenlake-data-services.IssuesApi(greenlake-data-services.ApiClient(configuration))
id = 'id_example' # str | The UUID of the issue
select = 'select_example' # str | The select query parameter is used to limit the properties returned with a resource or collection-level GET. Multiple properties can be listed to be returned. The server must only return the set of properties requested by the client. The property “select” is the name of the select query parameter; its value is the list of properties to return separated by commas.  (optional)

try:
    # Returns the active issue with the given Id
    api_response = api_instance.get_issue(id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->get_issue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The UUID of the issue | 
 **select** | **str**| The select query parameter is used to limit the properties returned with a resource or collection-level GET. Multiple properties can be listed to be returned. The server must only return the set of properties requested by the client. The property “select” is the name of the select query parameter; its value is the list of properties to return separated by commas.  | [optional] 

### Return type

[**IssueDetails**](IssueDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_issues**
> IssuesList list_issues(offset=offset, limit=limit, filter=filter, sort=sort, select=select)

Returns a list of active issues associated with the account, scoped by the user's permissions

Returns the active (state=\"CREATED\") issues for the account, which are associated with the resource-types for which the user has access. The user should also have the permission to view issues. Eg: if there are issues associated with 50 resources (of different resource-types) for a customer (obtained from the request header), and the user (obtained from the request headers), who has correct permissions to view the issues but has acceess to only 20 of those resources (ie access to their resource types), this API will return only the issues associated with those 20 resources. The grouped issues are places next to each other. The client will have to process them for any desired grouping 

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
api_instance = greenlake-data-services.IssuesApi(greenlake-data-services.ApiClient(configuration))
offset = 56 # int | The number of items to skip before starting to collect the result set (optional)
limit = 56 # int | The numbers of items to return (optional)
filter = 'filter_example' # str | The filter query parameter is used to filter the set of resources returned in the response. The returned set of resources must match the criteria in the filter query parameter A comparision compares a property name to a literal. The comparisons supported are the following: “eq” : Is a property equal to value. Valid for number, boolean and string properties. “gt” : Is a property greater than a value. Valid for number or string timestamp properties. “lt” : Is a property less than a value. Valid for number or string timestamp properties “in” : Is a value in a property (that is an array of strings) Syntax:  “eq” : filter=<property> eq <value> {host:port}/api/v1/issues?filter=<property> eq <value> “gt” : filter=<property> gt <value> {host:port}/api/v1/issues?filter=<property> gt <value> “lt” : filter=<property> lt <value> {host:port}/api/v1/issues?filter=<property> lt <value> “in” : filter=<property> in <value> {host:port}/api/v1/issues?filter=<property> in <value> * Can use and to add more filter inputs {host:port}/api/v1/issues?filter=<property1> eq <value1> and <property2> lt <value2>  * To filter multiple values on one property e.g. filter=severity in ('CRITICAL','WARNING') {host:port}/api/v1/issues?filter=severity%20in%20CRITICAL%2CWARNING Examples: GET /api/v1/issues?filter=issueType eq 'ISSUE' GET /api/v1/issues?filter=issueType eq 'ISSUE' and state eq 'CREATED' GET /api/v1/issues?filter=relatedObjectType in ('NIMBLE-VOLUME') Filters are supported on following attributes: issueType, severity, category, state, relatedObject (relatedObject.resourceUri), relatedObjectType (relatedObject.type), relatedObjectOwner (relatedObjectOwner.resourceUri), relatedObjectOwnerType (relatedObjectOwner.type), ruleId, createdAt  (optional)
sort = 'sort_example' # str | resource property to sort, with an order appended Order may only be either “asc” (ascending) or “desc” (descending)  (optional)
select = 'select_example' # str | The select query parameter is used to limit the properties returned with a resource or collection-level GET. Multiple properties can be listed to be returned. The server must only return the set of properties requested by the client. The property “select” is the name of the select query parameter; its value is the list of properties to return separated by commas.  (optional)

try:
    # Returns a list of active issues associated with the account, scoped by the user's permissions
    api_response = api_instance.list_issues(offset=offset, limit=limit, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling IssuesApi->list_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of items to skip before starting to collect the result set | [optional] 
 **limit** | **int**| The numbers of items to return | [optional] 
 **filter** | **str**| The filter query parameter is used to filter the set of resources returned in the response. The returned set of resources must match the criteria in the filter query parameter A comparision compares a property name to a literal. The comparisons supported are the following: “eq” : Is a property equal to value. Valid for number, boolean and string properties. “gt” : Is a property greater than a value. Valid for number or string timestamp properties. “lt” : Is a property less than a value. Valid for number or string timestamp properties “in” : Is a value in a property (that is an array of strings) Syntax:  “eq” : filter&#x3D;&lt;property&gt; eq &lt;value&gt; {host:port}/api/v1/issues?filter&#x3D;&lt;property&gt; eq &lt;value&gt; “gt” : filter&#x3D;&lt;property&gt; gt &lt;value&gt; {host:port}/api/v1/issues?filter&#x3D;&lt;property&gt; gt &lt;value&gt; “lt” : filter&#x3D;&lt;property&gt; lt &lt;value&gt; {host:port}/api/v1/issues?filter&#x3D;&lt;property&gt; lt &lt;value&gt; “in” : filter&#x3D;&lt;property&gt; in &lt;value&gt; {host:port}/api/v1/issues?filter&#x3D;&lt;property&gt; in &lt;value&gt; * Can use and to add more filter inputs {host:port}/api/v1/issues?filter&#x3D;&lt;property1&gt; eq &lt;value1&gt; and &lt;property2&gt; lt &lt;value2&gt;  * To filter multiple values on one property e.g. filter&#x3D;severity in (&#39;CRITICAL&#39;,&#39;WARNING&#39;) {host:port}/api/v1/issues?filter&#x3D;severity%20in%20CRITICAL%2CWARNING Examples: GET /api/v1/issues?filter&#x3D;issueType eq &#39;ISSUE&#39; GET /api/v1/issues?filter&#x3D;issueType eq &#39;ISSUE&#39; and state eq &#39;CREATED&#39; GET /api/v1/issues?filter&#x3D;relatedObjectType in (&#39;NIMBLE-VOLUME&#39;) Filters are supported on following attributes: issueType, severity, category, state, relatedObject (relatedObject.resourceUri), relatedObjectType (relatedObject.type), relatedObjectOwner (relatedObjectOwner.resourceUri), relatedObjectOwnerType (relatedObjectOwner.type), ruleId, createdAt  | [optional] 
 **sort** | **str**| resource property to sort, with an order appended Order may only be either “asc” (ascending) or “desc” (descending)  | [optional] 
 **select** | **str**| The select query parameter is used to limit the properties returned with a resource or collection-level GET. Multiple properties can be listed to be returned. The server must only return the set of properties requested by the client. The property “select” is the name of the select query parameter; its value is the list of properties to return separated by commas.  | [optional] 

### Return type

[**IssuesList**](IssuesList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

