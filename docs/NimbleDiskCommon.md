# NimbleDiskCommon


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**bank** | **int, none_type** | Disk bank number. | [optional] 
**block_type** | **str, none_type** | Native block type of the disk. Possible values: &#39;block_512e&#39;, &#39;block_4Kn&#39;, &#39;block_none&#39;, &#39;block_512n&#39;. | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**disk_internal_stat1** | **str, none_type** | Internal disk statistic 1. | [optional] 
**firmware_version** | **str, none_type** | Firmware version on the disk. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**hba** | **int, none_type** | HBA ID the disk is connected to. | [optional] 
**is_dfc** | **bool, none_type** | Is disk part of dual flash carrier. | [optional] 
**path** | **str, none_type** | Disk SCSI device path. | [optional] 
**port** | **int, none_type** | HBA port number the disk is connected to. | [optional] 
**raid_id** | **int, none_type** | Raid ID. | [optional] 
**raid_resync_average_speed** | **int, none_type** | Average RAID rebuild speed (bytes/sec). | [optional] 
**raid_resync_current_speed** | **int, none_type** | Current RAID rebuild speed (bytes/sec). | [optional] 
**raid_resync_percent** | **int, none_type** | Percentage RAID rebuild completed on this disk. | [optional] 
**raid_state** | **str, none_type** | RAID status for the disk (N/A, okay, resynchronizing, spare, faulty). Disk RAID state. Possible values: &#39;N/A&#39;, &#39;okay&#39;, &#39;resynchronizing&#39;, &#39;spare&#39;, &#39;faulty&#39;. | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**shelf_location** | **str, none_type** | Identifies the controller, port, and chain position of the shelf the disk belongs to. | [optional] 
**shelf_location_id** | **int, none_type** | Identifies the position shelf the disk belongs to, as coded integer. | [optional] 
**size** | **int, none_type** | Disk size in bytes. | [optional] 
**slot** | **int, none_type** | Disk slot number. | [optional] 
**smart_attribute_list** | [**[NimbleDiskSmartAttributes], none_type**](NimbleDiskSmartAttributes.md) | S.M.A.R.T. attributes for the disk. List of Smart attributes. | [optional] 
**type** | **str, none_type** | type | [optional] 
**vendor** | **str, none_type** | Vendor name of the disk manufacturer. | [optional] 
**vshelf_id** | **int, none_type** | Identifies the local shelf id the disk belongs to. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


