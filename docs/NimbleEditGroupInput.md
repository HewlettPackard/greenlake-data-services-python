# NimbleEditGroupInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_switchover_enabled** | **bool** | Whether automatic switchover of Group management services feature is enabled. | [optional] 
**autoclean_unmanaged_snapshots_enabled** | **bool** | Whether auto-clean unmanaged snapshots feature is enabled. | [optional] 
**autoclean_unmanaged_snapshots_ttl_unit** | **int** | Unit for unmanaged snapshot time to live. | [optional] 
**cc_mode_enabled** | **bool** | Enable or disable Common Criteria mode. | [optional] 
**date** | **int** | Unix epoch time local to the group. Seconds since last epoch i.e. 00:00 January 1, 1970. Setting this along with ntp_server causes ntp_server to be reset. | [optional] 
**default_iscsi_target_scope** | **str** | Newly created volumes are exported under iSCSI Group Target or iSCSI Volume Target. | [optional] 
**group_snapshot_ttl** | **int** | Snapshot Time-to-live(TTL) configured at group level for automatic deletion of unmanaged snapshots. Value 0 indicates unlimited TTL. | [optional] 
**group_target_name** | **str** | Iscsi target name for this group. Plain string. | [optional] 
**name** | **str** | Name of the group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**ntp_server** | **str** | Either IP address or hostname of the NTP server for this group. | [optional] 
**tdz_enabled** | **bool** | Is Target Driven Zoning (TDZ) enabled on this group. | [optional] 
**tdz_prefix** | **str** | Target Driven Zoning (TDZ) prefix for peer zones created by TDZ. | [optional] 
**timezone** | **str** | Timezone in which this group is located. Plain string. | [optional] 
**tlsv1_enabled** | **bool** | Enable or disable TLSv1.0 and TLSv1.1. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


