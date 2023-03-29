# VlunsList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool, none_type** | Indicates if this is an active VLUN or a template | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**device_wwns** | **str, none_type** | Device WWNs | [optional] 
**disk_partition** | **str, none_type** | Disk partition of host | [optional] 
**displayname** | **str, none_type** | SED state | [optional] 
**domain** | **str, none_type** | SED state | [optional] 
**failed_path_interval** | **int, none_type** | Monitoring interval in seconds after which the host checks for failed paths | [optional] 
**failed_path_policy** | **str, none_type** | Failed path monitoring method | [optional] 
**generation** | **int, none_type** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str, none_type** | uid of the vlun &#x60;Filter&#x60; | [optional] 
**initiators** | [**VlunsListInitiators**](VlunsListInitiators.md) |  | [optional] 
**lun** | **int, none_type** | Exported LUN ID &#x60;Filter, Sort&#x60; | [optional] 
**mount_point** | **str, none_type** | Mount points of devices | [optional] 
**mount_point_fsau** | **int, none_type** | File system allocation unit in MiB | [optional] 
**multi_path_type** | **str, none_type** | Multi-path method in use | [optional] 
**port_pos** | [**VlunsListPortPos**](VlunsListPortPos.md) |  | [optional] 
**raw_volume** | **str, none_type** | Volume that has not been formatted. Yes if it supports | [optional] 
**remote_name** | **str, none_type** | Host WWN, iSCSI name, or SAS address; depending on port type | [optional] 
**resource_uri** | **str, none_type** | resourceUri for detailed vlun object | [optional] 
**state** | [**VlunsListState**](VlunsListState.md) |  | [optional] 
**status** | **str, none_type** | SED state | [optional] 
**system_id** | **str, none_type** | System Uid &#x60;Filter, Sort&#x60; | [optional] 
**tpg_id** | **int, none_type** | SED state | [optional] 
**type** | **str, none_type** | type | [optional] 
**used_space** | **int, none_type** | Host devices used space in MiB | [optional] 
**vlun_type** | **str, none_type** | VLUN type | [optional] 
**volume_group** | **str, none_type** | Volume group info | [optional] 
**volume_manager** | **str, none_type** | Volume Manager tool used | [optional] 
**volume_name** | **str, none_type** | Name of exported virtual volume or volume set name &#x60;Filter, Sort&#x60; | [optional] 
**volume_wwn** | **str, none_type** | WWN of exported volume.If a volume set is exported, then this value is null. &#x60;Filter, Sort&#x60; | [optional] 
**vv_reserved_user_space** | **int, none_type** | Volume user reserved space in MiB | [optional] 
**vv_size** | **int, none_type** | Size of volume in MiB | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


