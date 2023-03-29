# NimbleSnapshotFilterableFieldsWithoutFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Identifier for the snapshot. A 42 digit hexadecimal number. | [optional] 
**name** | **str, none_type** | Name of snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. | [optional] 
**online** | **bool, none_type** | Online state for a snapshot means it could be mounted for data restore. | [optional] 
**pool_name** | **str, none_type** | Name of the pool in which the parent volume belongs to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**replication_status** | **str, none_type** | Replication status. Possible values: &#39;complete&#39;, &#39;in_progress&#39;, &#39;pending&#39;, &#39;fail&#39;. | [optional] 
**schedule_id** | **str, none_type** | Identifier of protection schedule. A 42 digit hexadecimal number. | [optional] 
**schedule_name** | **str, none_type** | Name of protection schedule. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**serial_number** | **str, none_type** | Identifier for the SCSI protocol. A 32 digit hexadecimal number. | [optional] 
**size** | **int, none_type** | Size of volume at time of snapshot (in bytes). | [optional] 
**snap_collection_id** | **str, none_type** | Identifier of snapshot collection. A 42 digit hexadecimal number. | [optional] 
**snap_collection_name** | **str, none_type** | Name of snapshot collection. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints. | [optional] 
**target_name** | **str, none_type** | The iSCSI Qualified Name (IQN) or the Fibre Channel World Wide Node Name (WWNN) of the target snapshot. The iSCSI Qualified Name (IQN) or the Fibre Channel World Wide Node Name (WWNN) of the target. | [optional] 
**writable** | **bool, none_type** | Whether snapshot is writable or not. Mandatory and must be set to &#39;true&#39; for VSS application synchronized snapshots. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


