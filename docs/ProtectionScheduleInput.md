# ProtectionScheduleInput

Protection schedule details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of snapshot schedule to create. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | 
**num_retain** | **int** | Number of snapshots to retain. If replication is enabled on this schedule the array will always retain the latest replicated snapshot, which may exceed the specified retention value. This is necessary to ensure efficient replication performance. Unsigned 64-bit integer. | 
**at_time** | **int, none_type** | Time of day when snapshot should be taken. In case repeat frequency specifies more than one snapshot in a day then the until_time option specifies until what time of day to take snapshots. Non-negative integer in range [0,86399] which is equivalent to [0:00:00 AM, 23:59:59 PM]. | [optional] 
**days** | **str, none_type** | Specifies which days snapshots should be taken. Comma separated list of days of the week or &#39;all&#39;. | [optional] 
**description** | **str, none_type** | Description of the schedule. String of up to 255 printable ASCII characters. | [optional] 
**disable_appsync** | **bool, none_type** | Disables application synchronized snapshots and creates crash consistent snapshots instead. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**downstream_partner** | **str, none_type** | Specifies the partner name if snapshots created by this schedule should be replicated. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  | [optional] 
**downstream_partner_id** | **str, none_type** | Specifies the partner ID if snapshots created by this schedule should be replicated. In an update operation, if snapshots should be replicated, set this attribute to the ID of the replication partner. If snapshots should not be replicated, set this attribute to the empty string. An optional NsObjectID. A 42 digit hexadecimal number or the empty string. | [optional] 
**num_retain_replica** | **int, none_type** | Number of snapshots to retain on the replica. Unsigned 64-bit integer. | [optional] 
**period** | **int, none_type** | Repeat interval for snapshots with respect to the period_unit. For example, a value of 2 with the &#39;period_unit&#39; of &#39;hours&#39; results in one snapshot every 2 hours. Unsigned 64-bit integer. | [optional] 
**period_unit** | **str, none_type** | Time unit over which to take the number of snapshots specified in &#39;period&#39;. For example, a value of &#39;days&#39; with a &#39;period&#39; of &#39;1&#39; results in one snapshot every day. Possible values: &#39;minutes&#39;, &#39;hours&#39;, &#39;days&#39;, &#39;weeks&#39;. | [optional] 
**repl_alert_thres** | **int, none_type** | Replication alert threshold in seconds. If the replication of a snapshot takes more than this amount of time to complete an alert will be generated. Enter 0 to disable this alert. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**replicate_every** | **int, none_type** | Specifies which snapshots should be replicated. If snapshots are replicated and this option is not specified, every snapshot is replicated. Unsigned 64-bit integer.  | [optional] 
**schedule_type** | **str, none_type** | Normal schedules have internal timers which drive snapshot creation. An externally driven schedule has no internal timers. All snapshot activity is driven by an external trigger. In other words, these schedules are used only for externally driven manual snapshots. Possible values: &#39;regular&#39;, &#39;external_trigger&#39; | [optional] 
**skip_db_consistency_check** | **bool, none_type** | Skip consistency check for database files on snapshots created by this schedule. This option only applies to snapshot schedules of a protection template with application synchronization set to VSS, application ID set to MS Exchange 2010 or later w/DAG, this schedule&#39;s snap_verify option set to yes, and its disable_appsync option set to false. Skipping consistency checks is only recommended if each database in a DAG has multiple copies. Possible values: &#39;true&#39;, &#39;false&#39;.  | [optional] 
**snap_verify** | **bool, none_type** | Run verification tool on snapshot created by this schedule. This option can only be used with snapshot schedules of a protection template that has application synchronization. The tool used to verify snapshot depends on the type of application. For example, if application synchronization is VSS and the application ID is Exchange, eseutil tool is run on the snapshots. If verification fails, the logs are not truncated. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**until_time** | **int, none_type** | Time of day to stop taking snapshots. Applicable only when repeat frequency specifies more than one snapshot in a day. Non-negative integer in range [0,86399] which is equivalent to [0:00:00 AM, 23:59:59 PM]. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


