# NimblePortDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | Identifier for the array. A 42 digit hexadecimal number. | [optional] 
**array_name_or_serial** | **str** | Name or serial number of array where the interface is hosted. | [optional] 
**bus_location** | **str** | PCI bus location of the HBA for this Fibre Channel port. | [optional] 
**controller_id** | **str** | Identifier of the controller where the interface is hosted. A 42 digit hexadecimal number. | [optional] 
**controller_name** | **str** | Name (A or B) of the controller where the interface is hosted. Plain string. | [optional] 
**fabric_info** | [**NimbleFibreChannelFabricInfo**](NimbleFibreChannelFabricInfo.md) | Fibre Channel fabric information. | [optional] 
**fc_port_id** | **str** | ID of the port with which the interface is associated. | [optional] 
**fc_port_name** | **str** | Name of Fibre Channel port. | [optional] 
**firmware_version** | **str** | Version of the Fibre Channel firmware. | [optional] 
**id** | **str** | Identifier for the interface. A 42 digit hexadecimal number. | [optional] 
**ip_list** | [**IpListInfo**](IpListInfo.md) | Information about the Fibre Channel link at which interface is operating. | [optional] 
**is_present** | **bool** | Whether this interface is present on this controller. Possible values: true, false. | [optional] 
**link_info** | [**NimbleFibreChannelLinkInfo**](NimbleFibreChannelLinkInfo.md) | Information about the Fibre Channel link at which interface is operating. | [optional] 
**link_speed** | **str** | Speed of the link. Possible values: link_speed_unknown, link_speed_10M, link_speed_100M, link_speed_1000M, link_speed_10000M. | [optional] 
**link_status** | **str** | Status of the link. Possible values: link_status_unknown, link_status_down, link_status_up. | [optional] 
**logical_port_number** | **int** | Logical port number for the Fibre Channel port. | [optional] 
**mac** | **str** | MAC address of the interface. Mac address of an interface. | [optional] 
**max_link_speed** | **str** | Maximum speed of the link. Possible values: link_speed_unknown, link_speed_10M, link_speed_100M, link_speed_1000M, link_speed_10000M. | [optional] 
**mtu** | **int** | MTU on the link. | [optional] 
**name** | **str** | Name of the interface. | [optional] 
**nic_type** | **str** | Interface type. Possible values: nic_type_unknown, nic_type_tp, nic_type_sfp. | [optional] 
**online** | **bool** | Identify whether the Fibre Channel interface is online. | [optional] 
**orientation** | **str** | Orientation of FC ports on a HBA. An orientation of &#39;right_to_left&#39; indicates that ports are ordered as 3,2,1,0 on the slot. Possible values: &#39;left_to_right&#39;, &#39;right_to_left&#39;. | [optional] 
**partial_response_ok** | **bool** | Port response. | [optional] 
**peerzone** | **str** | Active peer zone for this Fibre Channel interface. | [optional] 
**port** | **int** | Port number for this interface. | [optional] 
**slot** | **int** | Slot number for this interface. | [optional] 
**wwnn** | **str** | World Wide Node Name for this Fibre Channel interface. | [optional] 
**wwpn** | **str** | World Wide Port Name for this Fibre Channel interface. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


