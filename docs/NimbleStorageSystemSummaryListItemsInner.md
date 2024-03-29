# NimbleStorageSystemSummaryListItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Identifier of the group. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str, none_type** | Name of the group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 
**access_protocol_list** | **[str, none_type], none_type** | Protocol used to access this group. List of access protocols. | [optional] 
**alarms_enabled** | **bool, none_type** | Whether alarm feature is enabled. | [optional] 
**alert_from_email_addr** | **str, none_type** | From email address to use while sending emails. Case insensitive email address. | [optional] 
**alert_min_level** | **str, none_type** | Minimum level of alert to be notified. Possible values: &#39;info&#39;, &#39;notice&#39;, &#39;warning&#39;, &#39;critical&#39;. | [optional] 
**alert_to_email_addrs** | **str, none_type** | Comma-separated list of email addresss to receive emails. Comma separated email list. | [optional] 
**allow_support_tunnel** | **bool, none_type** | Whether to allow support tunnel. | [optional] 
**array_unassign_migration_status** | [**[ArrayUnassignMigStatus], none_type**](ArrayUnassignMigStatus.md) | Data migration status for arrays being removed from their pool. Data migration status information for arrays being unassigned from their pool. | [optional] 
**arrays** | [**NimbleArrayList**](NimbleArrayList.md) |  | [optional] 
**associated_links** | [**GroupAssociatedLinks**](GroupAssociatedLinks.md) |  | [optional] 
**auto_switchover_enabled** | **bool, none_type** | Whether automatic switchover of Group management services feature is enabled. | [optional] 
**auto_switchover_messages** | [**[NimbleErrorWithArguments], none_type**](NimbleErrorWithArguments.md) | List of validation messages for automatic switchover of Group Management. This will be empty when there are no conflicts found. | [optional] 
**autoclean_unmanaged_snapshots_enabled** | **bool, none_type** | Whether auto-clean unmanaged snapshots feature is enabled. | [optional] 
**autoclean_unmanaged_snapshots_ttl_unit** | **int, none_type** | Deprecated. Unit for unmanaged snapshot time to live. | [optional] 
**autosupport_enabled** | **bool, none_type** | Whether to send autosupport. | [optional] 
**cc_mode_enabled** | **bool, none_type** | Enable or disable Common Criteria mode. | [optional] 
**clone_ratio** | **float, none_type** | Clone savings for the group expressed as ratio. Fraction expressed as floating point number. | [optional] 
**compressed_snap_usage_bytes** | **int, none_type** | Compressed usage of snapshots in the group. | [optional] 
**compressed_vol_usage_bytes** | **int, none_type** | Compressed usage of volumes in the group. | [optional] 
**compression_ratio** | **float, none_type** | Compression savings for the group expressed as ratio. Fraction expressed as floating point number. | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**data_rebalance_status** | [**[PoolRebalanceMigStatus], none_type**](PoolRebalanceMigStatus.md) | Status of data rebalancing operations for pools in the group. Status of data re-balancing operations for a list of pools. | [optional] 
**data_reduction_ratio** | **float, none_type** | Space savings in the group that does not include thin-provisioning savings expressed as ratio. Fraction expressed as floating point number. | [optional] 
**date** | **int, none_type** | Unix epoch time local to the group. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**dedupe_ratio** | **float, none_type** | Dedupe savings for the group expressed as ratio. Fraction expressed as floating point number. | [optional] 
**default_iscsi_target_scope** | **str, none_type** | Newly created volumes are exported under iSCSI Group Target or iSCSI Volume Target. | [optional] 
**default_snap_limit_percent** | **int, none_type** | Default limit for a volumes snapshot space usage, expressed either as a percentage of the volumes size or as -1 to indicate that there is no limit. A volume will be taken offline or made non-writable upon exceeding its snapshot limit. Signed 64-bit integer. | [optional] 
**default_snap_reserve** | **int, none_type** | Amount of space to reserve for snapshots of a volume as a percentage of volume size. | [optional] 
**default_snap_warn_level** | **int, none_type** | Default threshold for snapshot space usage of a volume as a percentage of volume size above which an alert is raised. | [optional] 
**default_volume_limit** | **int, none_type** | Default limit for a volume space usage as a percentage of volume size. Volume will be taken offline/made non-writable on exceeding its limit. Percentage as integer from 0 to 100. | [optional] 
**default_volume_reserve** | **int, none_type** | Amount of space to reserve for a volume as a percentage of volume size. Percentage as integer from 0 to 100. | [optional] 
**default_volume_warn_level** | **int, none_type** | Default threshold for volume space usage as a percentage of volume size above which an alert is raised. Percentage as integer from 0 to 100. | [optional] 
**dns_servers** | [**[IPAddressObject], none_type**](IPAddressObject.md) | IP addresses for this groups dns servers. List of IP Addresses. | [optional] 
**domain_name** | **str, none_type** | Domain name for this group. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 
**encryption_config** | [**EncryptionSettings**](EncryptionSettings.md) |  | [optional] 
**failover_mode** | **str, none_type** | Failover mode of the group Management Service. Possible values: &#39;Manual&#39;, &#39;Automatic&#39;. | [optional] 
**fc_enabled** | **bool, none_type** | Whether FC is enabled on this group. | [optional] 
**free_space** | **int, none_type** | Free space of the pool in bytes. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**group_snapshot_ttl** | **int, none_type** | Snapshot Time-to-live(TTL) configured at group level for automatic deletion of unmanaged snapshots. Value 0 indicates unlimited TTL. | [optional] 
**group_target_enabled** | **bool, none_type** | Is group_target enabled on this group. | [optional] 
**group_target_name** | **str, none_type** | Iscsi target name for this group. Plain string. | [optional] 
**iscsi_automatic_connection_method** | **bool, none_type** | Is iscsi reconnection automatic. | [optional] 
**iscsi_connection_rebalancing** | **bool, none_type** | Does ISCSI automatically rebalance connections. | [optional] 
**iscsi_enabled** | **bool, none_type** | Whether iSCSI is enabled on this group. | [optional] 
**isns_enabled** | **bool, none_type** | Whether iSNS is enabled. | [optional] 
**isns_port** | **int, none_type** | Port number for iSNS Server. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**isns_server** | **str, none_type** | Hostname or IP Address of iSNS Server. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 
**last_login** | **str, none_type** | Time and user of last login to this group. Plain string. | [optional] 
**leader_array_name** | **str, none_type** | Name of the array where the group Management Service is running. | [optional] 
**leader_array_serial** | **str, none_type** | Serial number of the array where the group Management Service is running. | [optional] 
**management_service_backup_array_name** | **str, none_type** | Name of the array where backup the group Management Service is running. | [optional] 
**management_service_backup_status** | **str, none_type** | HA status of the group Management Service. Possible values: &#39;in_sync&#39;, &#39;remove_in_progress&#39;, &#39;yet_to_setup&#39;, &#39;unsetup_in_progress&#39;, &#39;setup_in_progress&#39;, &#39;out_of_sync&#39;, &#39;add_in_progress&#39;, &#39;setup_failed&#39;. | [optional] 
**member_list** | **[str, none_type], none_type** | Members of this group. A list of object names. | [optional] 
**merge_group_name** | **str, none_type** | Group that were being merged with. Plain string. | [optional] 
**merge_state** | **str, none_type** | State of group merge. Possible values: &#39;dset_start&#39;, &#39;dest_DB&#39;, &#39;dest_DB_done&#39;, &#39;dest_reassigned&#39;, &#39;dest_relinquish&#39;, &#39;dest_DB_failed&#39;, &#39;src_start&#39;, &#39;src_quiesced&#39;, &#39;src_reassigned&#39;, &#39;src_quiesce_failed&#39;, &#39;src_reassign_failed&#39;, &#39;none&#39;. | [optional] 
**ntp_server** | **str, none_type** | Either IP address or hostname of the NTP server for this group. Plain string. | [optional] 
**num_connections** | **int, none_type** | Number of connections to the group. | [optional] 
**num_snapcolls** | **int, none_type** | Number of snapshot collections in this group. | [optional] 
**num_snaps** | **int, none_type** | Number of snapshots in the group. | [optional] 
**pending_deletes** | **int, none_type** | Usage for blocks that are not yet deleted. | [optional] 
**proxy_port** | **int, none_type** | Proxy Port of HTTP Proxy Server. Integer value between 0-65535 representing TCP/IP port. | [optional] 
**proxy_server** | **str, none_type** | Hostname or IP Address of HTTP Proxy Server. Setting this attribute to an empty string will unset all proxy settings. String of alphanumeric characters, can be an empty string, or valid range must be from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 
**proxy_username** | **str, none_type** | Username to authenticate with HTTP Proxy Server. HTTP proxy server username, string up to 255 characters, special characters ([, ], &#x60;, ;, ampersand, tab, space, newline) are not allowed. | [optional] 
**raw_cache_capacity** | **int, none_type** | Total cache capacity of the group. | [optional] 
**raw_capacity** | **int, none_type** | Total capacity of the group. | [optional] 
**repl_throttle_list** | [**[Throttle], none_type**](Throttle.md) | All the replication bandwidth limits on the system. All the throttles for the partner. | [optional] 
**repl_throttled_bandwidth** | **int, none_type** | Current bandwidth throttle for replication, expressed either as megabits per second or as -1 to indicate that there is no throttle. Signed 64-bit integer. | [optional] 
**repl_throttled_bandwidth_kbps** | **int, none_type** | Current bandwidth throttle for replication, expressed either as kilobits per second or as -1 to indicate that there is no throttle. Signed 64-bit integer. | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**savings** | **int, none_type** | Overall space usage savings in the group. | [optional] 
**savings_clone** | **int, none_type** | Space usage savings in the group due to cloning of volumes. | [optional] 
**savings_compression** | **int, none_type** | Space usage savings in the group due to compression. | [optional] 
**savings_data_reduction** | **int, none_type** | Space usage savings in the group that does not include thin-provisioning savings. | [optional] 
**savings_dedupe** | **int, none_type** | Space usage savings in the group due to deduplication. | [optional] 
**savings_ratio** | **float, none_type** | Overall savings in the group expressed as ratio. Fraction expressed as floating point number. | [optional] 
**savings_vol_thin_provisioning** | **int, none_type** | Space usage savings in the group due to thin provisioning of volumes. | [optional] 
**scsi_vendor_id** | **str, none_type** | SCSI vendor ID. Plain string. | [optional] 
**send_alert_to_support** | **bool, none_type** | Whether to send alert to Support. | [optional] 
**smtp_port** | **int, none_type** | Port number of SMTP Server. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**smtp_server** | **str, none_type** | Hostname or IP Address of SMTP Server. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 
**snap_compression_ratio** | **float, none_type** | Compression ratio of snapshots in the group. Fraction expressed as floating point number. | [optional] 
**snap_retn_meter_high** | **int, none_type** | Threshold for considering a volume as high retention. | [optional] 
**snap_retn_meter_very_high** | **int, none_type** | Threshold for considering a volume as very high retention. | [optional] 
**snap_usage_populated** | **int, none_type** | Total snapshot usage as if each snapshot is deep copy of the volume. | [optional] 
**snmp_community** | **str, none_type** | Community string to be used with SNMP. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**snmp_get_enabled** | **bool, none_type** | Whether to accept SNMP get commands. | [optional] 
**snmp_get_port** | **int, none_type** | Port number to which SNMP get requests should be sent. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**snmp_sys_contact** | **str, none_type** | Name of the SNMP administrator. Plain string. | [optional] 
**snmp_sys_location** | **str, none_type** | Location of the group. Plain string. | [optional] 
**snmp_trap_enabled** | **bool, none_type** | Whether to enable SNMP traps. | [optional] 
**snmp_trap_host** | **str, none_type** | Hostname or IP Address to send SNMP traps. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 
**snmp_trap_port** | **int, none_type** | Port number of SNMP trap host. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**space_info_valid** | **bool, none_type** | Is space info for this group valid. | [optional] 
**syslogd_enabled** | **bool, none_type** | Is syslogd enabled on this system. | [optional] 
**syslogd_port** | **int, none_type** | Port number for syslogd server. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**syslogd_server** | **str, none_type** | Hostname of the syslogd server. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 
**syslogd_servers** | [**[NimbleSyslogdServerInfo], none_type**](NimbleSyslogdServerInfo.md) | syslogd server info. | [optional] 
**system_headroom** | [**SystemHeadroom**](SystemHeadroom.md) |  | [optional] 
**tdz_enabled** | **bool, none_type** | Is Target Driven Zoning (TDZ) enabled on this group. | [optional] 
**tdz_prefix** | **str, none_type** | Target Driven Zoning (TDZ) prefix for peer zones created by TDZ. | [optional] 
**timezone** | **str, none_type** | Timezone in which this group is located. Plain string. | [optional] 
**tlsv1_enabled** | **bool, none_type** | Enable or disable TLSv1.0 and TLSv1.1. | [optional] 
**uncompressed_snap_usage_bytes** | **int, none_type** | Uncompressed usage of snapshots in the group. | [optional] 
**uncompressed_vol_usage_bytes** | **int, none_type** | Uncompressed usage of volumes in the group. | [optional] 
**unique_name_enabled** | **bool, none_type** | Are new volume and volume collection names transformed on this group. | [optional] 
**unused_reserve_bytes** | **int, none_type** | Reserved space that is not utilized. | [optional] 
**update_array_names** | **str, none_type** | Arrays in the group undergoing update. Comma separated list of up to 64 non-empty lowercase alphanumeric strings without spaces. | [optional] 
**update_download_end_time** | **int, none_type** | End time of last update. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**update_download_error_code** | **str, none_type** | If the software download has failed, this indicates the error code corresponding to the failure. Non-negative integer in range [0,9000]. | [optional] 
**update_download_start_time** | **int, none_type** | Start time of last update. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**update_downloading** | **bool, none_type** | Is software update package currently downloading. | [optional] 
**update_end_time** | **int, none_type** | End time of last update. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**update_error_code** | **str, none_type** | If the software update has failed, this indicates the error code corresponding to the failure. Non-negative integer in range [0,9000]. | [optional] 
**update_progress_msg** | **str, none_type** | Group update detailed progress message. Plain string. | [optional] 
**update_start_time** | **int, none_type** | Start time of last update. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**update_state** | **str, none_type** | Group update state.Possible values: &#39;invalid&#39;, &#39;normal&#39;, &#39;updating&#39;, &#39;timed_out&#39;, &#39;failed&#39;, &#39;paused&#39;. | [optional] 
**usable_cache_capacity** | **int, none_type** | Usable cache capacity of the group. | [optional] 
**usable_capacity_bytes** | **int, none_type** | Usable capacity bytes of the group. | [optional] 
**usage** | **int, none_type** | Used space of the group in bytes. | [optional] 
**usage_valid** | **bool, none_type** | Indicates whether the usage of group is valid. | [optional] 
**user_inactivity_timeout** | **int, none_type** | The amount of time in seconds that the user session is inactive before timing out. User inactivity timeout in second, valid range is from 1 to 43200 (720 minutes). | [optional] 
**version_current** | **str, none_type** | Version of software running on the group. | [optional] 
**version_rollback** | **str, none_type** | Rollback software version for the group. | [optional] 
**version_target** | **str, none_type** | Desired software version for the group. | [optional] 
**vol_compression_ratio** | **float, none_type** | Compression ratio of volumes in the group. Fraction expressed as floating point number. | [optional] 
**vol_thin_provisioning_ratio** | **float, none_type** | Thin provisioning savings for volumes in the group expressed as ratio. Fraction expressed as floating point number. | [optional] 
**volume_migration_status** | [**[VolFamMigStatus], none_type**](VolFamMigStatus.md) | Status of data migration activity related to volumes being relocated to different pools. List of data migration status for a group of related volumes. | [optional] 
**vss_validation_timeout** | **int, none_type** | The amount of time in seconds to validate Microsoft VSS application synchronization before timing out. VSS validation timeout in second, valid range is from 1 to 3600 (60 minutes). | [optional] 
**vvol_enabled** | **bool, none_type** | Are vvols enabled on this group. | [optional] 
**witness_status** | [**[WitnessTestResponse], none_type**](WitnessTestResponse.md) | Witness status from group Management Service array and group Management Service backup array. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


