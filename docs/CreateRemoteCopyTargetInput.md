# CreateRemoteCopyTargetInput

Request body for creating remote copy targets

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the remote copy target | 
**port_pos_and_link** | [**[PortPosAndLinkInput]**](PortPosAndLinkInput.md) | Specifies all locations (portPos) of the local system, and all links(IP or WWN) of the remote system | 
**type** | **int** | Specifies the link protocol. Do not use UNKNOWN as a linkType enumeration value when creating a Remote Copy target. 1 for IP Target Type, 2 for FC Target Type | 
**disabled** | **bool, none_type** | Enable (true) or disable (false) the creation of the target in disabled mode | [optional] 
**node_wwn** | **str, none_type** | WWN of the node on the target system for FC Link type. Ignored if specified for IP type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


