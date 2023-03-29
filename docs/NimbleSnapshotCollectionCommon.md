# NimbleSnapshotCollectionCommon


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_writes** | **bool, none_type** | Allow applications to write to created snapshot(s). Mandatory and must be set to &#39;true&#39; for VSS application synchronized snapshots. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int, none_type** | Time when this snapshot collection was created. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**description** | **str, none_type** | Text description of snapshot collection. String of up to 255 printable ASCII characters. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**is_complete** | **bool, none_type** | Is complete. | [optional] 
**is_external_trigger** | **bool, none_type** | Is externally triggered. | [optional] 
**is_manual** | **bool, none_type** | Is manual. | [optional] 
**is_manually_managed** | **bool, none_type** | Is snapshot collection manually managed, i.e., snapshot collection is manually or third party created or created by system at the time of volume restore or resize. | [optional] 
**is_replica** | **bool, none_type** | Snapshot collection is a replica from upstream replication partner. | [optional] 
**is_unmanaged** | **bool, none_type** | Indicates whether a snapshot collection is unmanaged. This is based on the state of individual snapshots. | [optional] 
**last_modified** | **int, none_type** | Time when this snapshot collection was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**metadata** | [**[KeyValue], none_type**](KeyValue.md) | Key-value pairs that augment a snapshot collection&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. | [optional] 
**origin_name** | **str, none_type** | Origination group name/ID. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**peer_snapcoll_id** | **str, none_type** | ID of the peer snapshot collection created by synchronous replication. Field will be null if no peer snapshot_collection was created by synchronous replication. A 42 digit hexadecimal number. | [optional] 
**replicate_to** | **str, none_type** | Specifies the partner name that the snapshots in this snapshot collection are replicated to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**snapshots_list** | [**[NimbleSnapCollSnapshot], none_type**](NimbleSnapCollSnapshot.md) | Snapshot list for a SnapshotCollection | [optional] 
**type** | **str, none_type** | type | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


