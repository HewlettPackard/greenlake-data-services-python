# NimblePerformancePolicyDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**block_size** | **int** | Block Size in bytes to be used by the volumes created with this specific performance policy. Supported block sizes are 4096 bytes (4 KB), 8192 bytes (8 KB), 16384 bytes(16 KB), and 32768 bytes (32 KB). Block size of a performance policy cannot be changed once the performance policy is created. | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dedupe_override_pools** | [**list[NimbleNsPoolSummary]**](NimbleNsPoolSummary.md) | List of pools that override performance policy&#39;s dedupe setting. | [optional] 
**description** | **str** | Description of a performance policy. | [optional] 
**full_name** | **str** | Fully qualified name of the Performance Policy. | [optional] 
**generation** | **int** | generation | [optional] 
**resource_uri** | **str** |  | [optional] 
**search_name** | **str** | Name of the Performance Policy used for object search. | [optional] 
**type** | **str** | type | [optional] 
**volume_count** | **int** | Number of volumes using this performance policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


