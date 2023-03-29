# NimbleControllerListItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str, none_type** | Rest ID of the array containing this controller. &#x60;Filter, Sort&#x60; | [optional] 
**array_name** | **str, none_type** | Name of the array containing this controller. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str, none_type** | Identifier of the controller. &#x60;Filter&#x60; | [optional] 
**name** | **str, none_type** | Name of the controller. &#x60;Filter, Sort&#x60; | [optional] 
**serial** | **str, none_type** | Serial number for this controller. &#x60;Filter, Sort&#x60; | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**asup_time** | **int, none_type** | Time of the last autosupport by the controller. | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**ctrlr_side** | **str, none_type** | Identifies which controller this is on its array. Possible values: &#39;A&#39;, &#39;B&#39;. | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**fan_status** | **str, none_type** | Overall fan status for the controller. Possible values: &#39;fan_failed&#39;, &#39;fan_okay&#39;, &#39;fan_alerted&#39;, &#39;fan_unknown&#39;. | [optional] 
**fans** | [**[NimbleNsCtrlrHwSensorInfo], none_type**](NimbleNsCtrlrHwSensorInfo.md) | Status for each fan in the controller. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**hostname** | **str, none_type** | Host name for the controller. | [optional] 
**nvme_cards** | [**[NimbleNsCtrlrNvmeCard], none_type**](NimbleNsCtrlrNvmeCard.md) | List of NVMe accelerator cards. | [optional] 
**nvme_cards_enabled** | **int, none_type** | Indicates if the NVMe accelerator card is enabled. | [optional] 
**partial_response_ok** | **bool, none_type** | Indicate that it is ok to provide partially available response. | [optional] 
**partition_status** | [**[NimbleNsCtrlrRaidInfo], none_type**](NimbleNsCtrlrRaidInfo.md) | Status of the system&#39;s raid partitions. | [optional] 
**power_status** | **str, none_type** | Overall power supply status for the controller. Possible values: &#39;ps_alerted&#39;, &#39;ps_okay&#39;, &#39;ps_failed&#39;, &#39;ps_unknown&#39;. | [optional] 
**power_supplies** | [**[NimbleNsCtrlrHwSensorInfo], none_type**](NimbleNsCtrlrHwSensorInfo.md) | Status for each power supply in the controller. | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**state** | **str, none_type** | Indicates whether this controller is active or not. Possible values: &#39;start_active&#39;, &#39;start_standby&#39;, &#39;stale&#39;, &#39;standby&#39;, &#39;active&#39;, &#39;solo&#39;, &#39;none&#39;. | [optional] 
**support_address** | **str, none_type** | IP address used for support. | [optional] 
**support_netmask** | **str, none_type** | IP netmask used for support. | [optional] 
**support_nic** | **str, none_type** | Network card used for support. | [optional] 
**temperature_sensors** | [**[NimbleNsCtrlrHwSensorInfo], none_type**](NimbleNsCtrlrHwSensorInfo.md) | Status for temperature sensor in the controller. | [optional] 
**temperature_status** | **str, none_type** | Overall temperature status for the controller. Possible values: &#39;temperature_unknown&#39;, &#39;temperature_alerted&#39;, &#39;temperature_okay&#39;, &#39;temperature_fail&#39;. | [optional] 
**type** | **str, none_type** | type | [optional] 
**update_end_time** | **int, none_type** | End time of last update. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**update_error_code** | **str, none_type** | If the software update has failed, this indicates the error code corresponding to the failure. Non-negative integer in range [0,9000]. | [optional] 
**update_progress_msg** | **str, none_type** | Group update detailed progress message. Plain string. | [optional] 
**update_start_time** | **int, none_type** | Start time of last update. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**update_state** | **str, none_type** | Group update state.Possible values: &#39;invalid&#39;, &#39;normal&#39;, &#39;updating&#39;, &#39;timed_out&#39;, &#39;failed&#39;, &#39;paused&#39;. | [optional] 
**version_current** | **str, none_type** | Version of software running on the group. | [optional] 
**version_rollback** | **str, none_type** | Rollback software version for the group. | [optional] 
**version_target** | **str, none_type** | Desired software version for the group. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


