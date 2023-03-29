# ReplicationPartnerList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str, none_type** | customer ID | [optional] 
**display_name** | **str, none_type** | Replication partner display name. | [optional] 
**domain** | **str, none_type** | Domain that the resource belongs to. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**group_id** | **str, none_type** | Unique id of replication partner remote group | [optional] 
**group_last_sync_time** | [**SyncTime**](SyncTime.md) |  | [optional] 
**group_name** | **str, none_type** | Replication partner remote group name. | [optional] 
**group_object_id** | **int, none_type** | Replication partner group ID. | [optional] 
**id** | **str, none_type** | Unique Identifier of the replication partner. | [optional] 
**is_protection_policy_configured** | **bool** | Boolean value to indicate if protection policy is properly configured on the volume set. If it is set to false, user needs to either delete the policy or fix the policy configuration. All other operations will be blocked in this scenario. | [optional] 
**is_remote_array_support_replication** | **bool** | Boolean value to indicate if remote array OS version supports replication | [optional] 
**is_source_array_support_replication** | **bool** | Boolean value to indicate if source array OS version supports replication | [optional] 
**mode** | **str, none_type** | Replication partner group mode. | [optional] 
**policies** | [**ReplicationPartnerListPolicies**](ReplicationPartnerListPolicies.md) |  | [optional] 
**protection_type** | **str, none_type** | Type of protection | [optional] 
**remote_snp_cpg** | **str, none_type** | Name for which the snapshot space is allocated on the remote target. | [optional] 
**remote_usr_cpg** | **str, none_type** | Name for which the user space is allocated on the remote target. | [optional] 
**remote_volume_set_name** | **str, none_type** | Target volume set name where remote protection is enabled | [optional] 
**resource_uri** | **str** | resourceUri for replication partner list where volume set is remote protected | [optional] 
**role_reversed** | **bool, none_type** | Remote group role switched due to a fail over. | [optional] 
**snap_frequency_secs** | **int, none_type** | Specifies the interval in seconds at which remote group takes coordinated snapshots. This field applies only to Async mode: it is set to -1 otherwise. | [optional] 
**state** | **str, none_type** | Status of the Remote group for the replication partner. Can be New, Starting, Started, Restart, Stopped, Backup, Failsafe or Logging. Null if unset. | [optional] 
**sync_period** | **int** | Time period in seconds for automatic resynchronization. The value must be at least five minutes and not more than one year. Defaults to 0. | [optional] 
**system_id** | **str, none_type** | Unique ID or serial number of the system. | [optional] 
**system_name** | **str, none_type** | Name of the system. | [optional] 
**system_wwn** | **str, none_type** | WWN of the system. | [optional] 
**target_name** | **str, none_type** | Target to which the volume group is mirrored. This is the same as replication partner. | [optional] 
**type** | **str, none_type** | type | [optional] 
**volume_count** | **int, none_type** | Number of volumes in the group for a replication partner. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


