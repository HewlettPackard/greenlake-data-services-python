# CreateCloneVolumeInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_volume** | **str** | Name of the destination volume. | 
**offline_clone** | [**list[OfflineClone]**](OfflineClone.md) | Offline clone of a volume. | [optional] 
**online** | **bool** | Create an online or offline clone of a volume. | [optional] 
**online_clone** | [**list[OnlineClone]**](OnlineClone.md) | Online clone of a volume. | [optional] 
**priority** | **str** | Priority of the task for clone volume. Defualts to MEDIUM. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


