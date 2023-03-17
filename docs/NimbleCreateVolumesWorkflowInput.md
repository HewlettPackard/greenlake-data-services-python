# NimbleCreateVolumesWorkflowInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_type** | **str** | External management agent type. Defaults to &#39;none&#39;. Possible values: &#39;none&#39;, &#39;smis&#39;, &#39;vvol&#39;, &#39;openstack&#39;, &#39;openstackv2&#39; | [optional] 
**app_uuid** | **str** | Application identifier of volume. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. Defaults to the empty string.  | [optional] 
**count** | **int** | Number of volumes to be created. | 
**dedupe_enabled** | **bool** | Indicate whether dedupe is enabled. Defaults to &#39;false&#39;. | [optional] 
**downstream_partner** | **str** | Name of the downstream partner | [optional] 
**downstream_partner_id** | **str** | ID of the downstream partner | [optional] 
**folder_id** | **str** | ID of the folder holding this volume. An optional NsObjectID. A 42 digit hexadecimal int64 or the empty string. Defaults to the empty string. | [optional] 
**host_groups** | [**list[NimbleHostGroupDetails]**](NimbleHostGroupDetails.md) | List of host group details. | [optional] 
**limit** | **int** | Limit for the volume as a percentage of volume size. Percentage as integer from 0 to 100. Defaults to the default volume limit set on group, typically 100. | [optional] 
**limit_iops** | **int** | IOPS limit for this volume. If limit_iops is not specified when a volume is created, or if limit_iops is set to -1, then the volume has no IOPS limit. If limit_iops is not specified while creating a clone, IOPS limit of parent volume will be used as limit. IOPS limit should be in range [256, 4294967294] or -1 for unlimited. If both limit_iops and limit_mbps are specified, limit_mbps must not be hit before limit_iops. In other words, IOPS and MBPS limits should honor limit_iops _ampersand_amp;lt;&#x3D; ((limit_mbps MB/s * 2^20 B/MB) / block_size B). By default the volume is created with unlimited iops. | [optional] 
**limit_mbps** | **int** | Throughput limit for this volume in MB/s. If limit_mbps is not specified when a volume is created, or if limit_mbps is set to -1, then the volume has no MBPS limit. MBPS limit should be in range [1, 4294967294] or -1 for unlimited. If both limit_iops and limit_mbps are specified, limit_mbps must not be hit before limit_iops. In other words, IOPS and MBPS limits should honor limit_iops _ampersand_amp;lt;&#x3D; ((limit_mbps MB/s * 2^20 B/MB) / block_size B). By default, the volume is created with unlimited throughput. | [optional] 
**name** | **str** | Name of the volume. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. This type is used for object sets containing volumes, snapshots, snapshot collections and protocol endpoints. | 
**perfpolicy** | [**CustomApp**](CustomApp.md) |  | [optional] 
**perfpolicy_id** | **str** | Identifier of the performance policy. After creating a volume, performance policy for the volume can only be changed to another performance policy with same block size. A 42 digit hexadecimal int64. Defaults to ID of the &#39;default&#39; performance policy. | [optional] 
**pool_id** | **str** | Identifier associated with the pool in the storage pool table. A 42 digit hexadecimal int64. Defaults to the ID of the &#39;default&#39; pool. | [optional] 
**protection_policy_id** | **str** | Protection policy ID | [optional] 
**protection_policy_schedules** | [**list[NimbleCreateVolumesWorkflowInputProtectionPolicySchedules]**](NimbleCreateVolumesWorkflowInputProtectionPolicySchedules.md) | Protection Policy Schedule | [optional] 
**replication_start_time** | **int** | Remote replication start time which  will be used to offset local snapshot start time | [optional] 
**size** | **int** | Volume size in megabytes. Size is required for creating a volume but not for cloning an existing volume.When creating a new volume, size is required. When cloning an existing volume, size defaults to that of the parent volume. | 
**vol_col_id** | **str** | volume collection id | [optional] 
**vol_col_name** | **str** | volume collection Name | [optional] 
**warn_level** | **int** | Threshold for available space as a percentage of volume size below which an alert is raised. If this option is not specified, array default volume warn level setting is used to decide the warning level for this volume. Percentage as integer from 0 to 100. Defaults to the default volume warning level set on the group, typically 80. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


