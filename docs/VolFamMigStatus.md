# VolFamMigStatus

Data migration status for a group of related volumes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_list** | [**[ArrayMigStatus], none_type**](ArrayMigStatus.md) | Data migration status for the arrays that store the volumes. | [optional] 
**dest_pool_id** | **str, none_type** | ID of the destination pool, where the volumes are moved. | [optional] 
**dest_pool_name** | **str, none_type** | Name of the destination pool, where the volumes are moved. | [optional] 
**move_bytes_migrated** | **int, none_type** | The bytes of volumes which have been moved. | [optional] 
**move_bytes_remaining** | **int, none_type** | The bytes of volumes which have not been moved. | [optional] 
**move_est_compl_time** | **int, none_type** | The estimated time of completion of a move. | [optional] 
**move_start_time** | **int, none_type** | The start time when the volumes was moved. | [optional] 
**root_vol_id** | **str, none_type** | ID of the root volume in the group. | [optional] 
**root_vol_name** | **str, none_type** | Name of the root volume in the group. | [optional] 
**source_pool_id** | **str, none_type** | ID of the source pool, where the volumes originally locate. | [optional] 
**source_pool_name** | **str, none_type** | Name of the source pool, where the volumes originally locate. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


