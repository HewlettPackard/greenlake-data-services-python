# CommonFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**description** | **str** | Text description of application server. String of up to 255 printable ASCII characters. Defaults to the empty string. | [optional] 
**generation** | **int** | generation | [optional] 
**metadata** | [**list[AppKeyValue]**](AppKeyValue.md) | Key-value pairs that augment an application server&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. Defaults to an empty array. | [optional] 
**port** | **int** | Application server port number. Positive integer value up to 65535 representing TCP/IP port. Defaults to 65536. | [optional] 
**resource_uri** | **str** |  | [optional] 
**type** | **str** | type | [optional] 
**username** | **str** | Application server username. String of up to 255 printable ASCII characters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


