# NimbleNsDiskSetAttr

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ave_mb_ps** | **int** | Average evacuation speed in MB/s; valid only when sw_state is evacuating, ie. evacuation is underway. | [optional] 
**ave_segment_ps** | **int** | Average evacuation speed in segments/sec; valid only when sw_state is evacuating, ie. evacuation is underway. | [optional] 
**ave_ttc** | **int** | Average time to complete in seconds; valid only when sw_state is evacuating, ie. evacuation is underway. | [optional] 
**driveset** | **int** | Driveset index for this shelf. | [optional] 
**is_capacity_valid** | **bool** | Is the capacity fields in this data struct valid. | [optional] 
**is_flash_shelf** | **bool** | Is this a all-flash-shelf. | [optional] 
**pause_state** | **int** | State of evacuation, paused or in-progress; valid only when sw_state is evacuating, ie. evacuation is underway. | [optional] 
**pct_completion** | **int** | Evacuation percent completion; valid only when sw_state is evacuating, ie. evacuation is underway. | [optional] 
**raw_cache_capacity** | **int** | Raw cache capacity for this shelf. | [optional] 
**raw_capacity** | **int** | Hdd raw capacity for this shelf. | [optional] 
**sw_state** | **str** | Software state. Possible values:&#39;available&#39;, &#39;online&#39;, &#39;foreign&#39;, &#39;unknown&#39;. | [optional] 
**usable_cache_capacity** | **int** | Estimated usable cache capacity for this shelf. | [optional] 
**usable_capacity** | **int** | Estimated usable capacity for this shelf. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


