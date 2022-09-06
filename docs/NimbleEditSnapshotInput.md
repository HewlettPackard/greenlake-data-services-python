# NimbleEditSnapshotInput

Edit Nimble snapshot input. Edit a snapshot with the given attributes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Identifier for the snapshot. A 42 digit hexadecimal number. | 
**app_uuid** | **str, none_type** | Application identifier of snapshots. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. Defaults to empty string. | [optional] 
**description** | **str, none_type** | Text description of snapshot. String of up to 255 printable ASCII characters. Defaults to the empty string. | [optional] 
**metadata** | [**[KeyValue], none_type**](KeyValue.md) | Key-value pairs that augment a volume&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. Defaults to an empty array. | [optional] 
**online** | **bool, none_type** | Online state for a snapshot means it could be mounted for data restore. Defaults to &#39;false&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


