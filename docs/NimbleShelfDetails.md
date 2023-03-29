# NimbleShelfDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**chassis_sensors** | [**[NimbleNsShelfSensor], none_type**](NimbleNsShelfSensor.md) | List of chassis sensor readings. | [optional] 
**chassis_type** | **str, none_type** | Chassis type. Possible values: &#39;chassis_unknown&#39;, &#39;chassis_3u16&#39;, &#39;chassis_4u24&#39;, &#39;chassis_nmbl_2u12&#39;, &#39;chassis_nmbl_4u24&#39; | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**ctrlrs** | [**[NimbleNsShelfCtrlr], none_type**](NimbleNsShelfCtrlr.md) | List of ctrlr info. | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**disk_sets** | [**[NimbleNsDiskSetAttr], none_type**](NimbleNsDiskSetAttr.md) | Attributes for the disk sets in this shelf. | [optional] 
**fan_overall_status** | **str, none_type** | The overall status for the fans on both controllers. Possible values: &#39;OK&#39;, &#39;Alerted&#39;, &#39;Failed&#39;, &#39;Missing&#39;. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**model_ext** | **str, none_type** | Extended model of the shelf or head unit. | [optional] 
**psu_overall_status** | **str, none_type** | The overall status for the PSUs. Possible values: &#39;OK&#39;, &#39;Alerted&#39;, &#39;Failed&#39;, &#39;Missing&#39;. | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**temp_overall_status** | **str, none_type** | The overall status for the temperature on both controllers. Possible values: &#39;OK&#39;, &#39;Alerted&#39;, &#39;Failed&#39;, &#39;Missing&#39;. | [optional] 
**type** | **str, none_type** | type | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


