# EditSystemParameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alarms_enabled** | **bool** | Enable or disable alarm feature. | [optional] 
**default_volume_limit** | **int** | Default limit for a volume space usage as a percentage of volume size. Volume will be taken offline/made non-writable on exceeding its limit. Percentage as integer from 0 to 100. | [optional] 
**fc_enabled** | **bool** | Enable or disable FC.This flag can be modified only on the physical array which supports FC. | [optional] 
**group_target_enabled** | **bool** | Enable or disable group target. | [optional] 
**iscsi_enabled** | **bool** | Enable or disable iSCSI. | [optional] 
**repl_throttle_list** | [**list[EditThrottle]**](EditThrottle.md) | All the replication bandwidth limits on the system. All the throttles for the partner. | [optional] 
**vss_validation_timeout** | **int** | The amount of time in seconds to validate Microsoft VSS application synchronization before timing out. VSS validation timeout in second, valid range is from 1 to 3600 (60 minutes). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


