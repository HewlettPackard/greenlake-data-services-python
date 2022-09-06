# NimbleHealthStatusDetailsWithRequestUri


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str, none_type** | requestUri for detailed health status object | [optional] 
**array_id** | **str, none_type** | Identifier of the array to which this result belongs. | [optional] 
**context** | **str, none_type** | Context for aggregating health check results. Possible values: &#39;all&#39;, &#39;failover&#39;, &#39;sw_update&#39;. | [optional] 
**ctrlr_id** | **str, none_type** | Identifier of the controller to which this result belongs. | [optional] 
**id** | **str, none_type** | Identifier for the health check. | [optional] 
**scope** | **str, none_type** | Scope at which the health check is to be run.Possible values: &#39;controller&#39;, &#39;array&#39;, &#39;group&#39;. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**element_result** | [**NimbleHCFResult**](NimbleHCFResult.md) |  | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**on_demand** | **bool, none_type** | Flag to indicate running the health checks and then report results. | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


