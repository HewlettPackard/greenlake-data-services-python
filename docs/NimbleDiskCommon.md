# NimbleDiskCommon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**bank** | **int** | Disk bank number. | [optional] 
**block_type** | **str** | Native block type of the disk. Possible values: &#39;block_512e&#39;, &#39;block_4Kn&#39;, &#39;block_none&#39;, &#39;block_512n&#39;. | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**disk_internal_stat1** | **str** | Internal disk statistic 1. | [optional] 
**firmware_version** | **str** | Firmware version on the disk. | [optional] 
**generation** | **int** | generation | [optional] 
**hba** | **int** | HBA ID the disk is connected to. | [optional] 
**is_dfc** | **bool** | Is disk part of dual flash carrier. | [optional] 
**path** | **str** | Disk SCSI device path. | [optional] 
**port** | **int** | HBA port number the disk is connected to. | [optional] 
**raid_id** | **int** | Raid ID. | [optional] 
**raid_resync_average_speed** | **int** | Average RAID rebuild speed (bytes/sec). | [optional] 
**raid_resync_current_speed** | **int** | Current RAID rebuild speed (bytes/sec). | [optional] 
**raid_resync_percent** | **int** | Percentage RAID rebuild completed on this disk. | [optional] 
**raid_state** | **str** | RAID status for the disk (N/A, okay, resynchronizing, spare, faulty). Disk RAID state. Possible values: &#39;N/A&#39;, &#39;okay&#39;, &#39;resynchronizing&#39;, &#39;spare&#39;, &#39;faulty&#39;. | [optional] 
**resource_uri** | **str** |  | [optional] 
**shelf_location** | **str** | Identifies the controller, port, and chain position of the shelf the disk belongs to. | [optional] 
**shelf_location_id** | **int** | Identifies the position shelf the disk belongs to, as coded integer. | [optional] 
**size** | **int** | Disk size in bytes. | [optional] 
**slot** | **int** | Disk slot number. | [optional] 
**smart_attribute_list** | [**list[NimbleDiskSmartAttributes]**](NimbleDiskSmartAttributes.md) | S.M.A.R.T. attributes for the disk. List of Smart attributes. | [optional] 
**type** | **str** | type | [optional] 
**vendor** | **str** | Vendor name of the disk manufacturer. | [optional] 
**vshelf_id** | **int** | Identifies the local shelf id the disk belongs to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


