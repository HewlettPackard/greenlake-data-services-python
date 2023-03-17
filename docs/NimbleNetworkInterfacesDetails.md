# NimbleNetworkInterfacesDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str** | Identifier for the array. A 42 digit hexadecimal number. | [optional] 
**array_name_or_serial** | **str** | Name or serial of the array where the interface is hosted.String of up to 64 alphanumeric characters. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**controller_id** | **str** | Identifier of the controller where the interface is hosted. A 42 digit hexadecimal number. | [optional] 
**controller_name** | **str** | Name (A or B) of the controller where the interface is hosted. Plain string. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Identifier for the array. A 42 digit hexadecimal number. | [optional] 
**ip_list** | [**list[NimbleNetworkIP]**](NimbleNetworkIP.md) | List of IP addresses assigned to this network interface. List of IP address assignment details to network interface. | [optional] 
**is_present** | **bool** | Whether this interface is present on this controller. Possible values : true, false. | [optional] 
**link_speed** | **str** | Speed of the link. Possible values: link_speed_unknown, link_speed_10M,link_speed_100M, link_speed_1000M, link_speed_10000M.. | [optional] 
**link_status** | **str** | Status of the link. Possible values: link_status_unknown,link_status_down, link_status_up | [optional] 
**mac** | **str** | MAC address of the interface. Mac address of an interface. | [optional] 
**max_link_speed** | **str** | Maximum speed of the link. Possible values: &#39;link_speed_unknown&#39;, &#39;link_speed_10M&#39;,&#39;link_speed_100M&#39;, &#39;link_speed_1000M&#39;, &#39;link_speed_10000M&#39;, &#39;link_speed_25000M&#39;,&#39;link_speed_40000M&#39;, &#39;link_speed_50000M&#39;, &#39;link_speed_100000M&#39;. | [optional] 
**mtu** | **int** | MTU on the link. Unsigned 64-bit integer. | [optional] 
**name** | **str** | Name of the interface. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**nic_type** | **str** | Interface type. Possible values: nic_type_unknown, nic_type_tp, nic_type_sfp | [optional] 
**port** | **int** | Port number for this interface.Unsigned 64-bit integer. | [optional] 
**resource_uri** | **str** |  | [optional] 
**slot** | **int** | Slot number for this interface. Unsigned 64-bit integer. | [optional] 
**type** | **str** | type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


