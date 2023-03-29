# CreateCloneSnapshotInput

Request body for creating physical copy of a snapshot.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_volume** | **str** | Name of the destination volume. | 
**auto_lun** | **bool, none_type** | Secify to use auto lun number. | [optional] 
**destination_cpg** | **str, none_type** | Name of the User CPG | [optional] 
**host_group_id** | **str, none_type** | Unique identifier of host group. | [optional] 
**lun** | **int, none_type** | LUN of volume. | [optional] 
**priority** | **str, none_type** | Priority of the task for clone of a snashot. Defualts to MEDIUM. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


