# VlunsListSingle


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool, none_type** | Indicates if this is an active VLUN or a template | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**device_wwns** | **str, none_type** | Device WWNs | [optional] 
**disk_partition** | **str, none_type** | Disk partition of host | [optional] 
**displayname** | **str, none_type** | SED state | [optional] 
**domain** | **str, none_type** | SED state | [optional] 
**failed_path_interval** | **int, none_type** | Monitoring interval in seconds after which the host checks for failed paths | [optional] 
**failed_path_policy** | **str, none_type** | Failed path monitoring method | [optional] 
**id** | **str, none_type** | uid of the vlun | [optional] 
**initiators** | [**VlunsListInitiators**](VlunsListInitiators.md) |  | [optional] 
**lun** | **int, none_type** | Exported LUN ID | [optional] 
**mount_point** | **str, none_type** | Mount points of devices | [optional] 
**mount_point_fsau** | **int, none_type** | File system allocation unit in MiB | [optional] 
**multi_path_type** | **str, none_type** | Multi-path method in use | [optional] 
**port_pos** | [**VlunsListSinglePortPos**](VlunsListSinglePortPos.md) |  | [optional] 
**raw_volume** | **str, none_type** | Volume that has not been formatted. Yes if it supports | [optional] 
**remote_name** | **str, none_type** | Host WWN, iSCSI name, or SAS address; depending on port type | [optional] 
**request_uri** | **str, none_type** | requestUri for detailed vlun object | [optional] 
**resource_uri** | **str, none_type** | resourceUri for detailed vlun object | [optional] 
**state** | [**VlunsListState**](VlunsListState.md) |  | [optional] 
**status** | **str, none_type** | SED state | [optional] 
**system_id** | **str, none_type** | SED state | [optional] 
**tpg_id** | **int, none_type** | SED state | [optional] 
**type** | **str, none_type** | VLUN type | [optional] 
**used_space** | **int, none_type** | Host devices used space in MiB | [optional] 
**volume_group** | **str, none_type** | Volume group info | [optional] 
**volume_manager** | **str, none_type** | Volume Manager tool used | [optional] 
**volume_name** | **str, none_type** | Name of exported virtual volume or volume set name | [optional] 
**volume_wwn** | **str, none_type** | WWN of exported volume.If a volume set is exported, then this value is null. | [optional] 
**vv_reserved_user_space** | **int, none_type** | Volume user reserved space in MiB | [optional] 
**vv_size** | **int, none_type** | Size of volume in MiB | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


