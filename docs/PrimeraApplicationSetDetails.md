# PrimeraApplicationSetDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_set_business_unit** | **str, none_type** | Appset BusinessUnit | [optional] 
**app_set_comments** | **str, none_type** | Application set comments | [optional] 
**app_set_exclude_aiqo_s** | **str, none_type** | Exclusion from AI QoS | [optional] 
**app_set_id** | **int, none_type** | ID | [optional] 
**app_set_importance** | **str, none_type** | Importance Level | [optional] 
**app_set_name** | **str, none_type** | Application set name | [optional] 
**app_set_type** | **str, none_type** | Type of the application set | [optional] 
**associated_links** | [**[PrimeraApplicationSetCapacityStatsAssociatedLinks]**](PrimeraApplicationSetCapacityStatsAssociatedLinks.md) | Associated Links Details | [optional] 
**comment** | **str, none_type** | Comments if any | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**display_name** | **str, none_type** | Display Name | [optional] 
**domain** | **str, none_type** | Domain name | [optional] 
**export_status** | **str, none_type** | Export status | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**id** | **str, none_type** | uid of the applicationset | [optional] 
**initiators** | [**[PrimeraApplicationSetDetailsInitiators], none_type**](PrimeraApplicationSetDetailsInitiators.md) | Initiator details | [optional] 
**is_failover_allowed** | **bool, none_type** | Shows if failover is allowed or not | [optional] 
**is_override_allowed** | **bool, none_type** | Shows if Override is allowed or not | [optional] 
**is_primary** | **bool, none_type** | States if the Application set is Primary or not | [optional] 
**is_sync_allowed** | **bool, none_type** | Shows if sync is allowed or not | [optional] 
**kv_pairs_present** | **bool** | Represents KV pairs present or not | [optional] 
**members** | **[str, none_type], none_type** | Volume Names | [optional] 
**name** | **str, none_type** | Name of the application set | [optional] 
**non_zero_rto_config** | **str, none_type** | Non-Zero RTO configuration. Supported config is Active-Sync | [optional] 
**remote_recovery_point** | [**RecoveryPoint**](RecoveryPoint.md) |  | [optional] 
**replication_partner** | [**[PrimeraApplicationSetDetailsReplicationPartner], none_type**](PrimeraApplicationSetDetailsReplicationPartner.md) | Shows the Replication Partner Systems and Replication Partners | [optional] 
**replication_state** | **str, none_type** | Shows whether data replication is in started or stopped state | [optional] 
**replication_traffic** | **str, none_type** | Shows the direction of flow of data | [optional] 
**replication_type** | **str** | Mode of replication. Can be sync or periodic | [optional] 
**request_uri** | **str, none_type** | RequestUri for applicationsets resources | [optional] 
**serial_number** | **str, none_type** | Serial number. | [optional] 
**size_mi_b** | **float, none_type** | Size in MB of appset | [optional] 
**snap_set_parent_id** | **int, none_type** | ParentId of the snapSet | [optional] 
**snap_set_parent_name** | **str, none_type** | Parent name of the snapSet | [optional] 
**system_id** | **str, none_type** | SystemUid/serialNumber of the array. | [optional] 
**type** | **str, none_type** | type | [optional] 
**vv_set_type** | **str, none_type** | Type of the volume-set | [optional] 
**zero_rto_config** | **str, none_type** | Zero RTO configuration. Supported configs are Active Peer Persistence and Peer Persistence | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


