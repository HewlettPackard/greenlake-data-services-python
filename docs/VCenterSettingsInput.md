# VCenterSettingsInput

Request body to add vCenter Settings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inetaddress** | **str** | Host name or IP address of vCenter server | 
**name** | **str** | Name of the vCenter setting | 
**password** | **str** | Password to login to the vCenter server | 
**port** | **int** | Port number of the vCenter server. | 
**username** | **str** | Username to login to the vCenter server | 
**cert_chain_pem** | **str, none_type** | Certificate chain of the VCenter server as PEM data | [optional] 
**description** | **str, none_type** | Description of the vCenter setting | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


