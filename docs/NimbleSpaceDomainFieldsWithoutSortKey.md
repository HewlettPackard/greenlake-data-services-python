# NimbleSpaceDomainFieldsWithoutSortKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_category_id** | **str, none_type** | Identifier of the application category associated with the space domain. | [optional] 
**app_category_name** | **str, none_type** | Name of the application category associated with the space domain. | [optional] 
**block_size** | **int, none_type** | Block size in bytes of volumes belonging to the space domain. | [optional] 
**clone_ratio** | **float, none_type** | Clone savings for the space domain expressed as ratio. | [optional] 
**compressed_usage_bytes** | **int, none_type** | Compressed usage of volumes and snapshots in the space domain. | [optional] 
**compression_ratio** | **float, none_type** | Compression savings for the space domain expressed as ratio. | [optional] 
**dedupe_ratio** | **float, none_type** | Deduplication savings for the space domain expressed as ratio. | [optional] 
**deduped** | **bool, none_type** | Volumes in space domain are deduplicated by default. | [optional] 
**encrypted** | **bool, none_type** | Volumes in space domain are encrypted. | [optional] 
**id** | **str, none_type** | Identifier of the application summery. | [optional] 
**logical_dedupe_usage** | **int, none_type** | Logical space usage of volumes when deduped. | [optional] 
**physical_dedupe_usage** | **int, none_type** | Physical space usage of volumes including snapshots when deduped. | [optional] 
**pool_id** | **str, none_type** | Identifier associated with the pool in the storage pool table. | [optional] 
**pool_name** | **str, none_type** | Name of the pool containing the space domain. | [optional] 
**savings_clone** | **int, none_type** | Space usage savings in the space domain due to cloning of volumes. | [optional] 
**savings_compression** | **int, none_type** | Space usage savings in the space domain due to compression. | [optional] 
**savings_dedupe** | **int, none_type** | Space usage savings in the space domain due to deduplication. | [optional] 
**snap_logical_usage** | **int, none_type** | Logical usage of snapshots in the space domain. | [optional] 
**uncompressed_usage_bytes** | **int, none_type** | Uncompressed usage of volumes and snapshots in the space domain. | [optional] 
**usage** | **int, none_type** | Physical space usage of volumes in the space domain. | [optional] 
**vol_logical_usage** | **int, none_type** | Logical usage of volumes in the space domain. | [optional] 
**vol_mapped_usage** | **int, none_type** | Mapped usage of volumes in the space domain, useful for computing clone savings. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


