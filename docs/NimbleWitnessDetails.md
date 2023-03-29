# NimbleWitnessDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str, none_type** | Request URI for detailed witness objects | [optional] 
**host** | **str, none_type** | Hostname or ip addresses of witness. Comma separated strings of up to 63 characters of hostname and/or ip addresses. Total length cannot exceed 255 characters. | [optional] 
**id** | **str, none_type** | Identifier for the witness configuration. A 42 digit hexadecimal number. | [optional] 
**port** | **int, none_type** | Port of witness. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**username** | **str, none_type** | Username of witness. This has to be a non-root that can login to the witness host. String of up to 32 characters, beginning with a letter or number or period (.) or an underscore (_). It can include underscore (_), dash (-), period (.) and end with doller ($) sign. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**auto_switchover_messages** | [**[NimbleErrorWithArguments], none_type**](NimbleErrorWithArguments.md) | List of validation messages for automatic switchover of Group Management. This will be empty when there are no conflicts found. List of error codes with details. | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**type** | **str, none_type** | type | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


