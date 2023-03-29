# CreateHostGroupInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Name of the host group | 
**user_created** | **bool, none_type** | Idicates whether user created host or discovered host | 
**comment** | **str, none_type** | Comment | [optional] 
**host_ids** | **[str, none_type], none_type** | List of host ids of existing hosts | [optional] 
**hosts_to_create** | [**[CreateHostInput], none_type**](CreateHostInput.md) | List of hosts to be created and added to this hostGroup | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


