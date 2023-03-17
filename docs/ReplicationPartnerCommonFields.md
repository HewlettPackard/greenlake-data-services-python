# ReplicationPartnerCommonFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**list[PrimeraVolumeDetailsAssociatedLinks]**](PrimeraVolumeDetailsAssociatedLinks.md) | Associated Links | [optional] 
**buffer_size_b** | **int** | Socket buffer size to use. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**display_name** | **str** | Replication partner displayname. | [optional] 
**domain** | **str** | Domain that the resource belongs to. | [optional] 
**flags** | **int** | Partner flags. | [optional] 
**generation** | **int** | generation | [optional] 
**health** | **int** | Partner health status. | [optional] 
**is_remote_array_support_replication** | **bool** | Boolean value to indicate if remote array OS version supports replication | [optional] 
**min_period_secs** | **int** | Minimum supported Async Periodic period for the partner. The field is omitted if unset or unavailable for the version of partner firmware. | [optional] 
**node_wwn** | **str** | Partner options, with FC partners this includes the partner system&#39;s node WWN. Omitted if unpopulated. | [optional] 
**num_sockets** | **int** | Number of sockets to use. | [optional] 
**policies** | [**ReplicationPartnerCommonFieldsPolicies**](ReplicationPartnerCommonFieldsPolicies.md) |  | [optional] 
**quorum_atf_timeout** | **int** | Automatic Transparent Failover quorum partner failure timeout. | [optional] 
**quorum_ip_address** | **str** | Quorum IP Address associated with the partner. Set to &#39;NA&#39; if not available. | [optional] 
**quorum_ssl_port** | **int** | Quorum SSL port number. | [optional] 
**quorum_status** | **str** | Quorum status of the partner. Possible values - Uninitialized, Initializing, Standby, Active, Failsafe, Failover or Restarting. Null if unset. | [optional] 
**quorum_status_qual** | **str** | Quorum status qualifier. Set to &#39;NA&#39; if not available. | [optional] 
**quorum_version** | **str** | Quorum version. | [optional] 
**remote_id** | **str** | Unique id of the remote replication partner. | [optional] 
**remote_name** | **str** | Name of the remote replication partner. | [optional] 
**remote_replication_id** | **int** | Replication ID of the remote replication partner. | [optional] 
**remote_system_id** | **str** | Unique ID or serial number of the remote system. | [optional] 
**remote_system_name** | **str** | Name of the remote system. | [optional] 
**replication_id** | **int** | Replication ID of the partner. | [optional] 
**replication_partner_links** | [**RemoteCopyLinks**](RemoteCopyLinks.md) |  | [optional] 
**replication_system_id** | **int** | ID of the remote system. | [optional] 
**resource_uri** | **str** | resourceUri for detailed replication partner object | [optional] 
**state** | **str** | State of the replication partner. | [optional] 
**system_id** | **str** | Unique ID or serial number of the system. | [optional] 
**system_name** | **str** | Name of the system. | [optional] 
**system_wwn** | **str** | WWN of the system. | [optional] 
**type** | **str** | type | [optional] 
**version** | **int** | Partner version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


