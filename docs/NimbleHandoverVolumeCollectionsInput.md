# NimbleHandoverVolumeCollectionsInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoke_on_upstream_partner** | **bool** | Invoke handover request on upstream partner. Default: &#39;false&#39;. This operation is not supported for synchronous replication volume vollections. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**no_reverse** | **bool** | Do not automatically reverse direction of replication. Using this argument will prevent the new owner from automatically replicating the volume collection to this node when the handover completes. The default behavior is to enable replication back to this node. Default: &#39;false&#39;. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**override_upstream_down** | **bool** | Allow the handover request to proceed even if upstream array is down. The default behavior is to return an error when upstream is down. This option is applicable for synchronous replication only. Default: &#39;false&#39;. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**replication_partner_id** | **str** | Replication partner ID of the new owner. A 42 digit hexadecimal number. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


