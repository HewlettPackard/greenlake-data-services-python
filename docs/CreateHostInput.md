# CreateHostInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Comment | [optional] 
**contact** | **str** | Contact information | [optional] 
**fqdn** | **str** | Fully qualified domain name of the host. | [optional] 
**host_group_ids** | **list[str]** | List of hostgroup IDs | [optional] 
**initiator_ids** | **list[str]** | List of ids of existing initiators | [optional] 
**initiators_to_create** | [**list[InitiatorInput]**](InitiatorInput.md) | List of initiators to be created and added to this host | [optional] 
**ip_address** | **str** | IP address of the host. | [optional] 
**location** | **str** | location. | [optional] 
**model** | **str** | Model | [optional] 
**name** | **str** | Name of the host. | 
**operating_system** | **str** | Host operating system. Possible Values are: - AIX - Apple - Citrix Hypervisor(XenServer) - HP-UX - IBM VIO Server - InForm - NetApp/ONTAP - OE Linux UEK - OpenVMS - Oracle VM x86 - RHE Linux - RHE Virtualization - Solaris - SuSE Linux - SuSE Virtualization - Ubuntu - VMware (ESXi) - Windows Server | 
**persona** | **str** | Host persona details. | [optional] 
**protocol** | **str** | protocol | [optional] 
**subnet** | **str** | subnet. | [optional] 
**user_created** | **bool** | Indicates whether user created host or discovered host | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


