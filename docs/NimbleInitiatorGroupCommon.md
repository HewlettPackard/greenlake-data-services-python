# NimbleInitiatorGroupCommon

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int** | Time when this initiator group was created. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**description** | **str** | Text description of initiator group. String of up to 255 printable ASCII characters. | [optional] 
**fc_initiators** | [**list[NimbleFCInitiator]**](NimbleFCInitiator.md) | List of FC initiators. When create/update fc_initiators, wwpn is required. List of Fibre Channel initiators. | [optional] 
**fc_sessions** | [**list[NimbleFCSessionDetails]**](NimbleFCSessionDetails.md) | List of FC sessions. | [optional] 
**fc_tdz_ports** | [**list[NimbleFCTdzPorts]**](NimbleFCTdzPorts.md) | List of target Fibre Channel ports with Target Driven Zoning configured on this initiator group. | [optional] 
**full_name** | **str** | Initiator group&#39;s full name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**generation** | **int** | generation | [optional] 
**iscsi_initiators** | [**list[NimbleISCSIInitiator]**](NimbleISCSIInitiator.md) | List of ISCSI initiators. When create/update iscsi_initiators, either iqn or ip_address is always required with label. | [optional] 
**last_modified** | **int** | Time when this initiator group was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**metadata** | [**list[NimbleMetadata]**](NimbleMetadata.md) | Key-value pairs that augment an initiator group&#39;s attributes. | [optional] 
**num_connections** | **int** | Total number of connections from initiators in the initiator group. | [optional] 
**resource_uri** | **str** |  | [optional] 
**sc_host_id** | **str** | Host Service Host Id | [optional] 
**search_name** | **str** | Initiator group name used for search. Alphanumeric string, up to 64 characters including hyphen, period, colon. | [optional] 
**target_subnets** | [**list[NimbleTargetSubnets]**](NimbleTargetSubnets.md) | List of target subnet labels. If specified, discovery and access to volumes will be restricted to the specified subnets. List of target subnet tables. | [optional] 
**type** | **str** | type | [optional] 
**volume_count** | **int** | Number of volumes that are accessible by the initiator group. | [optional] 
**volume_list** | [**list[NimbleVolList]**](NimbleVolList.md) | List of volumes that are accessible by the initiator group. List of volumes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


