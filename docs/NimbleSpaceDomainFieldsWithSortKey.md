# NimbleSpaceDomainFieldsWithSortKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_category_id** | **str** | Identifier of the application category associated with the space domain. &#x60;Filter&#x60; | [optional] 
**app_category_name** | **str** | Name of the application category associated with the space domain. &#x60;Filter&#x60; | [optional] 
**block_size** | **int** | Block size in bytes of volumes belonging to the space domain. &#x60;Sort&#x60; | [optional] 
**clone_ratio** | **float** | Clone savings for the space domain expressed as ratio. &#x60;Sort&#x60; | [optional] 
**compressed_usage_bytes** | **int** | Compressed usage of volumes and snapshots in the space domain. &#x60;Sort&#x60; | [optional] 
**compression_ratio** | **float** | Compression savings for the space domain expressed as ratio. &#x60;Sort&#x60; | [optional] 
**dedupe_ratio** | **float** | Deduplication savings for the space domain expressed as ratio. &#x60;Sort&#x60; | [optional] 
**deduped** | **bool** | Volumes in space domain are deduplicated by default. &#x60;Filter, Sort&#x60; | [optional] 
**encrypted** | **bool** | Volumes in space domain are encrypted. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier of the application summery. &#x60;Filter&#x60; | [optional] 
**logical_dedupe_usage** | **int** | Logical space usage of volumes when deduped. &#x60;Sort&#x60; | [optional] 
**physical_dedupe_usage** | **int** | Physical space usage of volumes including snapshots when deduped. &#x60;Sort&#x60; | [optional] 
**pool_id** | **str** | Identifier associated with the pool in the storage pool table. &#x60;Filter&#x60; | [optional] 
**pool_name** | **str** | Name of the pool containing the space domain. &#x60;Filter&#x60; | [optional] 
**savings_clone** | **int** | Space usage savings in the space domain due to cloning of volumes. &#x60;Sort&#x60; | [optional] 
**savings_compression** | **int** | Space usage savings in the space domain due to compression. &#x60;Sort&#x60; | [optional] 
**savings_dedupe** | **int** | Space usage savings in the space domain due to deduplication. &#x60;Sort&#x60; | [optional] 
**snap_logical_usage** | **int** | Logical usage of snapshots in the space domain. &#x60;Sort&#x60; | [optional] 
**uncompressed_usage_bytes** | **int** | Uncompressed usage of volumes and snapshots in the space domain. &#x60;Sort&#x60; | [optional] 
**usage** | **int** | Physical space usage of volumes in the space domain. &#x60;Sort&#x60; | [optional] 
**vol_logical_usage** | **int** | Logical usage of volumes in the space domain. &#x60;Sort&#x60; | [optional] 
**vol_mapped_usage** | **int** | Mapped usage of volumes in the space domain, useful for computing clone savings. &#x60;Sort&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


