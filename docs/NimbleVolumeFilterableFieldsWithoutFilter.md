# NimbleVolumeFilterableFieldsWithoutFilter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_snap_id** | **str** | Base snapshot ID. This attribute is required together with name and clone when cloning a volume with the create operation. A 42 digit hexadecimal number. | [optional] 
**base_snap_name** | **str** | Name of base snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints. | [optional] 
**clone** | **bool** | Whether this volume is a clone. Use this attribute in combination with name and base_snap_id to create a clone by setting clone &#x3D; true. | [optional] 
**dest_pool_id** | **str** | ID of the destination pool where the volume is moving to. A 42 digit hexadecimal number. | [optional] 
**dest_pool_name** | **str** | Name of the destination pool where the volume is moving to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**folder_id** | **str** | ID of the folder holding this volume. An optional NsObjectID. A 42 digit hexadecimal number or the empty string. | [optional] 
**folder_name** | **str** | Name of the folder holding this volume. It can be empty. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**id** | **str** | Identifier for the volume. A 42 digit hexadecimal number. | [optional] 
**name** | **str** | Name of the volume. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. | [optional] 
**online** | **bool** | Online state of volume, available for host initiators to establish connections. | [optional] 
**owned_by_group** | **str** | Name of group that currently owns the volume. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**owned_by_group_id** | **str** | ID of group that currently owns the volume. A 42 digit hexadecimal number. | [optional] 
**parent_vol_id** | **str** | Parent volume ID. A 42 digit hexadecimal number. | [optional] 
**parent_vol_name** | **str** | Name of parent volume. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints. | [optional] 
**perfpolicy_id** | **str** | Identifier of the performance policy. After creating a volume, performance policy for the volume can only be changed to another performance policy with same block size. A 42 digit hexadecimal number. | [optional] 
**perfpolicy_name** | **str** | Name of performance policy. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**pool_id** | **str** | Identifier associated with the pool in the storage pool table. A 42 digit hexadecimal number. | [optional] 
**pool_name** | **str** | Name of the pool where the volume resides. Volume data will be distributed across arrays over which specified pool is defined. If pool option is not specified, volume is assigned to the default pool. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**read_only** | **bool** | Volume is read-only. | [optional] 
**replication_role** | **str** | Replication role that this volume performs. Possible values: &#39;periodic_snapshot_downstream&#39;, &#39;synchronous_upstream&#39;, &#39;synchronous_downstream&#39;, &#39;no_replication&#39;, &#39;periodic_snapshot_upstream&#39;. | [optional] 
**secondary_serial_number** | **str** | Secondary identifier associated with the volume for the SCSI protocol. | [optional] 
**serial_number** | **str** | Identifier associated with the volume for the SCSI protocol. A 32 digit hexadecimal number. | [optional] 
**size** | **int** | Volume size in megabytes. Size is required for creating a volume but not for cloning an existing volume. | [optional] 
**target_name** | **str** | The iSCSI Qualified Name (IQN) or the Fibre Channel World Wide Node Name (WWNN) of the target volume. The iSCSI Qualified Name (IQN) or the Fibre Channel World Wide Node Name (WWNN) of the target. | [optional] 
**volcoll_id** | **str** | ID of volume collection of which this volume is a member. Use this attribute in update operation to associate or dissociate volumes with or from volume collections. When associating, set this attribute to the ID of the volume collection. When dissociating, set this attribute to empty string. An optional NsObjectID. A 42 digit hexadecimal number or the empty string. | [optional] 
**volcoll_name** | **str** | Name of volume collection of which this volume is a member. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


