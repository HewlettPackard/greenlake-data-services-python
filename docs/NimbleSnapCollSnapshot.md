# NimbleSnapCollSnapshot


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_time** | **int, none_type** | Unix timestamp indicating that the snapshot is considered expired by Snapshot Time-to-live(TTL). A value of 0 indicates that snapshot never expires. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**id** | **str, none_type** | Identifier for the snapshot. A 42 digit hexadecimal number. | [optional] 
**name** | **str, none_type** | Name of snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. | [optional] 
**schedule_id** | **str, none_type** | Identifier of protection schedule. A 42 digit hexadecimal number. | [optional] 
**schedule_name** | **str, none_type** | Name of protection schedule. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**snap_collection_id** | **str, none_type** | Identifier of snapshot collection. A 42 digit hexadecimal number. | [optional] 
**snap_collection_name** | **str, none_type** | Name of snapshot collection. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints. | [optional] 
**vol_id** | **str, none_type** | Parent volume ID. A 42 digit hexadecimal number. | [optional] 
**vol_name** | **str, none_type** | Name of the parent volume in which the snapshot belongs to. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


