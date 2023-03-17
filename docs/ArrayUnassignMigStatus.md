# ArrayUnassignMigStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_migrated** | **int** | Number of bytes already migrated to the destination arrays. | [optional] 
**bytes_remaining** | **int** | Number of bytes yet to be migrated to the destination arrays. | [optional] 
**destination_arrays** | [**list[NimbleArrSummary]**](NimbleArrSummary.md) | List of arrays to which data is being migrated. | [optional] 
**estimated_completion_time** | **int** | Estimated completion time. 0 if unknown. | [optional] 
**id** | **str** | Unique identifier of the array being unassigned. | [optional] 
**name** | **str** | Name of the array being unassigned. | [optional] 
**start_time** | **int** | Time when array unassign operation started. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


