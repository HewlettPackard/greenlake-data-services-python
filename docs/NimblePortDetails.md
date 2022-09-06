# NimblePortDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str, none_type** | Identifier for the array. A 42 digit hexadecimal number. | [optional] 
**array_name_or_serial** | **str, none_type** | Name or serial number of array where the interface is hosted. | [optional] 
**bus_location** | **str, none_type** | PCI bus location of the HBA for this Fibre Channel port. | [optional] 
**controller_id** | **str, none_type** | Identifier of the controller where the interface is hosted. A 42 digit hexadecimal number. | [optional] 
**controller_name** | **str, none_type** | Name (A or B) of the controller where the interface is hosted. Plain string. | [optional] 
**fabric_info** | **bool, date, datetime, dict, float, int, list, str, none_type** | Fibre Channel fabric information. | [optional] 
**fc_port_id** | **str, none_type** | ID of the port with which the interface is associated. | [optional] 
**fc_port_name** | **str, none_type** | Name of Fibre Channel port. | [optional] 
**firmware_version** | **str, none_type** | Version of the Fibre Channel firmware. | [optional] 
**id** | **str, none_type** | Identifier for the interface. A 42 digit hexadecimal number. | [optional] 
**ip_list** | **bool, date, datetime, dict, float, int, list, str, none_type** | Information about the Fibre Channel link at which interface is operating. | [optional] 
**is_present** | **bool, none_type** | Whether this interface is present on this controller. Possible values: true, false. | [optional] 
**link_info** | **bool, date, datetime, dict, float, int, list, str, none_type** | Information about the Fibre Channel link at which interface is operating. | [optional] 
**link_speed** | **str, none_type** | Speed of the link. Possible values: link_speed_unknown, link_speed_10M, link_speed_100M, link_speed_1000M, link_speed_10000M. | [optional] 
**link_status** | **str, none_type** | Status of the link. Possible values: link_status_unknown, link_status_down, link_status_up. | [optional] 
**logical_port_number** | **int, none_type** | Logical port number for the Fibre Channel port. | [optional] 
**mac** | **str, none_type** | MAC address of the interface. Mac address of an interface. | [optional] 
**max_link_speed** | **str, none_type** | Maximum speed of the link. Possible values: link_speed_unknown, link_speed_10M, link_speed_100M, link_speed_1000M, link_speed_10000M. | [optional] 
**mtu** | **int, none_type** | MTU on the link. | [optional] 
**name** | **str, none_type** | Name of the interface. | [optional] 
**nic_type** | **str, none_type** | Interface type. Possible values: nic_type_unknown, nic_type_tp, nic_type_sfp. | [optional] 
**online** | **bool, none_type** | Identify whether the Fibre Channel interface is online. | [optional] 
**orientation** | **str, none_type** | Orientation of FC ports on a HBA. An orientation of &#39;right_to_left&#39; indicates that ports are ordered as 3,2,1,0 on the slot. Possible values: &#39;left_to_right&#39;, &#39;right_to_left&#39;. | [optional] 
**partial_response_ok** | **bool, none_type** | Port response. | [optional] 
**peerzone** | **str, none_type** | Active peer zone for this Fibre Channel interface. | [optional] 
**port** | **int, none_type** | Port number for this interface. | [optional] 
**slot** | **int, none_type** | Slot number for this interface. | [optional] 
**wwnn** | **str, none_type** | World Wide Node Name for this Fibre Channel interface. | [optional] 
**wwpn** | **str, none_type** | World Wide Port Name for this Fibre Channel interface. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


