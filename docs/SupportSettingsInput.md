# SupportSettingsInput

Edit Support settings for the system

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connect_to_hpe** | **str** | Enable remote support by allowing sending of files from device to HPE. Allowed values: enabled or disabled. It is mandatory. | 
**rap_forwarding** | **str** | Enable/Disable RAP forwarding. Allowed values: enabled or disabled. It is mandatory. | 
**remote_access** | **str** | Allow HPE Support to access the device remotely. Allowed values: ENABLE_ROOT or DISABLE or ENABLE_NONROOT. It is mandatory. | 
**rts_enabled** | **str** | Enable/Disable Real time data scrubbing. Allowed values: enabled or disabled. It is mandatory. | 
**device_id** | **str** | Id of the array. User can get Id info from GET response. It is mandatory. | [optional] 
**enterprise_server_url** | **str, none_type** | Callhome collection server URL | [optional] 
**mini_insplore_enabled** | **str, none_type** | Enables/Disable scheduled Mini-Insplore collection. Allowed values: enabled or disabled. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


