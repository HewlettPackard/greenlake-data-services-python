# NimbleVolumeCollectionListItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_cluster_name** | **str, none_type** | If the application is running within a Windows cluster environment, this is the cluster name. &#x60;Filter, Sort&#x60; | [optional] 
**app_id** | **str, none_type** | Application ID running on the server. Application ID can only be specified if application synchronization is \\\\\&quot;vss\\\\\&quot;. &#x60;Filter, Sort&#x60; Possible values: &#39;exchange_dag&#39;, &#39;sql2012&#39;, &#39;inval&#39;, &#39;sql2014&#39;, &#39;sql2005&#39;, &#39;sql2016&#39;, &#39;exchange&#39;, &#39;sql2017&#39;, &#39;sql2018&#39;, &#39;hyperv&#39;. | [optional] 
**app_server** | **str, none_type** | Application server hostname. &#x60;Filter, Sort&#x60; | [optional] 
**app_service_name** | **str, none_type** | If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str, none_type** | Identifier of the Volume-Collection. &#x60;Filter&#x60; | [optional] 
**name** | **str, none_type** | Name of volume collection. &#x60;Filter, Sort&#x60; | [optional] 
**prottmpl_id** | **str, none_type** | Identifier of the protection template whose attributes will be used to create this volume collection. This attribute is only used for input when creating a volume collection and is not outputed. &#x60;Filter, Sort&#x60; | [optional] 
**replication_type** | **str, none_type** | Type of replication configured for the volume collection. Possible values: &#39;synchronous&#39;, &#39;periodic_snapshot&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**synchronous_replication_state** | **str, none_type** | State of synchronous replication on the volume collection. Possible values: &#39;in_sync&#39;, &#39;not_applicable&#39;, &#39;out_of_sync&#39;, &#39;unknown&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**synchronous_replication_type** | **str, none_type** | Type of synchronous replication configured for the volume collection. Possible values: &#39;soft_available&#39;, &#39;not_applicable&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**agent_hostname** | **str, none_type** | Generic backup agent hostname. Custom port number can be specified with agent hostname using \\\\\&quot;:\\\\\&quot;. | [optional] 
**app_sync** | **str, none_type** | Application Synchronization. Possible values: &#39;vss&#39;, &#39;vmware&#39;, &#39;none&#39;, &#39;generic&#39;. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**cache_pinned_volume_list** | [**[NimbleVolumeSummary], none_type**](NimbleVolumeSummary.md) | List of cache pinned volumes associated with volume collection. | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int, none_type** | Application server hostname. | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**description** | **str, none_type** | Text descrption of volume collection. | [optional] 
**full_name** | **str, none_type** | Fully qualified name of volume collection. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**handover_replication_partner** | **str, none_type** | Replication partner to which ownership is being transferred as part of handover operation. | [optional] 
**is_handing_over** | **bool, none_type** | Indicates whether a handover operation is in progress on this volume collection. | [optional] 
**is_standalone_volcoll** | **bool, none_type** | Last snapshot collection on this volume collection. | [optional] 
**lag_time** | **int, none_type** | Replication lag time for volume collection. | [optional] 
**last_replicated_snapcoll** | [**[NimbleSnapcollSummary], none_type**](NimbleSnapcollSummary.md) | Last replicated snapshot collection on this volume collection. | [optional] 
**last_snapcoll** | [**[NimbleSnapcollSummary], none_type**](NimbleSnapcollSummary.md) | Last snapshot collection on this volume collection. | [optional] 
**metadata** | [**[NimbleNsKeyValue], none_type**](NimbleNsKeyValue.md) | Key-value pairs that augment a volume collection&#39;s attributes. | [optional] 
**pol_owner_name** | **str, none_type** | PolOwnerName - Owner group. | [optional] 
**protection_type** | **str, none_type** | Specifies if volume collection is protected with schedules. If protected, indicated whether replication is setup. | [optional] 
**repl_bytes_transferred** | **int, none_type** | Total size of volumes replicated for this volume collection. | [optional] 
**repl_priority** | **str, none_type** | Replication priority for the volume collection with the following choices: {normal | high}.  Possible values: &#39;normal&#39;, &#39;high&#39;. | [optional] 
**replication_partner** | **[str], none_type** | List of replication partners associated with the volume collection. | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**schedule_list** | [**[NimbleNsSchedule], none_type**](NimbleNsSchedule.md) | List of schedules for this volume collection. | [optional] 
**search_name** | **str, none_type** | Name of volume collection used for object search. | [optional] 
**snapcoll_count** | **int, none_type** | Count of snapshot collections associated with volume collection. | [optional] 
**srep_last_sync** | **int, none_type** | Time when a synchronously replicated volume collection was last synchronized. | [optional] 
**srep_resync_percent** | **int, none_type** | Percentage of the resync progress for a synchronously replicated volume collection. | [optional] 
**total_repl_bytes** | **int, none_type** | Total size of volumes to be replicated for this volume collection. | [optional] 
**type** | **str, none_type** | type | [optional] 
**vcenter_hostname** | **str, none_type** | VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\\\\&quot;:\\\\\&quot;. | [optional] 
**vcenter_username** | **str, none_type** | Application VMware vCenter username. | [optional] 
**volume_count** | **int, none_type** | Count of volumes associated with the volume collection. | [optional] 
**volume_list** | [**[NimbleVolumeSummary], none_type**](NimbleVolumeSummary.md) | List of volumes associated with the volume collection. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


