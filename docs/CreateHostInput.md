# CreateHostInput


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Name of the host. | 
**operating_system** | **str, none_type** | Host operating system. Possible Values are: - AIX - Apple - Citrix Hypervisor(XenServer) - HP-UX - IBM VIO Server - InForm - NetApp/ONTAP - OE Linux UEK - OpenVMS - Oracle VM x86 - RHE Linux - RHE Virtualization - Solaris - SuSE Linux - SuSE Virtualization - Ubuntu - VMware (ESXi) - Windows Server | 
**user_created** | **bool, none_type** | Indicates whether user created host or discovered host | 
**comment** | **str, none_type** | Comment | [optional] 
**contact** | **str, none_type** | Contact information | [optional] 
**fqdn** | **str, none_type** | Fully qualified domain name of the host. | [optional] 
**host_group_ids** | **[str, none_type], none_type** | List of hostgroup IDs | [optional] 
**initiator_ids** | **[str, none_type], none_type** | List of ids of existing initiators | [optional] 
**initiators_to_create** | [**[InitiatorInput], none_type**](InitiatorInput.md) | List of initiators to be created and added to this host | [optional] 
**ip_address** | **str, none_type** | IP address of the host. | [optional] 
**location** | **str, none_type** | location. | [optional] 
**model** | **str, none_type** | Model | [optional] 
**persona** | **str, none_type** | Host persona details. | [optional] 
**protocol** | **str, none_type** | protocol | [optional] 
**subnet** | **str, none_type** | subnet. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


