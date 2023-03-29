# EditSyslogdSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**syslogd_enabled** | **bool, none_type** | Enable or disable syslogd in system | [optional] 
**syslogd_port** | **int, none_type** | Port number for syslogd server. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**syslogd_server** | **str, none_type** | Hostname of the syslogd server. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 
**syslogd_servers** | [**[NimbleSyslogdServerInfo], none_type**](NimbleSyslogdServerInfo.md) | syslogd server info. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


