# DiskFilterableFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | ID of array the disk belongs to. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**array_name** | **str** | Name of array the disk belongs to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  &#x60;Filter, Sort&#x60; | [optional] 
**device_type** | **str** | Type of disk (HDD, SSD, N/A). Disk type. Possible values: &#39;hdd&#39;, &#39;ssd&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier of disk. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**model** | **str** | Disk model name. &#x60;Filter, Sort&#x60; | [optional] 
**serial** | **str** | Disk serial number(N/A if empty). &#x60;Filter, Sort&#x60; | [optional] 
**shelf_id** | **str** | Identifies the physical shelf the disk belongs to. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**shelf_serial** | **str** | Serial number of the shelf the disk is attached to. &#x60;Filter, Sort&#x60; | [optional] 
**state** | **str** | Disk hardware state. Disk state. Possible values: &#39;valid&#39;, &#39;in use&#39;, &#39;failed&#39;, absent&#39;, &#39;removed&#39;, &#39;void&#39;, &#39;t_fail&#39;, &#39;foreign&#39;. &#x60;Filter, Sort&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


