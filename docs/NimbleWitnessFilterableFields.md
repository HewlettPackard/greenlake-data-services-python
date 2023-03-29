# NimbleWitnessFilterableFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **str, none_type** | Hostname or ip addresses of witness. Comma separated strings of up to 63 characters of hostname and/or ip addresses. Total length cannot exceed 255 characters. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str, none_type** | Identifier for the witness configuration. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**port** | **int, none_type** | Port of witness. Positive integer value up to 65535 representing TCP/IP port. &#x60;Filter, Sort&#x60; | [optional] 
**username** | **str, none_type** | Username of witness. This has to be a non-root that can login to the witness host. String of up to 32 characters, beginning with a letter or number or period (.) or an underscore (_). It can include underscore (_), dash (-), period (.) and end with dollar ($) sign. &#x60;Filter, Sort&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


