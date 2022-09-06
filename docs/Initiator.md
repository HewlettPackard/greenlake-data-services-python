# Initiator


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str, none_type** | Address of the initiator. &#x60;Filter&#x60; | [optional] 
**associated_links** | [**ScAssociatedLinks**](ScAssociatedLinks.md) |  | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**driver_version** | **str, none_type** | Driver version of the host initiator. | [optional] 
**firmware_version** | **str, none_type** | Firmware version of the host initiator. | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**hba_model** | **str, none_type** | Host bus adaptor model of the host initiator | [optional] 
**host_speed** | **int, none_type** | Host speed | [optional] 
**hosts** | [**[HostSummaryForInitiatorObject], none_type**](HostSummaryForInitiatorObject.md) | List of hosts. &#x60;Filter&#x60; by hostId. | [optional] 
**id** | **str, none_type** | Identifier for an initiator. &#x60;Filter&#x60; | [optional] 
**ip_address** | **str, none_type** | IP address of the initiator. | [optional] 
**name** | **str, none_type** | Name of the initiator. &#x60;Filter, Sort&#x60; | [optional] 
**protocol** | **str, none_type** | protocol supported are : FC ,iSCSI or NVMe | [optional] 
**systems** | **[str, none_type], none_type** | system IDs to which the host initiator is linked to. &#x60;Filter&#x60; | [optional] 
**type** | **str** | The type of resource. | [optional] 
**vendor** | **str, none_type** | Vendor of the host initiator | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


