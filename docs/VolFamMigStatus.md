# VolFamMigStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_list** | [**list[ArrayMigStatus]**](ArrayMigStatus.md) | Data migration status for the arrays that store the volumes. | [optional] 
**dest_pool_id** | **str** | ID of the destination pool, where the volumes are moved. | [optional] 
**dest_pool_name** | **str** | Name of the destination pool, where the volumes are moved. | [optional] 
**move_bytes_migrated** | **int** | The bytes of volumes which have been moved. | [optional] 
**move_bytes_remaining** | **int** | The bytes of volumes which have not been moved. | [optional] 
**move_est_compl_time** | **int** | The estimated time of completion of a move. | [optional] 
**move_start_time** | **int** | The start time when the volumes was moved. | [optional] 
**root_vol_id** | **str** | ID of the root volume in the group. | [optional] 
**root_vol_name** | **str** | Name of the root volume in the group. | [optional] 
**source_pool_id** | **str** | ID of the source pool, where the volumes originally locate. | [optional] 
**source_pool_name** | **str** | Name of the source pool, where the volumes originally locate. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


