# DiskFilterableFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str, none_type** | ID of array the disk belongs to. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**array_name** | **str, none_type** | Name of array the disk belongs to. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.  &#x60;Filter, Sort&#x60; | [optional] 
**device_type** | **str, none_type** | Type of disk (HDD, SSD, N/A). Disk type. Possible values: &#39;hdd&#39;, &#39;ssd&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str, none_type** | Identifier of disk. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**model** | **str, none_type** | Disk model name. &#x60;Filter, Sort&#x60; | [optional] 
**serial** | **str, none_type** | Disk serial number(N/A if empty). &#x60;Filter, Sort&#x60; | [optional] 
**shelf_id** | **str, none_type** | Identifies the physical shelf the disk belongs to. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**shelf_serial** | **str, none_type** | Serial number of the shelf the disk is attached to. &#x60;Filter, Sort&#x60; | [optional] 
**state** | **str, none_type** | Disk hardware state. Disk state. Possible values: &#39;valid&#39;, &#39;in use&#39;, &#39;failed&#39;, absent&#39;, &#39;removed&#39;, &#39;void&#39;, &#39;t_fail&#39;, &#39;foreign&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


