# VlunsListSingle

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | Indicates if this is an active VLUN or a template | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**device_ww_ns** | **str** | Device WWNs | [optional] 
**disk_partition** | **str** | Disk partition of host | [optional] 
**displayname** | **str** | SED state | [optional] 
**domain** | **str** | SED state | [optional] 
**failed_path_interval** | **int** | Monitoring interval in seconds after which the host checks for failed paths | [optional] 
**failed_path_policy** | **str** | Failed path monitoring method | [optional] 
**id** | **str** | uid of the vlun | [optional] 
**initiators** | [**VlunsListInitiators**](VlunsListInitiators.md) |  | [optional] 
**lun** | **int** | Exported LUN ID | [optional] 
**mount_point** | **str** | Mount points of devices | [optional] 
**mount_point_fsau** | **int** | File system allocation unit in MiB | [optional] 
**multi_path_type** | **str** | Multi-path method in use | [optional] 
**port_pos** | [**VlunsListSinglePortPos**](VlunsListSinglePortPos.md) |  | [optional] 
**raw_volume** | **str** | Volume that has not been formatted. Yes if it supports | [optional] 
**remote_name** | **str** | Host WWN, iSCSI name, or SAS address; depending on port type | [optional] 
**request_uri** | **str** | requestUri for detailed vlun object | [optional] 
**resource_uri** | **str** | resourceUri for detailed vlun object | [optional] 
**state** | [**VlunsListState**](VlunsListState.md) |  | [optional] 
**status** | **str** | SED state | [optional] 
**system_id** | **str** | SED state | [optional] 
**tpg_id** | **int** | SED state | [optional] 
**type** | **str** | VLUN type | [optional] 
**used_space** | **int** | Host devices used space in MiB | [optional] 
**volume_group** | **str** | Volume group info | [optional] 
**volume_manager** | **str** | Volume Manager tool used | [optional] 
**volume_name** | **str** | Name of exported virtual volume or volume set name | [optional] 
**volume_wwn** | **str** | WWN of exported volume.If a volume set is exported, then this value is null. | [optional] 
**vv_reserved_user_space** | **int** | Volume user reserved space in MiB | [optional] 
**vv_size** | **int** | Size of volume in MiB | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


