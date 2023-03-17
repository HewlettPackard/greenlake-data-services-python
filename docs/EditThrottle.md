# EditThrottle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **str** | Comma separated list of days of the week or &#39;all&#39;. | [optional] 
**description** | **str** | Description of the throttle. | [optional] 
**thr_at_time** | **int** | Start time for the throttle. | [optional] 
**thr_bandwidth** | **int** | Bandwidth for the throttle in megabits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This attribute is superseded by thr_bandwidth_limit_kbps. Use either thr_bandwidth or thr_bandwidth_kbps to set throttle bandwidth. | [optional] 
**thr_bandwidth_kbps** | **int** | Bandwidth for the throttle in kilobits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This atttibute is superseded by thr_bandwidth_limit_kbps. Use either thr_bandwidth or thr_bandwidth_kbps to set throttle bandwidth. | [optional] 
**thr_bandwidth_limit_kbps** | **int** | Bandwidth for the throttle in kilobits per second or -1 to indicate that there is no limit. | [optional] 
**thr_until_time** | **int** | End time for the throttle. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


