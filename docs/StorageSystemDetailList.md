# StorageSystemDetailList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_list** | [**[NimbleArraySummary], none_type**](NimbleArraySummary.md) | The list of Nimble arrays part of this system. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**callhome_status** | **str** | Device Call-home connectivity status. | [optional] 
**collection_status** | [**CollectionStatus**](CollectionStatus.md) |  | [optional] 
**connection_status** | [**ConnectionStatus**](ConnectionStatus.md) |  | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**description** | **str, none_type** | A brief description of the storage system. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**id** | **str, none_type** | UUID string uniquely identifying the storage system object. | [optional] 
**last_connected_time** | **int, none_type** | Last time when the system was connected | [optional] 
**mgmt_ip** | [**Ips**](Ips.md) |  | [optional] 
**model** | **str, none_type** | Model of the storage system &#x60;Filter, Sort&#x60; | [optional] 
**name** | **str, none_type** | A name to identify the storage system. &#x60;Filter, Sort&#x60; | [optional] 
**product_family** | **str** | Storage device type | [optional] 
**resource_uri** | **str, none_type** | resourceUri for detailed storage object | [optional] 
**software_version** | **str, none_type** | Software version of the storage system &#x60;Filter, Sort&#x60; | [optional] 
**state** | **str** | For deviceType1 State derived from ports, enclosure, disk and node state for deviceType2 state is state reported by deviceType2 array &#x60;Filter, Sort&#x60; | [optional] 
**system_wwn** | **str, none_type** | WWN of the array | [optional] 
**tier_type** | **str, none_type** | StorageTier. | [optional] 
**type** | **str, none_type** | type | [optional] 
**up_since** | **int, none_type** | The time that the system has been up since | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


