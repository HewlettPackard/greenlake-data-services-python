# Throttle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creation_time** | **int** | Creation time of the throttle. | [optional] 
**days** | **str** | List of days that the throttle operates. | [optional] 
**description** | **str** | Description of the throttle. | [optional] 
**id** | **str** | Id of the throttle. | [optional] 
**last_modified** | **int** | Last modification time of the throttle. | [optional] 
**name** | **str** | Name of the throttle. | [optional] 
**thr_at_time** | **int** | Start time set for the throttle. | [optional] 
**thr_bandwidth** | **int** | Bandwidth set for the throttle in megabits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This attribute is superseded by thr_bandwidth_limit_kbps. | [optional] 
**thr_bandwidth_kbps** | **int** | Bandwidth set for the throttle in kilobits per second or as the largest possible 64-bit signed integer (9223372036854775807) to indicate that there is no limit. This atttibute is superseded by thr_bandwidth_limit_kbps. | [optional] 
**thr_bandwidth_limit_kbps** | **int** | Bandwidth set for the throttle in kilobits per second or -1 to indicate that there is no limit. | [optional] 
**thr_day_mask** | **int** | Mask for days that the throttle operates. | [optional] 
**thr_partner_id** | **str** | ID of the partner object. | [optional] 
**thr_until_time** | **int** | End time set for the throttle. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


