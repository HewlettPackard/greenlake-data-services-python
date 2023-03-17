# NimbleNsShelfCtrlr

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cached_serial** | **str** | CachedSerial - Cached serial. | [optional] 
**ctrlr_attrset_list** | [**list[NimbleNsShelfCtrlrAttrSet]**](NimbleNsShelfCtrlrAttrSet.md) | List of ctrlr attribute set for each logical controller. | [optional] 
**ctrlr_hw_model** | **str** | Controller hardware model. Possible values:&#39;head_x9&#39;, &#39;head_x8&#39;, &#39;head_gen5_2u&#39;, &#39;es2_4u&#39;, &#39;head_vmware&#39;, &#39;es1_3u&#39;, &#39;head_x9_2u&#39;, &#39;head_x10&#39;, &#39;head_gen5&#39;, &#39;es3_4u&#39;, &#39;unknown&#39;. | [optional] 
**ctrlr_sensor_last_run** | **int** | The time of last valid sensor reading, in epoch seconds. | [optional] 
**ctrlr_sensors** | [**list[NimbleNsShelfSensor]**](NimbleNsShelfSensor.md) | The list of individual sensor reading in this controller. | [optional] 
**ctrlr_side** | **str** | Position of this controller in the chassis. Possible values:&#39;A&#39;, &#39;B&#39;, &#39;unknown&#39;. | [optional] 
**enc_loc_id** | **int** | Location ID based on SAS topology. | [optional] 
**exp_sas_addr** | **str** | Expander SAS address. | [optional] 
**extra_attributes** | **list[str]** | Extra attributes as attribute value pairs. | [optional] 
**fan_overall_status** | **str** | The overall status for the fans on this controller. Possible values:&#39;Missing&#39;, &#39;Failed&#39;, &#39;OK&#39;, &#39;Alerted&#39;. | [optional] 
**hw_master_state** | **str** | SES device hardware mastership state. Possible values:&#39;not master&#39;, &#39;failed&#39;, &#39;unknown&#39;, &#39;master&#39;. | [optional] 
**hw_mship_failure** | **bool** | SES device hardware mastership failure. | [optional] 
**identify_status** | **bool** | Status of chassis identifier. | [optional] 
**port_info** | [**list[NimbleNsShelfPortInfo]**](NimbleNsShelfPortInfo.md) | Port info for each SAS port. | [optional] 
**psu_overall_status** | **str** | The overall status for the PSU on this controller.. Possible values: &#39;OK&#39;, &#39;Alerted&#39;, &#39;Failed&#39;, &#39;Missing&#39;. | [optional] 
**sw_master_state** | **str** | SES device software mastership state. Possible values:&#39;not master&#39;, &#39;want master&#39;, &#39;unknown&#39;, &#39;master&#39;, &#39;release master&#39;. | [optional] 
**temp_overall_status** | **str** | The overall status for the temperature of this controller.  Possible values:&#39;Missing&#39;, &#39;Failed&#39;, &#39;OK&#39;, &#39;Alerted&#39;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


