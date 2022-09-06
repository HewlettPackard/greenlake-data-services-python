# CreateRemoteCopyLinkInput

Request body for creating remote copy links

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | IP Address or WWN of Remote Copy target for this link, depending on the link type IP or FC | 
**port_pos** | [**CreateRemoteCopyLinkInputPortPos**](CreateRemoteCopyLinkInputPortPos.md) |  | 
**target_name** | **str** | Remote Copy target with which the link is affiliated | 
**type** | **int** | Remote Copy link type. 1 for IP and 2 for FC | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


