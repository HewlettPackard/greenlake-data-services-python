# EditSystemParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alarms_enabled** | **bool, none_type** | Enable or disable alarm feature. | [optional] 
**default_volume_limit** | **int, none_type** | Default limit for a volume space usage as a percentage of volume size. Volume will be taken offline/made non-writable on exceeding its limit. Percentage as integer from 0 to 100. | [optional] 
**fc_enabled** | **bool, none_type** | Enable or disable FC.This flag can be modified only on the physical array which supports FC. | [optional] 
**group_target_enabled** | **bool, none_type** | Enable or disable group target. | [optional] 
**iscsi_enabled** | **bool, none_type** | Enable or disable iSCSI. | [optional] 
**repl_throttle_list** | [**[EditThrottle], none_type**](EditThrottle.md) | All the replication bandwidth limits on the system. All the throttles for the partner. | [optional] 
**vss_validation_timeout** | **int, none_type** | The amount of time in seconds to validate Microsoft VSS application synchronization before timing out. VSS validation timeout in second, valid range is from 1 to 3600 (60 minutes). | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


