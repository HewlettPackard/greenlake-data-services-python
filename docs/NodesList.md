# NodesList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int, none_type** | Numeric ID of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**associated_links** | [**NodeAssociatedLinks**](NodeAssociatedLinks.md) |  | [optional] 
**bios_version** | **str, none_type** | Bios version | [optional] 
**cache_available_pct** | **int, none_type** | Percentage of the cache available | [optional] 
**cache_enabled** | **int, none_type** | Percentage of the cache enabled on the node | [optional] 
**control_memory_mi_b** | **int, none_type** | Total control memory in the node in MiB | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**data_memory_mi_b** | **int, none_type** | Total data memory in the node in MiB | [optional] 
**displayname** | **str, none_type** | Name to be used for display purposes | [optional] 
**domain** | **str, none_type** | Domain that the resource belongs to | [optional] 
**generation** | **int, none_type** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str, none_type** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**in_cluster** | **bool, none_type** | Indicates if this node is part of the cluster. | [optional] 
**kernel_version** | **str, none_type** | Kernel version | [optional] 
**locate_enabled** | **bool, none_type** | Indicates if the locate beacon is enabled or not | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**master** | **bool, none_type** | Indicates if this is the master node. | [optional] 
**name** | **str, none_type** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**online** | **bool, none_type** | Indicates if this node is online | [optional] 
**resource_uri** | **str, none_type** | resourceUri for detailed node object | [optional] 
**safe_to_remove** | **bool, none_type** | Indicates if the component is safe to remove | [optional] 
**service_led** | **str, none_type** | LED state. | [optional] 
**state** | [**STATE**](STATE.md) |  | [optional] 
**state_description** | **str, none_type** | State of the resource | [optional] 
**system_id** | **str, none_type** | SystemId/serialNumber of the array. | [optional] 
**system_led** | [**LED**](LED.md) |  | [optional] 
**type** | **str, none_type** | type | [optional] 
**uptime** | [**Nodeuptime**](Nodeuptime.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


