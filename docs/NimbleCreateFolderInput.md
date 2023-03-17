# NimbleCreateFolderInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_protocol** | **str** | Access protocol of the folder. This attribute is used by the VASA Provider to determine the access protocol of the bind request. If not specified in the creation request, it will be the access protocol supported by the group. If the group supports multiple protocols, the default will be Fibre Channel. This field is meaningful only to VVol folder. Possible values: &#39;iscsi&#39;, &#39;fc&#39;. | [optional] 
**agent_type** | **str** | External management agent type. Possible values: &#39;none&#39;, &#39;smis&#39;, &#39;vvol&#39;, &#39;openstack&#39;. | [optional] 
**appserver_id** | **str** | Identifier of the application server associated with the folder. | [optional] 
**description** | **str** | Text description of folder. | [optional] 
**inherited_vol_perfpol_id** | **str** | Identifier of the default performance policy for a newly created volume. | [optional] 
**limit_iops** | **int** | IOPS limit for this folder. If limit_iops is not specified when a folder is created, or if limit_iops is set to -1, then the folder has no IOPS limit. IOPS limit should be in range [256, 4294967294] or -1 for unlimited. | [optional] 
**limit_mbps** | **int** | Throughput limit for this folder in MB/s. If limit_mbps is not specified when a folder is created, or if limit_mbps is set to -1, then the folder has no throughput limit. MBPS limit should be in range [1, 4294967294] or -1 for unlimited. | [optional] 
**limit_size_bytes** | **int** | Folder size limit in bytes. If limit_size_bytes is not specified when a folder is created, or if limit_size_bytes is set to -1, then the folder has no limit. Otherwise, a limit smaller than the capacity of the pool can be set. Folders with an agent_type of &#39;smis&#39; or &#39;vvol&#39; must have a size limit. | [optional] 
**name** | **str** | Name of the folder. | 
**overdraft_limit_pct** | **int** | Amount of space to consider as overdraft range for this folder as a percentage of folder used limit. Valid values are from 0% - 200%. This is the limit above the folder usage limit beyond which enforcement action(volume offline/non-writable) is issued. | [optional] 
**pool_id** | **str** | ID of the pool where the folder resides. | 
**provisioned_limit_size_bytes** | **int** | Limit on the provisioned size of volumes in a folder. If provisioned_limit_size_bytes is not specified when a folder is created, or if provisioned_limit_size_bytes is set to -1, then the folder has no provisioned size limit. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


