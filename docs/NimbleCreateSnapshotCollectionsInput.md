# NimbleCreateSnapshotCollectionsInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_type** | **str** | External management agent type for snapshots being created as part of snapshot collection. Possible values: &#39;none&#39;, &#39;smis&#39;, &#39;vvol&#39;, &#39;openstack&#39;, &#39;openstackv2&#39;. | [optional] 
**allow_writes** | **bool** | Atollow applications to write to created snapshot(s). Mandatory and must be set to &#39;true&#39; for VSS application synchronized snapshots. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**description** | **str** | Text description of snapshot collection. String of up to 255 printable ASCII characters. Example: &#39;99.9999% availability&#39;. | [optional] 
**disable_appsync** | **bool** | Do not perform application synchronization for this snapshot, create a crash-consistent snapshot instead. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**invoke_on_upstream_partner** | **bool** | Invoke snapshot request on upstream partner. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**is_external_trigger** | **bool** | Is externally triggered. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**metadata** | [**list[KeyValue]**](KeyValue.md) | Key-value pairs that augment a snapshot collection&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. | [optional] 
**name** | **str** | Name of snapshot collection. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints. | 
**replicate** | **bool** | True if this snapshot collection has been marked for replication. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**replicate_to** | **str** | Specifies the partner name that the snapshots in this snapshot collection are replicated to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. Example: &#39;myobject-5&#39;. | [optional] 
**skip_db_consistency_check** | **bool** | Skip consistency check for database files on this snapshot. This option only applies to volume collections with application synchronization set to VSS, application ID set to MS Exchange 2010 or later with Database Availability Group (DAG), snap_verify option set to true, and disable_appsync option set to false. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**snap_verify** | **bool** | Run verification tool on this snapshot. This option can only be used with a volume collection that has application synchronization. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**start_online** | **bool** | Start with snapshot set online. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**vol_snap_attr_list** | [**list[NimbleVolumeSnapAttr]**](NimbleVolumeSnapAttr.md) | List of snapshot attributes for snapshots being created as part of snapshot collection creation. List of volumes with per snapshot attributes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


