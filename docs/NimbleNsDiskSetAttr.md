# NimbleNsDiskSetAttr


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ave_mb_ps** | **int, none_type** | Average evacuation speed in MB/s; valid only when sw_state is evacuating, ie. evacuation is underway. | [optional] 
**ave_segment_ps** | **int, none_type** | Average evacuation speed in segments/sec; valid only when sw_state is evacuating, ie. evacuation is underway. | [optional] 
**ave_ttc** | **int, none_type** | Average time to complete in seconds; valid only when sw_state is evacuating, ie. evacuation is underway. | [optional] 
**driveset** | **int, none_type** | Driveset index for this shelf. | [optional] 
**is_capacity_valid** | **bool, none_type** | Is the capacity fields in this data struct valid. | [optional] 
**is_flash_shelf** | **bool, none_type** | Is this a all-flash-shelf. | [optional] 
**pause_state** | **int, none_type** | State of evacuation, paused or in-progress; valid only when sw_state is evacuating, ie. evacuation is underway. | [optional] 
**pct_completion** | **int, none_type** | Evacuation percent completion; valid only when sw_state is evacuating, ie. evacuation is underway. | [optional] 
**raw_cache_capacity** | **int, none_type** | Raw cache capacity for this shelf. | [optional] 
**raw_capacity** | **int, none_type** | Hdd raw capacity for this shelf. | [optional] 
**sw_state** | **str, none_type** | Software state. Possible values:&#39;available&#39;, &#39;online&#39;, &#39;foreign&#39;, &#39;unknown&#39;. | [optional] 
**usable_cache_capacity** | **int, none_type** | Estimated usable cache capacity for this shelf. | [optional] 
**usable_capacity** | **int, none_type** | Estimated usable capacity for this shelf. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


