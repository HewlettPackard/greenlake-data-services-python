# NimbleMergePoolInput

Merge the specified pool into the target pool. All volumes on the specified pool are moved to the target pool and the specified pool is then deleted. All the arrays in the pool are assigned to the target pool.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_pool_id** | **str** | ID of the target pool. A 42 digit hexadecimal number. | 
**force** | **bool, none_type** | Forcibly merge the specified pool into target pool. Defaults to false. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


