# NimblePerformancePolicyDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**block_size** | **int, none_type** | Block Size in bytes to be used by the volumes created with this specific performance policy. Supported block sizes are 4096 bytes (4 KB), 8192 bytes (8 KB), 16384 bytes(16 KB), and 32768 bytes (32 KB). Block size of a performance policy cannot be changed once the performance policy is created. | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**dedupe_override_pools** | [**[NimbleNsPoolSummary], none_type**](NimbleNsPoolSummary.md) | List of pools that override performance policy&#39;s dedupe setting. | [optional] 
**description** | **str, none_type** | Description of a performance policy. | [optional] 
**full_name** | **str, none_type** | Fully qualified name of the Performance Policy. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**search_name** | **str, none_type** | Name of the Performance Policy used for object search. | [optional] 
**type** | **str, none_type** | type | [optional] 
**volume_count** | **int, none_type** | Number of volumes using this performance policy. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


