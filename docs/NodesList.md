# NodesList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_id** | **int** | Numeric ID of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**associated_links** | [**NodeAssociatedLinks**](NodeAssociatedLinks.md) |  | [optional] 
**bios_version** | **str** | Bios version | [optional] 
**cache_available_pct** | **int** | Percentage of the cache available | [optional] 
**cache_enabled** | **int** | Percentage of the cache enabled on the node | [optional] 
**control_memory_mi_b** | **int** | Total control memory in the node in MiB | [optional] 
**customer_id** | **str** | customerId | [optional] 
**data_memory_mi_b** | **int** | Total data memory in the node in MiB | [optional] 
**displayname** | **str** | Name to be used for display purposes | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Unique Identifier of the resource. &#x60;Filter&#x60; | [optional] 
**in_cluster** | **bool** | Indicates if this node is part of the cluster. | [optional] 
**kernel_version** | **str** | Kernel version | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**manufacturing** | [**ManufacturingSingle**](ManufacturingSingle.md) |  | [optional] 
**master** | **bool** | Indicates if this is the master node. | [optional] 
**name** | **str** | Name of the resource. &#x60;Filter, Sort&#x60; | [optional] 
**online** | **bool** | Indicates if this node is online | [optional] 
**resource_uri** | **str** | resourceUri for detailed node object | [optional] 
**safe_to_remove** | **bool** | Indicates if the component is safe to remove | [optional] 
**service_led** | **str** | LED state. | [optional] 
**state** | [**STATE**](STATE.md) |  | [optional] 
**state_description** | **str** | State of the resource | [optional] 
**system_id** | **str** | SystemId/serialNumber of the array. | [optional] 
**system_led** | [**LED**](LED.md) |  | [optional] 
**type** | **str** | type | [optional] 
**uptime** | [**Nodeuptime**](Nodeuptime.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


