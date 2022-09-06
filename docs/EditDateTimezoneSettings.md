# EditDateTimezoneSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **int, none_type** | Unix epoch time local to the group. Seconds since last epoch i.e. 00:00 January 1, 1970. Setting this along with ntp_server causes ntp_server to be reset. | [optional] 
**ntp_server** | **str, none_type** | Either IP address or hostname of the NTP server for this group. | [optional] 
**timezone** | **str, none_type** | Timezone in which this group is located. Plain string. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


