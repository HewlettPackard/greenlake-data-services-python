# CreateApplicationServer

Create Nimble application server input.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | Application server hostname. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; Hypen and  colon are allowed after the first and before the last character. | 
**name** | **str** | Name of the volume. String of up to 64 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. | 
**description** | **str, none_type** | Text description of application server. String of up to 255 printable ASCII characters. Defaults to the empty string. | [optional] 
**metadata** | [**[AppKeyValue], none_type**](AppKeyValue.md) | Key-value pairs that augment an application server&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. Defaults to an empty array. | [optional] 
**port** | **int, none_type** | Application server port number. Positive integer value up to 65535 representing TCP/IP port. Defaults to 65536. | [optional] 
**server_type** | **str, none_type** | Application server type. Defaults to &#39;vmware&#39;. Possible values are &#39;vss&#39; and &#39;vmware&#39;. | [optional] 
**username** | **str, none_type** | Application server username. String of up to 255 printable ASCII characters. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


