# Vasa

Vasa service details for a device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cert_mgmt** | [**CertMgmt**](CertMgmt.md) |  | [optional] 
**cert_subject** | **str, none_type** | Certificate subject of the VASA Provider | [optional] 
**cert_thumbprint** | **str, none_type** | Certificate thumbprint of the VASA Provider | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**enabled** | **bool, none_type** | Indicates if the service status is enabled or not | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**https_enabled** | **bool, none_type** | Indicates if the vasa https state is enabled or not | [optional] 
**https_port** | **int, none_type** | Vasa https port number | [optional] 
**id** | **str, none_type** | Unique Identifier of the resource | [optional] 
**mem_usage_mi_b** | **int, none_type** | Memory usage of the VASA provider | [optional] 
**more_uris** | [**[VasaUriInfo], none_type**](VasaUriInfo.md) | List of VASA Service URLs  | [optional] 
**server_name** | **str, none_type** | Name of the vasa server | [optional] 
**system_id** | **str, none_type** | SystemId of the storage system | [optional] 
**system_wwn** | **str, none_type** | WWN of the array | [optional] 
**type** | **str** | The type of resource. | [optional] 
**version** | **str, none_type** | Version of the VASA provider | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


