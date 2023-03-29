# ArrayUnassignMigStatus

Data migration status for array being unassigned from its pool.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_migrated** | **int, none_type** | Number of bytes already migrated to the destination arrays. | [optional] 
**bytes_remaining** | **int, none_type** | Number of bytes yet to be migrated to the destination arrays. | [optional] 
**destination_arrays** | [**[NimbleArrSummary], none_type**](NimbleArrSummary.md) | List of arrays to which data is being migrated. | [optional] 
**estimated_completion_time** | **int, none_type** | Estimated completion time. 0 if unknown. | [optional] 
**id** | **str, none_type** | Unique identifier of the array being unassigned. | [optional] 
**name** | **str, none_type** | Name of the array being unassigned. | [optional] 
**start_time** | **int, none_type** | Time when array unassign operation started. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


