# HostDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**ScAssociatedLinks**](ScAssociatedLinks.md) |  | [optional] 
**associated_systems** | **list[str]** | system IDs to which the host belongs to. | [optional] 
**comment** | **str** | Comment | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**contact** | **str** | Contact information | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**edit_status** | **str** | Host Update or Delete progress status. Possible status are: Update_In_Progress,Update_Success,Update_Failed,Delete_In_Progress,Delete_Failed,Not_Applicable. | [optional] 
**fqdn** | **str** | Fully qualified domain name of the host. | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**host_groups** | [**list[HostGroupSummaryObject]**](HostGroupSummaryObject.md) | Host group to which the host belongs to | [optional] 
**id** | **str** | Identifier for host. | [optional] 
**initiators** | [**list[InitiatorSummary]**](InitiatorSummary.md) | Host initiator list this host is associated with. | [optional] 
**ip_address** | **str** | IP address of the host. | [optional] 
**location** | **str** | location. | [optional] 
**marked_for_delete** | **bool** | Indicates whether host group is marked for deletion or not | [optional] 
**model** | **str** | Model | [optional] 
**name** | **str** | Name of the host. | [optional] 
**operating_system** | **str** | Host operating system. | [optional] 
**persona** | **str** | Host persona details. | [optional] 
**protocol** | **str** | protocol supported are : FC ,iSCSI or NVMe | [optional] 
**request_uri** | **str** | requestUri for host initiators | [optional] 
**subnet** | **str** | subnet. | [optional] 
**systems** | **list[str]** | system IDs to which the host belongs to | [optional] 
**type** | **str** | The type of resource. | [optional] 
**user_created** | **bool** | Indicates whether user created host or discovered host | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


