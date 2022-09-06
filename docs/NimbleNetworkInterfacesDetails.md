# NimbleNetworkInterfacesDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_id** | **str, none_type** | Identifier for the array. A 42 digit hexadecimal number. | [optional] 
**array_name_or_serial** | **str, none_type** | Name or serial of the array where the interface is hosted.String of up to 64 alphanumeric characters. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**controller_id** | **str, none_type** | Identifier of the controller where the interface is hosted. A 42 digit hexadecimal number. | [optional] 
**controller_name** | **str, none_type** | Name (A or B) of the controller where the interface is hosted. Plain string. | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**id** | **str, none_type** | Identifier for the array. A 42 digit hexadecimal number. | [optional] 
**ip_list** | [**[NimbleNetworkIP], none_type**](NimbleNetworkIP.md) | List of IP addresses assigned to this network interface. List of IP address assignment details to network interface. | [optional] 
**is_present** | **bool, none_type** | Whether this interface is present on this controller. Possible values : true, false. | [optional] 
**link_speed** | **str, none_type** | Speed of the link. Possible values: link_speed_unknown, link_speed_10M,link_speed_100M, link_speed_1000M, link_speed_10000M.. | [optional] 
**link_status** | **str, none_type** | Status of the link. Possible values: link_status_unknown,link_status_down, link_status_up | [optional] 
**mac** | **str, none_type** | MAC address of the interface. Mac address of an interface. | [optional] 
**max_link_speed** | **str, none_type** | Maximum speed of the link. Possible values: &#39;link_speed_unknown&#39;, &#39;link_speed_10M&#39;,&#39;link_speed_100M&#39;, &#39;link_speed_1000M&#39;, &#39;link_speed_10000M&#39;, &#39;link_speed_25000M&#39;,&#39;link_speed_40000M&#39;, &#39;link_speed_50000M&#39;, &#39;link_speed_100000M&#39;. | [optional] 
**mtu** | **int, none_type** | MTU on the link. Unsigned 64-bit integer. | [optional] 
**name** | **str, none_type** | Name of the interface. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**nic_type** | **str, none_type** | Interface type. Possible values: nic_type_unknown, nic_type_tp, nic_type_sfp | [optional] 
**port** | **int, none_type** | Port number for this interface.Unsigned 64-bit integer. | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**slot** | **int, none_type** | Slot number for this interface. Unsigned 64-bit integer. | [optional] 
**type** | **str, none_type** | type | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


