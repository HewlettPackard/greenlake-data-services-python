# NimbleNsShelfCtrlr


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cached_serial** | **str, none_type** | CachedSerial - Cached serial. | [optional] 
**ctrlr_attrset_list** | [**[NimbleNsShelfCtrlrAttrSet], none_type**](NimbleNsShelfCtrlrAttrSet.md) | List of ctrlr attribute set for each logical controller. | [optional] 
**ctrlr_hw_model** | **str, none_type** | Controller hardware model. Possible values:&#39;head_x9&#39;, &#39;head_x8&#39;, &#39;head_gen5_2u&#39;, &#39;es2_4u&#39;, &#39;head_vmware&#39;, &#39;es1_3u&#39;, &#39;head_x9_2u&#39;, &#39;head_x10&#39;, &#39;head_gen5&#39;, &#39;es3_4u&#39;, &#39;unknown&#39;. | [optional] 
**ctrlr_sensor_last_run** | **int, none_type** | The time of last valid sensor reading, in epoch seconds. | [optional] 
**ctrlr_sensors** | [**[NimbleNsShelfSensor], none_type**](NimbleNsShelfSensor.md) | The list of individual sensor reading in this controller. | [optional] 
**ctrlr_side** | **str, none_type** | Position of this controller in the chassis. Possible values:&#39;A&#39;, &#39;B&#39;, &#39;unknown&#39;. | [optional] 
**enc_loc_id** | **int, none_type** | Location ID based on SAS topology. | [optional] 
**exp_sas_addr** | **str, none_type** | Expander SAS address. | [optional] 
**extra_attributes** | **[str, none_type], none_type** | Extra attributes as attribute value pairs. | [optional] 
**fan_overall_status** | **str, none_type** | The overall status for the fans on this controller. Possible values:&#39;Missing&#39;, &#39;Failed&#39;, &#39;OK&#39;, &#39;Alerted&#39;. | [optional] 
**hw_master_state** | **str, none_type** | SES device hardware mastership state. Possible values:&#39;not master&#39;, &#39;failed&#39;, &#39;unknown&#39;, &#39;master&#39;. | [optional] 
**hw_mship_failure** | **bool, none_type** | SES device hardware mastership failure. | [optional] 
**identify_status** | **bool, none_type** | Status of chassis identifier. | [optional] 
**port_info** | [**[NimbleNsShelfPortInfo], none_type**](NimbleNsShelfPortInfo.md) | Port info for each SAS port. | [optional] 
**psu_overall_status** | **str, none_type** | The overall status for the PSU on this controller.. Possible values: &#39;OK&#39;, &#39;Alerted&#39;, &#39;Failed&#39;, &#39;Missing&#39;. | [optional] 
**sw_master_state** | **str, none_type** | SES device software mastership state. Possible values:&#39;not master&#39;, &#39;want master&#39;, &#39;unknown&#39;, &#39;master&#39;, &#39;release master&#39;. | [optional] 
**temp_overall_status** | **str, none_type** | The overall status for the temperature of this controller.  Possible values:&#39;Missing&#39;, &#39;Failed&#39;, &#39;OK&#39;, &#39;Alerted&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


