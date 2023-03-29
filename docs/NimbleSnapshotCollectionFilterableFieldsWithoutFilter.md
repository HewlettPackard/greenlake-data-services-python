# NimbleSnapshotCollectionFilterableFieldsWithoutFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Identifier for the snapshot collection. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str, none_type** | Name of snapshot. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. &#x60;Filter, Sort&#x60; | [optional] 
**online_status** | **str, none_type** | Online status of snapshot collection. This is based on the online status of the individual snapshots. Online status based on that of the constituent entities. Possible values: &#39;online&#39;, &#39;offline&#39; or &#39;partial&#39;. | [optional] 
**schedule_id** | **str, none_type** | Identifier of protection schedule. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**srep_owner_id** | **str, none_type** | ID of the partner where snapshots for this snapshot collection reside which were created by synchronous replication. Field will be null if no peer snapshot_collection was created by synchronous replication. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**volcoll_id** | **str, none_type** | Parent volume collection ID. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


