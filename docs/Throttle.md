# Throttle

A single throttle for the partner.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time** | **int, none_type** | Creation time of the throttle. | [optional] 
**days** | **str, none_type** | List of days that the throttle operates. | [optional] 
**description** | **str, none_type** | Description of the throttle. | [optional] 
**id** | **str, none_type** | Id of the throttle. | [optional] 
**last_modified** | **int, none_type** | Last modification time of the throttle. | [optional] 
**name** | **str, none_type** | Name of the throttle. | [optional] 
**thr_at_time** | **int, none_type** | Start time set for the throttle. | [optional] 
**thr_bandwidth** | **int, none_type** | Bandwidth set for the throttle in megabits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This attribute is superseded by thr_bandwidth_limit_kbps. | [optional] 
**thr_bandwidth_kbps** | **int, none_type** | Bandwidth set for the throttle in kilobits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This atttibute is superseded by thr_bandwidth_limit_kbps. | [optional] 
**thr_bandwidth_limit_kbps** | **int, none_type** | Bandwidth set for the throttle in kilobits per second or -1 to indicate that there is no limit. | [optional] 
**thr_day_mask** | **int, none_type** | Mask for days that the throttle operates. | [optional] 
**thr_partner_id** | **str, none_type** | ID of the partner object. | [optional] 
**thr_until_time** | **int, none_type** | End time set for the throttle. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


