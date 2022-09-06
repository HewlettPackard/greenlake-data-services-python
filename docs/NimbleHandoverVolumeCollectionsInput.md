# NimbleHandoverVolumeCollectionsInput

Perform handover action on a volume collection input.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replication_partner_id** | **str** | Replication partner ID of the new owner. A 42 digit hexadecimal number. | 
**invoke_on_upstream_partner** | **bool, none_type** | Invoke handover request on upstream partner. Default: &#39;false&#39;. This operation is not supported for synchronous replication volume vollections. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**no_reverse** | **bool, none_type** | Do not automatically reverse direction of replication. Using this argument will prevent the new owner from automatically replicating the volume collection to this node when the handover completes. The default behavior is to enable replication back to this node. Default: &#39;false&#39;. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**override_upstream_down** | **bool, none_type** | Allow the handover request to proceed even if upstream array is down. The default behavior is to return an error when upstream is down. This option is applicable for synchronous replication only. Default: &#39;false&#39;. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


