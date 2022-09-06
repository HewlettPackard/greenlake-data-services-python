# NimbleNsSchedule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool, none_type** | A schedule is active only if it is owned by the same owner as the volume collection. Only active schedules of a volume collection participate in the creation of snapshots and replication. | [optional] 
**at_time** | **int, none_type** | Time of day when snapshot should be taken. | [optional] 
**days** | **str, none_type** | Which days snapshots should be taken. | [optional] 
**disable_appsync** | **bool, none_type** | Disables application synchronized snapshots and creates crash consistent snapshots instead. | [optional] 
**downstream_partner** | **str, none_type** | Partner name if snapshots created by this schedule should be replicated. | [optional] 
**downstream_partner_id** | **str, none_type** | Partner ID if snapshots created by this schedule should be replicated. | [optional] 
**downstream_partner_name** | **str, none_type** | Partner name if snapshots created by this schedule should be replicated. | [optional] 
**id** | **str, none_type** | ID of protection schedule. | [optional] 
**name** | **str, none_type** | Name of protection schedule. | [optional] 
**num_retain** | **int, none_type** | Number of snapshots to retain. | [optional] 
**num_retain_replica** | **int, none_type** | Number of snapshots to retain on the replica. | [optional] 
**period** | **int, none_type** | Frequency of snapshots. | [optional] 
**period_unit** | **str, none_type** | Units for repeat frequency -- minutes, hours, days or weeks. Possible values: &#39;hours&#39;, &#39;weeks&#39;, &#39;minutes&#39;, &#39;days&#39;. | [optional] 
**repl_alert_thres** | **int, none_type** | Replication alert threshold. | [optional] 
**replicate_every** | **int, none_type** | Which snapshots should be replicated. | [optional] 
**schedule_id** | **str, none_type** | ID of protection schedule. | [optional] 
**schedule_name** | **str, none_type** | Name of protection schedule. | [optional] 
**schedule_type** | **str, none_type** | regular or external_trigger. Possible values: &#39;external_trigger&#39;, &#39;regular&#39;. | [optional] 
**skip_db_consistency_check** | **bool, none_type** | Skip consistency check for database files on snapshots created by this schedule. | [optional] 
**snap_verify** | **bool, none_type** | Run verification tool on snapshot created by this schedule. | [optional] 
**until_time** | **int, none_type** | Time of day to stop taking snapshots. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


