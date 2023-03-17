# SystemSettingsDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**list[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**auth_mode** | **str** | Password Authentication Mode | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object  | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**installationsites** | [**SystemSettingsDetailsInstallationsites**](SystemSettingsDetailsInstallationsites.md) |  | [optional] 
**is_fips_enabled** | **bool** | Apply FIPS Standard | [optional] 
**name** | **str** | system name | [optional] 
**ntp_server** | **str** | ntp server | [optional] 
**remote_syslog_settings** | **object** |  | [optional] 
**srinfo** | **object** |  | [optional] 
**supportcontact** | [**ContactsDetails**](ContactsDetails.md) |  | [optional] 
**system_date** | **int** | system date time | [optional] 
**system_id** | **str** | SystemId/serialNumber of the array. | [optional] 
**system_parameters** | **object** |  | [optional] 
**timezone** | **str** | system time zone | [optional] 
**type** | **str** | The type of resource. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


