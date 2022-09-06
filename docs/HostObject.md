# HostObject


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**ScAssociatedLinks**](ScAssociatedLinks.md) |  | [optional] 
**associated_systems** | **[str, none_type], none_type** | system IDs to which the host belongs to. | [optional] 
**comment** | **str, none_type** | Comment | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**contact** | **str, none_type** | Contact information | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**edit_status** | **str, none_type** | Host Update or Delete progress status. Possible status are: Update_In_Progress,Update_Success,Update_Failed,Delete_In_Progress,Delete_Failed,Not_Applicable. &#x60;Filter&#x60; | [optional] 
**fqdn** | **str, none_type** | Fully qualified domain name of the host. | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**host_groups** | [**[HostGroupSummaryObject], none_type**](HostGroupSummaryObject.md) | Host group to which the host belongs to. &#x60;Filter&#x60; by hostGroupId. | [optional] 
**id** | **str, none_type** | Identifier for host. &#x60;Filter&#x60; | [optional] 
**initiators** | [**[InitiatorSummary], none_type**](InitiatorSummary.md) | Host initiator list this host is associated with. &#x60;Filter&#x60; by initiatorId. | [optional] 
**ip_address** | **str, none_type** | IP address of the host. | [optional] 
**location** | **str, none_type** | location. | [optional] 
**marked_for_delete** | **bool, none_type** | Indicates whether host is marked for deletion or not | [optional] 
**model** | **str, none_type** | Model | [optional] 
**name** | **str, none_type** | Name of the host. &#x60;Filter, Sort&#x60; | [optional] 
**operating_system** | **str, none_type** | Host operating system. &#x60;Filter&#x60; | [optional] 
**persona** | **str, none_type** | Host persona details. | [optional] 
**protocol** | **str, none_type** | protocol supported are : FC ,iSCSI or NVMe | [optional] 
**subnet** | **str, none_type** | subnet. | [optional] 
**systems** | **[str, none_type], none_type** | system IDs to which the host belongs to. &#x60;Filter&#x60; | [optional] 
**type** | **str** | The type of resource. | [optional] 
**user_created** | **bool, none_type** | Indicates whether user created host or discovered host | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


