# NimbleReplicationPartnerCommon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**control_port** | **int** | Port number of partner control interface. Value -1 for an invalid port or a positive integer value up to 65535 representing the TCP/IP port. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**data_port** | **int** | Port number of partner data interface. Value -1 for an invalid port or a positive integer value up to 65535 representing the TCP/IP port. | [optional] 
**description** | **str** | Description of replication partner. String of up to 255 printable ASCII characters. | [optional] 
**full_name** | **str** | Fully qualified name of replication partner. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**generation** | **int** | generation | [optional] 
**last_keepalive_error** | **str** | Most recent error while attempting to ping the partner. Plain string. | [optional] 
**last_modified** | **int** | Time when this replication partner was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**last_sync_error** | **str** | Most recent error seen while attempting to sync objects to the partner. Plain string. | [optional] 
**match_folder** | **bool** | Indicates whether to match the upstream volumes folder on the downstream. Possible values: true, false | [optional] 
**partner_group_uid** | **int** | Replication partner group uid. Unsigned 64-bit integer. | [optional] 
**port_range_start** | **int** | Positive integer value up to 65535 representing TCP/IP port. Example: 1234. | [optional] 
**proxy_hostname** | **str** | String of up to 64 alphanumeric characters, - and . and : are allowed after first character. Example: &#39;myobject-5&#39; | [optional] 
**proxy_user** | **str** | HTTP proxy server username, string up to 255 characters, special characters ([, ], &#x60;, ;, ampersand, tab, space, newline) are not allowed. | [optional] 
**remote_partner_folder_id** | **str** | The folder ID where volumes replicated from remote partner will be created. Replica volumes created as clones ignore this parameter and are always created in the same pool as their parent volume. A 42 digit hexadecimal number. | [optional] 
**remote_partner_folder_name** | **str** | The folder name where volumes replicated from remote partner will be created. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. Example: &#39;myobject-5&#39;. | [optional] 
**remote_partner_id** | **str** | ID of the remote partner. | [optional] 
**remote_partner_name** | **str** | Name of the remote partner. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. Example: &#39;myobject-5&#39;. | [optional] 
**remote_partner_pool_id** | **str** | The pool ID where volumes replicated from remote partner will be created. Replica volumes created as clones ignore this parameter and are always created in the same pool as their parent volume. A 42 digit hexadecimal number. | [optional] 
**remote_partner_pool_name** | **str** | The pool name where volumes replicated from remote partner will be created. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. Example: &#39;myobject-5&#39;. | [optional] 
**remote_partner_subnet_label** | **str** | Label of the subnet used to replicate to remote partner. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | [optional] 
**remote_partner_subnet_type** | **str** | Type of the subnet used to replicate to the remote partner. Possible values are &#39;invalid&#39;, &#39;unconfigured&#39;, &#39;mgmt&#39;, &#39;data&#39;, &#39;mgmt_data&#39;. | [optional] 
**remote_partner_system_id** | **str** | ID of the system to which the remote partner belongs. | [optional] 
**replication_direction** | **str** | Direction of replication configured with this partner. Possible values: none, downstream, upstream, bi_directional | [optional] 
**search_name** | **str** | Name of replication partner used for object search. Alphanumeric string, up to 64 characters including hyphen, period, colon. | [optional] 
**status** | **str** | Status of the partner. Failed, Normal, Degraded, Unknown. | [optional] 
**throttled_bandwidth_current** | **int** | Current bandwidth throttle for this partner, expressed either as megabits per second or as -1 to indicate that there is no throttle. Signed 64-bit integer. | [optional] 
**throttled_bandwidth_current_kbps** | **int** | Current bandwidth throttle for this partner, expressed either as kilobits per second or as -1 to indicate that there is no throttle. Signed 64-bit integer. | [optional] 
**throttles** | [**list[ReplicationThrottle]**](ReplicationThrottle.md) | Throttles used while replicating from/to this partner. All the throttles for the partner. | [optional] 
**type** | **str** | type | [optional] 
**unique_name** | **bool** | Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**volume_collection_list** | [**list[ReplicationVolumeCollectionSummary]**](ReplicationVolumeCollectionSummary.md) | List of volume collections that are replicating from/to this partner. List of volume collections. | [optional] 
**witness** | **str** | Hostname or ip addresses of witness. Comma separated strings of up to 63 characters of hostname and/or ip addresses. Total length cannot exceed 255 characters. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


