# EditThrottle

A single throttle for the partner.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **str, none_type** | Comma separated list of days of the week or &#39;all&#39;. | [optional] 
**description** | **str, none_type** | Description of the throttle. | [optional] 
**thr_at_time** | **int, none_type** | Start time for the throttle. | [optional] 
**thr_bandwidth** | **int, none_type** | Bandwidth for the throttle in megabits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This attribute is superseded by thr_bandwidth_limit_kbps. Use either thr_bandwidth or thr_bandwidth_kbps to set throttle bandwidth. | [optional] 
**thr_bandwidth_kbps** | **int, none_type** | Bandwidth for the throttle in kilobits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This atttibute is superseded by thr_bandwidth_limit_kbps. Use either thr_bandwidth or thr_bandwidth_kbps to set throttle bandwidth. | [optional] 
**thr_bandwidth_limit_kbps** | **int, none_type** | Bandwidth for the throttle in kilobits per second or -1 to indicate that there is no limit. | [optional] 
**thr_until_time** | **int, none_type** | End time for the throttle. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


