# ReplicationPartnerListPolicies

The policy assigned to the replication partner remote group.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_active** | **bool, none_type** | Specifies active active policy of the group. | [optional] 
**auto_failover** | **bool, none_type** | Automatic failover on a group. | [optional] 
**auto_recover** | **bool, none_type** | If the group is stopped as a result of links going down, the group can be automatically restarted after the links come back up. | [optional] 
**auto_synchronize** | **bool, none_type** | Specifies auto synchronization of the group. | [optional] 
**multi_target_peer_persistence** | **bool, none_type** | Specifies that the group is participating in a Multi-target Peer Persistence configuration. The group must have two targets, one of which must be synchronous.The synchronous group target also requires pathManagement and auto Fail over policy settings. | [optional] 
**over_period_alert** | **bool, none_type** | If synchronization of an asynchronous periodic group takes longer to complete than its synchronization period, an alert is generated. | [optional] 
**path_management** | **bool, none_type** | Path management on a group. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


