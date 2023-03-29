# NimblePortsListFibreChannelInterfaceItemsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**controller_name** | **str, none_type** | Name (A or B) of the controller where the interface is hosted. Plain string. &#x60;Filter&#x60; | [optional] 
**fc_port_id** | **str, none_type** | ID of the port with which the interface is associated. &#x60;Filter&#x60; | [optional] 
**id** | **str, none_type** | Identifier for the interface. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str, none_type** | Name of the interface. &#x60;Filter, Sort&#x60; | [optional] 
**wwnn** | **str, none_type** | World Wide Node Name for this Fibre Channel interface. &#x60;Filter, Sort&#x60; | [optional] 
**wwpn** | **str, none_type** | World Wide Port Name for this Fibre Channel interface. &#x60;Filter, Sort&#x60; | [optional] 
**array_name_or_serial** | **str, none_type** | Name or serial number of array where the interface is hosted. | [optional] 
**bus_location** | **str, none_type** | PCI bus location of the HBA for this Fibre Channel port. | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**fabric_info** | [**NimbleFibreChannelInterfaceDetailsFabricInfo**](NimbleFibreChannelInterfaceDetailsFabricInfo.md) |  | [optional] 
**fc_port_name** | **str, none_type** | Name of Fibre Channel port. | [optional] 
**firmware_version** | **str, none_type** | Version of the Fibre Channel firmware. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**link_info** | [**NimbleFibreChannelInterfaceDetailsLinkInfo**](NimbleFibreChannelInterfaceDetailsLinkInfo.md) |  | [optional] 
**logical_port_number** | **int, none_type** | Logical port number for the Fibre Channel port. | [optional] 
**online** | **bool, none_type** | Identify whether the Fibre Channel interface is online. | [optional] 
**orientation** | **str, none_type** | Orientation of FC ports on a HBA. An orientation of &#39;right_to_left&#39; indicates that ports are ordered as 3,2,1,0 on the slot. Possible values: &#39;left_to_right&#39;, &#39;right_to_left&#39;. | [optional] 
**partial_response_ok** | **bool, none_type** | Port response. | [optional] 
**peerzone** | **str, none_type** | Active peer zone for this Fibre Channel interface. | [optional] 
**port** | **int, none_type** | HBA port number for this Fibre Channel port. | [optional] 
**slot** | **int, none_type** | HBA slot number for this Fibre Channel port. | [optional] 
**type** | **str, none_type** | type | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


