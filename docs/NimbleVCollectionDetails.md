# NimbleVCollectionDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_hostname** | **str** | Generic backup agent hostname. Custom port number can be specified with agent hostname using \\\\\&quot;:\\\\\&quot;. | [optional] 
**app_sync** | **str** | Application Synchronization. Possible values: &#39;vss&#39;, &#39;vmware&#39;, &#39;none&#39;, &#39;generic&#39;. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**cache_pinned_volume_list** | [**list[NimbleVolumeSummary]**](NimbleVolumeSummary.md) | List of cache pinned volumes associated with volume collection. | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int** | Application server hostname. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**description** | **str** | Text descrption of volume collection. | [optional] 
**full_name** | **str** | Fully qualified name of volume collection. | [optional] 
**generation** | **int** | generation | [optional] 
**handover_replication_partner** | **str** | Replication partner to which ownership is being transferred as part of handover operation. | [optional] 
**is_handing_over** | **bool** | Indicates whether a handover operation is in progress on this volume collection. | [optional] 
**is_standalone_volcoll** | **bool** | Last snapshot collection on this volume collection. | [optional] 
**lag_time** | **int** | Replication lag time for volume collection. | [optional] 
**last_replicated_snapcoll** | [**list[NimbleSnapcollSummary]**](NimbleSnapcollSummary.md) | Last replicated snapshot collection on this volume collection. | [optional] 
**last_snapcoll** | [**list[NimbleSnapcollSummary]**](NimbleSnapcollSummary.md) | Last snapshot collection on this volume collection. | [optional] 
**metadata** | [**list[NimbleNsKeyValue]**](NimbleNsKeyValue.md) | Key-value pairs that augment a volume collection&#39;s attributes. | [optional] 
**pol_owner_name** | **str** | PolOwnerName - Owner group. | [optional] 
**protection_type** | **str** | Specifies if volume collection is protected with schedules. If protected, indicated whether replication is setup. | [optional] 
**repl_bytes_transferred** | **int** | Total size of volumes replicated for this volume collection. | [optional] 
**repl_priority** | **str** | Replication priority for the volume collection with the following choices: {normal | high}.  Possible values: &#39;normal&#39;, &#39;high&#39;. | [optional] 
**replication_partner** | **list[str]** | List of replication partners associated with the volume collection. | [optional] 
**resource_uri** | **str** |  | [optional] 
**schedule_list** | [**list[NimbleNsSchedule]**](NimbleNsSchedule.md) | List of schedules for this volume collection. | [optional] 
**search_name** | **str** | Name of volume collection used for object search. | [optional] 
**snapcoll_count** | **int** | Count of snapshot collections associated with volume collection. | [optional] 
**srep_last_sync** | **int** | Time when a synchronously replicated volume collection was last synchronized. | [optional] 
**srep_resync_percent** | **int** | Percentage of the resync progress for a synchronously replicated volume collection. | [optional] 
**total_repl_bytes** | **int** | Total size of volumes to be replicated for this volume collection. | [optional] 
**type** | **str** | type | [optional] 
**vcenter_hostname** | **str** | VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\\\\&quot;:\\\\\&quot;. | [optional] 
**vcenter_username** | **str** | Application VMware vCenter username. | [optional] 
**volume_count** | **int** | Count of volumes associated with the volume collection. | [optional] 
**volume_list** | [**list[NimbleVolumeSummary]**](NimbleVolumeSummary.md) | List of volumes associated with the volume collection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


