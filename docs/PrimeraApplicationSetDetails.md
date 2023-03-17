# PrimeraApplicationSetDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_set_business_unit** | **str** | Appset BusinessUnit | [optional] 
**app_set_comments** | **str** | Application set comments | [optional] 
**app_set_exclude_ai_qo_s** | **str** | Exclusion from AI QoS | [optional] 
**app_set_id** | **int** | ID | [optional] 
**app_set_importance** | **str** | Importance Level | [optional] 
**app_set_name** | **str** | Application set name | [optional] 
**app_set_type** | **str** | Type of the application set | [optional] 
**associated_links** | [**list[AssociatedLinksInner]**](AssociatedLinksInner.md) | Associated Links Details | [optional] 
**comment** | **str** | Comments if any | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**display_name** | **str** | Display Name | [optional] 
**domain** | **str** | Domain name | [optional] 
**export_status** | **str** | Export status | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | uid of the applicationset | [optional] 
**initiators** | [**list[PrimeraApplicationSetDetailsInitiators]**](PrimeraApplicationSetDetailsInitiators.md) | Initiator details | [optional] 
**is_failover_allowed** | **bool** | Shows if failover is allowed or not | [optional] 
**is_override_allowed** | **bool** | Shows if Override is allowed or not | [optional] 
**is_primary** | **bool** | States if the Application set is Primary or not | [optional] 
**is_sync_allowed** | **bool** | Shows if sync is allowed or not | [optional] 
**kv_pairs_present** | **bool** | Represents KV pairs present or not | [optional] 
**members** | **list[str]** | Volume Names | [optional] 
**name** | **str** | Name of the application set | [optional] 
**non_zero_rto_config** | **str** | Non-Zero RTO configuration. Supported config is Active-Sync | [optional] 
**remote_recovery_point** | [**RecoveryPoint**](RecoveryPoint.md) |  | [optional] 
**replication_partner** | [**list[PrimeraApplicationSetDetailsReplicationPartner]**](PrimeraApplicationSetDetailsReplicationPartner.md) | Shows the Replication Partner Systems and Replication Partners | [optional] 
**replication_state** | **str** | Shows whether data replication is in started or stopped state | [optional] 
**replication_traffic** | **str** | Shows the direction of flow of data | [optional] 
**replication_type** | **str** | Mode of replication. Can be sync or periodic | [optional] 
**request_uri** | **str** | RequestUri for applicationsets resources | [optional] 
**serial_number** | **str** | Serial number. | [optional] 
**size_mi_b** | **float** | Size in MB of appset | [optional] 
**snap_set_parent_id** | **int** | ParentId of the snapSet | [optional] 
**snap_set_parent_name** | **str** | Parent name of the snapSet | [optional] 
**system_id** | **str** | SystemUid/serialNumber of the array. | [optional] 
**type** | **str** | type | [optional] 
**vv_set_type** | **str** | Type of the volume-set | [optional] 
**zero_rto_config** | **str** | Zero RTO configuration. Supported configs are Active Peer Persistence and Peer Persistence | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


