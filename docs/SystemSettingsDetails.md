# SystemSettingsDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**[AssociatedLinksInner], none_type**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**auth_mode** | **str, none_type** | Password Authentication Mode | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object  | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**installationsites** | [**SystemSettingsDetailsInstallationsites**](SystemSettingsDetailsInstallationsites.md) |  | [optional] 
**is_fips_enabled** | **bool, none_type** | Apply FIPS Standard | [optional] 
**name** | **str, none_type** | system name | [optional] 
**ntp_server** | **str, none_type** | ntp server | [optional] 
**remote_syslog_settings** | [**SystemSettingsDetailsRemoteSyslogSettings**](SystemSettingsDetailsRemoteSyslogSettings.md) |  | [optional] 
**srinfo** | [**SystemSettingsDetailsSrinfo**](SystemSettingsDetailsSrinfo.md) |  | [optional] 
**supportcontact** | [**ContactsDetails**](ContactsDetails.md) |  | [optional] 
**system_date** | **int, none_type** | system date time | [optional] 
**system_id** | **str, none_type** | SystemId/serialNumber of the array. | [optional] 
**system_parameters** | [**SystemSettingsDetailsSystemParameters**](SystemSettingsDetailsSystemParameters.md) |  | [optional] 
**timezone** | **str, none_type** | system time zone | [optional] 
**type** | **str** | The type of resource. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


