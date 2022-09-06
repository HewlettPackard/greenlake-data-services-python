# NimbleEditFolderInput

Edit Nimble / Alletra 6K Folder input.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appserver_id** | **str, none_type** | Identifier of the application server associated with the folder. | [optional] 
**description** | **str, none_type** | Text description of folder. | [optional] 
**inherited_vol_perfpol_id** | **str, none_type** | Identifier of the default performance policy for a newly created volume. | [optional] 
**limit_iops** | **int, none_type** | IOPS limit for this folder. If limit_iops is not specified when a folder is created, or if limit_iops is set to -1, then the folder has no IOPS limit. IOPS limit should be in range [256, 4294967294] or -1 for unlimited. | [optional] 
**limit_mbps** | **int, none_type** | Throughput limit for this folder in MB/s. If limit_mbps is not specified when a folder is created, or if limit_mbps is set to -1, then the folder has no throughput limit. MBPS limit should be in range [1, 4294967294] or -1 for unlimited. | [optional] 
**limit_size_bytes** | **int, none_type** | Folder size limit in bytes. If limit_size_bytes is not specified when a folder is created, or if limit_size_bytes is set to -1, then the folder has no limit. Otherwise, a limit smaller than the capacity of the pool can be set. Folders with an agent_type of &#39;smis&#39; or &#39;vvol&#39; must have a size limit. | [optional] 
**name** | **str, none_type** | Name of the folder. | [optional] 
**overdraft_limit_pct** | **int, none_type** | Amount of space to consider as overdraft range for this folder as a percentage of folder used limit. Valid values are from 0% - 200%. This is the limit above the folder usage limit beyond which enforcement action(volume offline/non-writable) is issued. | [optional] 
**provisioned_limit_size_bytes** | **int, none_type** | Limit on the provisioned size of volumes in a folder. If provisioned_limit_size_bytes is not specified when a folder is created, or if provisioned_limit_size_bytes is set to -1, then the folder has no provisioned size limit. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


