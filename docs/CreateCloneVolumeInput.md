# CreateCloneVolumeInput

Request body for creating physical copy of a volume.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_volume** | **str** | Name of the destination volume. | 
**offline_clone** | [**[OfflineClone], none_type**](OfflineClone.md) | Offline clone of a volume. | [optional] 
**online** | **bool, none_type** | Create an online or offline clone of a volume. | [optional] 
**online_clone** | [**[OnlineClone], none_type**](OnlineClone.md) | Online clone of a volume. | [optional] 
**priority** | **str, none_type** | Priority of the task for clone volume. Defualts to MEDIUM. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


