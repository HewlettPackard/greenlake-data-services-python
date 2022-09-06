# ReplicationPartnerCommonFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**[PrimeraVolumeDetailsAssociatedLinks], none_type**](PrimeraVolumeDetailsAssociatedLinks.md) | Associated Links | [optional] 
**buffer_size_b** | **int, none_type** | Socket buffer size to use. | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**display_name** | **str, none_type** | Replication partner displayname. | [optional] 
**domain** | **str, none_type** | Domain that the resource belongs to. | [optional] 
**flags** | **int, none_type** | Partner flags. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**health** | **int, none_type** | Partner health status. | [optional] 
**is_remote_array_support_replication** | **bool** | Boolean value to indicate if remote array OS version supports replication | [optional] 
**min_period_secs** | **int, none_type** | Minimum supported Async Periodic period for the partner. The field is omitted if unset or unavailable for the version of partner firmware. | [optional] 
**node_wwn** | **str, none_type** | Partner options, with FC partners this includes the partner system&#39;s node WWN. Omitted if unpopulated. | [optional] 
**num_sockets** | **int, none_type** | Number of sockets to use. | [optional] 
**policies** | [**ReplicationPartnerCommonFieldsPolicies**](ReplicationPartnerCommonFieldsPolicies.md) |  | [optional] 
**quorum_atf_timeout** | **int, none_type** | Automatic Transparent Failover quorum partner failure timeout. | [optional] 
**quorum_ip_address** | **str, none_type** | Quorum IP Address associated with the partner. Set to &#39;NA&#39; if not available. | [optional] 
**quorum_ssl_port** | **int, none_type** | Quorum SSL port number. | [optional] 
**quorum_status** | **str, none_type** | Quorum status of the partner. Possible values - Uninitialized, Initializing, Standby, Active, Failsafe, Failover or Restarting. Null if unset. | [optional] 
**quorum_status_qual** | **str, none_type** | Quorum status qualifier. Set to &#39;NA&#39; if not available. | [optional] 
**quorum_version** | **str, none_type** | Quorum version. | [optional] 
**remote_id** | **str, none_type** | Unique id of the remote replication partner. | [optional] 
**remote_name** | **str, none_type** | Name of the remote replication partner. | [optional] 
**remote_replication_id** | **int, none_type** | Replication ID of the remote replication partner. | [optional] 
**remote_system_id** | **str, none_type** | Unique ID or serial number of the remote system. | [optional] 
**remote_system_name** | **str, none_type** | Name of the remote system. | [optional] 
**replication_id** | **int, none_type** | Replication ID of the partner. | [optional] 
**replication_partner_links** | [**RemoteCopyLinks**](RemoteCopyLinks.md) |  | [optional] 
**replication_system_id** | **int, none_type** | ID of the remote system. | [optional] 
**resource_uri** | **str, none_type** | resourceUri for detailed replication partner object | [optional] 
**state** | **str, none_type** | State of the replication partner. | [optional] 
**system_id** | **str, none_type** | Unique ID or serial number of the system. | [optional] 
**system_name** | **str, none_type** | Name of the system. | [optional] 
**system_wwn** | **str, none_type** | WWN of the system. | [optional] 
**type** | **str, none_type** | type | [optional] 
**version** | **int, none_type** | Partner version. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


