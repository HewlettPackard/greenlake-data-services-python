# NimbleFibreChannelInterfaceDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_name_or_serial** | **str** | Name or serial number of array where the interface is hosted. | [optional] 
**bus_location** | **str** | PCI bus location of the HBA for this Fibre Channel port. | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**fabric_info** | [**NimbleFibreChannelFabricInfo**](NimbleFibreChannelFabricInfo.md) | Fibre Channel fabric information. | [optional] 
**fc_port_name** | **str** | Name of Fibre Channel port. | [optional] 
**firmware_version** | **str** | Version of the Fibre Channel firmware. | [optional] 
**generation** | **int** | generation | [optional] 
**link_info** | [**NimbleFibreChannelLinkInfo**](NimbleFibreChannelLinkInfo.md) | Information about the Fibre Channel link at which interface is operating. | [optional] 
**logical_port_number** | **int** | Logical port number for the Fibre Channel port. | [optional] 
**online** | **bool** | Identify whether the Fibre Channel interface is online. | [optional] 
**orientation** | **str** | Orientation of FC ports on a HBA. An orientation of &#39;right_to_left&#39; indicates that ports are ordered as 3,2,1,0 on the slot. Possible values: &#39;left_to_right&#39;, &#39;right_to_left&#39;. | [optional] 
**partial_response_ok** | **bool** | Port response. | [optional] 
**peerzone** | **str** | Active peer zone for this Fibre Channel interface. | [optional] 
**port** | **int** | HBA port number for this Fibre Channel port. | [optional] 
**slot** | **int** | HBA slot number for this Fibre Channel port. | [optional] 
**type** | **str** | type | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


