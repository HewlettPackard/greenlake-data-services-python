# SnapshotsList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_allocation_settings** | [**UserAllocationSettingsSingle**](UserAllocationSettingsSingle.md) |  | [optional] 
**admin_space** | [**Space**](Space.md) |  | [optional] 
**base_id** | **int, none_type** | snapshot Tdvv Size | [optional] 
**comment** | **str, none_type** | Comments | [optional] 
**compact_efficiency** | **float, none_type** | Compact Efficiency | [optional] 
**compression_efficiency** | **float, none_type** | Compression Efficiency | [optional] 
**compression_policy** | **str, none_type** | compression policy | [optional] 
**conversion_type** | **str, none_type** | Conversion Type of Volume | [optional] 
**copied_mb** | **float, none_type** | Copied MB | [optional] 
**copied_perc** | **int, none_type** | Copied Perecentage | [optional] 
**copy_of_id** | **int, none_type** | Copy of ID | [optional] 
**creation_time** | [**SnapshotsListCreationTime**](SnapshotsListCreationTime.md) |  | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**data_reduction** | **str, none_type** | Data Reduction type | [optional] 
**ddc_size** | **float, none_type** |  | [optional] 
**dds_size** | **float, none_type** |  | [optional] 
**dedup** | **str, none_type** |  | [optional] 
**dedup_savings_size** | **float, none_type** |  | [optional] 
**dedup_written_size** | **float, none_type** |  | [optional] 
**dev_type** | **str, none_type** | Device Type | [optional] 
**displayname** | **str, none_type** | Display name of the volume | [optional] 
**domain** | **str, none_type** | Domain of the volume | [optional] 
**efficiency_update_time** | [**Calendar**](Calendar.md) |  | [optional] 
**expiration_time** | [**Calendar**](Calendar.md) |  | [optional] 
**fully_provisioned** | **bool, none_type** |  | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**heads_per_cylinder** | **int, none_type** | Heads per Cylinder | [optional] 
**health_state** | **int, none_type** | Health status of the Volume. | [optional] 
**hidden** | **bool, none_type** | Flag to know if the Volume is hidden or not | [optional] 
**host_written_mi_b** | **float, none_type** | Host written data size in MiB. | [optional] 
**host_written_to_virtual_percent** | **float, none_type** | Host written to virtual percent | [optional] 
**id** | **str, none_type** | UID of the snapshot. &#x60;Filter&#x60; | [optional] 
**initiators** | [**[PrimeraApplicationSetDetailsInitiators], none_type**](PrimeraApplicationSetDetailsInitiators.md) | Initiator details | [optional] 
**name** | **str, none_type** | A user friendly name to identify the storage system volume (resourceName). | [optional] 
**parent_id** | **int, none_type** | Parent Id | [optional] 
**phys_parent_id** | **int, none_type** | physical Parent Id | [optional] 
**physical_copy** | **bool, none_type** |  | [optional] 
**policy** | [**Policy**](Policy.md) |  | [optional] 
**prov_type** | **str, none_type** | Provisioning type | [optional] 
**raid** | **str, none_type** | Raid | [optional] 
**rcopy_status** | **str, none_type** | RemoteCopy Status | [optional] 
**read_only** | **bool, none_type** |  | [optional] 
**retention_time** | [**Calendar**](Calendar.md) |  | [optional] 
**ro_child_id** | **int, none_type** | RO child id | [optional] 
**rw_child_id** | **int, none_type** |  | [optional] 
**sectors_per_track** | **int, none_type** | Sector per Track | [optional] 
**shared_parent_id** | **int, none_type** | Shared Parent Id | [optional] 
**size_mi_b** | **float, none_type** | Size in MiB | [optional] 
**snapshot_alloc_limit** | **int, none_type** | Snapshot alloc limit | [optional] 
**snapshot_alloc_warning** | **int, none_type** | Snapshot alloc Warning | [optional] 
**snapshot_allocation_settings** | [**UserAllocationSettingsSingle**](UserAllocationSettingsSingle.md) |  | [optional] 
**snapshot_cpg_id** | **int, none_type** | Snapshot CPG Id | [optional] 
**snapshot_cpg_name** | **str, none_type** | Snapshot CPG name | [optional] 
**snapshot_id** | **int, none_type** | Numeric ID of the resource | [optional] 
**snapshot_space** | [**Space**](Space.md) |  | [optional] 
**snapshot_tdvv_size** | [**SnapshotTdvvsize**](SnapshotTdvvsize.md) |  | [optional] 
**snapshot_type** | **str, none_type** |  | [optional] 
**snapshot_used_to_virtual_percent** | **float, none_type** | Snapshot used to virtual percent | [optional] 
**space_calculation_time** | [**Calendar**](Calendar.md) |  | [optional] 
**started** | **bool, none_type** |  | [optional] 
**state** | [**STATE**](STATE.md) |  | [optional] 
**system_id** | **str, none_type** | SystemUid/serialNumber of the array. | [optional] 
**thin_provisioned** | **bool, none_type** | Thin provisioning details | [optional] 
**total_raw_reserved_mi_b** | **float, none_type** | Total Raw Reserved Space in MiB | [optional] 
**total_reserved_mi_b** | **float, none_type** | Description | [optional] 
**total_space_mi_b** | **float, none_type** | Total Space in MiB | [optional] 
**type** | **str, none_type** | type | [optional] 
**unref_space_freed_time** | [**Calendar**](Calendar.md) |  | [optional] 
**used_capacity** | **float, none_type** | Used volume capacity. | [optional] 
**used_size_mi_b** | **float, none_type** | Used Size in MiB | [optional] 
**user_alloc_limit** | **int, none_type** | User alloc limit | [optional] 
**user_alloc_warning** | **int, none_type** | User alloc space limit warning | [optional] 
**user_allocation_settings** | [**UserAllocationSettingsSingle**](UserAllocationSettingsSingle.md) |  | [optional] 
**user_cpg_id** | **int, none_type** | User CPG Id | [optional] 
**user_cpg_name** | **str, none_type** | User CPG Name | [optional] 
**user_reserved_to_virtual_percent** | **float, none_type** | User reseved to virtual percent | [optional] 
**user_space** | [**Space**](Space.md) |  | [optional] 
**user_used_to_virtual_percent** | **float, none_type** | User used to virtual percent | [optional] 
**vlun_sector_size** | **int, none_type** | VLUN sector size | [optional] 
**wwn** | **str, none_type** | Volume wwn. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

