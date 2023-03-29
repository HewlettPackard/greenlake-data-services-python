# NimbleSpaceDomainListItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_category_id** | **str, none_type** | Identifier of the application category associated with the space domain. &#x60;Filter&#x60; | [optional] 
**app_category_name** | **str, none_type** | Name of the application category associated with the space domain. &#x60;Filter&#x60; | [optional] 
**block_size** | **int, none_type** | Block size in bytes of volumes belonging to the space domain. &#x60;Sort&#x60; | [optional] 
**clone_ratio** | **float, none_type** | Clone savings for the space domain expressed as ratio. &#x60;Sort&#x60; | [optional] 
**compressed_usage_bytes** | **int, none_type** | Compressed usage of volumes and snapshots in the space domain. &#x60;Sort&#x60; | [optional] 
**compression_ratio** | **float, none_type** | Compression savings for the space domain expressed as ratio. &#x60;Sort&#x60; | [optional] 
**dedupe_ratio** | **float, none_type** | Deduplication savings for the space domain expressed as ratio. &#x60;Sort&#x60; | [optional] 
**deduped** | **bool, none_type** | Volumes in space domain are deduplicated by default. &#x60;Filter, Sort&#x60; | [optional] 
**encrypted** | **bool, none_type** | Volumes in space domain are encrypted. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str, none_type** | Identifier of the application summery. &#x60;Filter&#x60; | [optional] 
**logical_dedupe_usage** | **int, none_type** | Logical space usage of volumes when deduped. &#x60;Sort&#x60; | [optional] 
**physical_dedupe_usage** | **int, none_type** | Physical space usage of volumes including snapshots when deduped. &#x60;Sort&#x60; | [optional] 
**pool_id** | **str, none_type** | Identifier associated with the pool in the storage pool table. &#x60;Filter&#x60; | [optional] 
**pool_name** | **str, none_type** | Name of the pool containing the space domain. &#x60;Filter&#x60; | [optional] 
**savings_clone** | **int, none_type** | Space usage savings in the space domain due to cloning of volumes. &#x60;Sort&#x60; | [optional] 
**savings_compression** | **int, none_type** | Space usage savings in the space domain due to compression. &#x60;Sort&#x60; | [optional] 
**savings_dedupe** | **int, none_type** | Space usage savings in the space domain due to deduplication. &#x60;Sort&#x60; | [optional] 
**snap_logical_usage** | **int, none_type** | Logical usage of snapshots in the space domain. &#x60;Sort&#x60; | [optional] 
**uncompressed_usage_bytes** | **int, none_type** | Uncompressed usage of volumes and snapshots in the space domain. &#x60;Sort&#x60; | [optional] 
**usage** | **int, none_type** | Physical space usage of volumes in the space domain. &#x60;Sort&#x60; | [optional] 
**vol_logical_usage** | **int, none_type** | Logical usage of volumes in the space domain. &#x60;Sort&#x60; | [optional] 
**vol_mapped_usage** | **int, none_type** | Mapped usage of volumes in the space domain, useful for computing clone savings. &#x60;Sort&#x60; | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**deduped_volume_count** | **int, none_type** | Number of deduplicated volumes belonging to the space domain. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**perf_policy_names** | [**[NimblePerfPolicySummary], none_type**](NimblePerfPolicySummary.md) | Name of the performance policies associated with the space domain. | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**sample_rate** | **int, none_type** | Sample rate value. | [optional] 
**type** | **str, none_type** | type | [optional] 
**volume_count** | **int, none_type** | Number of volumes belonging to the space domain. | [optional] 
**volumes** | [**[NimbleVolumeSummary], none_type**](NimbleVolumeSummary.md) | Volumes belonging to the space domain. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


