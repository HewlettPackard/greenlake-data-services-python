# Parameters

System parameters

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_processor_cookie** | **str, none_type** | Service processor cookie | [optional] 
**allow_domain_users_affect_no_domain** | **bool, none_type** |  | [optional] 
**allow_ssz** | **bool, none_type** | Enables or disables support for using the -ssz option during CPG creation | [optional] 
**allow_wrtback_single_node** | **int, none_type** | Allow writeback single node setting in days | [optional] 
**allow_wrtback_upgrade** | **int, none_type** | Allow the system to continue caching when in a single node state during an upgrade for up to the specified number of days | [optional] 
**auto_admit_tune** | **bool, none_type** | Enables or disables automatic rebalancing when admithw detects new disks. Only applies to 2-node systems | [optional] 
**auto_export_after_reboot** | **bool, none_type** | Enables or disables automatically exporting vluns after a reboot. If disabled, vluns and host ports will not become active after a reboot until \&quot;setsysmgr export_vluns\&quot; is issued. | [optional] 
**compliance_officer_approval** | **bool, none_type** | Specifies whether to enable or disable the compliance officer approval mode. | [optional] 
**disable_chunklet_init_unmap** | **bool, none_type** | Flag to know if the ChunkletInitUNMAP is disabled | [optional] 
**enable_aiqo_s** | **str, none_type** | Enable or disable AI QoS feature, values are:yes or no | [optional] 
**event_log_num** | **int, none_type** | The number of event log files | [optional] 
**event_log_size** | **str, none_type** | The size of the event log file | [optional] 
**failover_matched_set** | **bool, none_type** | When using Matched Set VLUN templates for exports and Persistent Ports together, you must enable this parameter. The default for this setting is disabled | [optional] 
**fc_raw_space_alert** | **int, none_type** | FC raw space alert setting in MiB | [optional] 
**host_dif** | **str, none_type** | Host Data Integrity Field type are:yes or no | [optional] 
**host_dif_template** | **str, none_type** | HostDIF Template | [optional] 
**max_volume_retention** | **int, none_type** | Maximum global volume retention policy in seconds | [optional] 
**nl_raw_space_alert** | **int, none_type** | NL raw space alert setting in MiB | [optional] 
**overprov_ratio_limit** | **float, none_type** | Over provisioning ratio limit setting | [optional] 
**overprov_ratio_warning** | **float, none_type** | Over provisioning ratio warning setting | [optional] 
**persona_profile** | **str, none_type** | If set to &#39;block-preferred&#39; File persona is supported. The default is &#39;block-only&#39; | [optional] 
**port_failover_enabled** | **bool, none_type** | Enables or disables the automatic failover of target ports to their designated partner ports | [optional] 
**r6_layout_version** | **str, none_type** | RAID6 implementation version in use | [optional] 
**remote_copy_host_throttling** | **bool, none_type** | Enables or disables Remote Copy throttling policy for host IO replicated in asynchronous streaming mode | [optional] 
**remote_sys_log** | **int, none_type** | Remote Syslog Enabled/Disabled | [optional] 
**remote_sys_log_host** | **str, none_type** | Host details for Remote Syslog | [optional] 
**remote_sys_log_security_host** | **str, none_type** | Security Host details for Remote Syslog | [optional] 
**session_timeout** | **int, none_type** | Idle session timeout for a CLI session | [optional] 
**single_lun_host** | **bool, none_type** | Enables or disables support to limit volume exports such that each volume can only be exported to a given host one time | [optional] 
**ssd_raw_space_alert** | **int, none_type** | SSD raw space alert setting in MiB | [optional] 
**thermal_shutdown** | **bool, none_type** | Enables or disables a system shutdown when the temperature gets too hot | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


