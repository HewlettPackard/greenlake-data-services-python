# NimbleVolumeSnapAttr

Snapshot attributes for snapshots being created as part of snapshot collection creation. List of volumes with per snapshot attributes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_uuid** | **str, none_type** | Application identifier of snapshots. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. Defaults to empty string. | [optional] 
**metadata** | [**[KeyValue], none_type**](KeyValue.md) | Key-value pairs that augment a volume&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. Defaults to an empty array. | [optional] 
**vol_id** | **str, none_type** | Identifier of volume. A 42 digit hexadecimal number. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


