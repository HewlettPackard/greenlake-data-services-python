# NimbleInitiatorGroupDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str, none_type** | requestUri for detailed initiator groups object | [optional] 
**access_protocol** | **str, none_type** | Initiator group access protocol. Possible values: &#39;iscsi&#39;, &#39;fc&#39;. | [optional] 
**app_uuid** | **str, none_type** | Application identifier of initiator group. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed | [optional] 
**host_type** | **str, none_type** | Initiator group host type. Available options are auto and hpux. The default option is auto. This attribute will be applied to all the initiators in the initiator group. Initiators with different host OSes should not be kept in the same initiator group having a non-default host type attribute. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**id** | **str, none_type** | Identifier for initiator group. A 42 digit hexadecimal number. | [optional] 
**name** | **str, none_type** | Name of initiator group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int, none_type** | Time when this initiator group was created. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**description** | **str, none_type** | Text description of initiator group. String of up to 255 printable ASCII characters. | [optional] 
**fc_initiators** | [**[NimbleFCInitiator], none_type**](NimbleFCInitiator.md) | List of FC initiators. When create/update fc_initiators, wwpn is required. List of Fibre Channel initiators. | [optional] 
**fc_sessions** | [**[NimbleFCSessionDetails], none_type**](NimbleFCSessionDetails.md) | List of FC sessions. | [optional] 
**fc_tdz_ports** | [**[NimbleFCTdzPorts], none_type**](NimbleFCTdzPorts.md) | List of target Fibre Channel ports with Target Driven Zoning configured on this initiator group. | [optional] 
**full_name** | **str, none_type** | Initiator group&#39;s full name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**iscsi_initiators** | [**[NimbleISCSIInitiator], none_type**](NimbleISCSIInitiator.md) | List of ISCSI initiators. When create/update iscsi_initiators, either iqn or ip_address is always required with label. | [optional] 
**last_modified** | **int, none_type** | Time when this initiator group was last modified. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**metadata** | [**[NimbleMetadata], none_type**](NimbleMetadata.md) | Key-value pairs that augment an initiator group&#39;s attributes. | [optional] 
**num_connections** | **int, none_type** | Total number of connections from initiators in the initiator group. | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**sc_host_id** | **str** | Host Service Host Id | [optional] 
**search_name** | **str, none_type** | Initiator group name used for search. Alphanumeric string, up to 64 characters including hyphen, period, colon. | [optional] 
**target_subnets** | [**[NimbleTargetSubnets], none_type**](NimbleTargetSubnets.md) | List of target subnet labels. If specified, discovery and access to volumes will be restricted to the specified subnets. List of target subnet tables. | [optional] 
**type** | **str, none_type** | type | [optional] 
**volume_count** | **int, none_type** | Number of volumes that are accessible by the initiator group. | [optional] 
**volume_list** | [**[NimbleVolList], none_type**](NimbleVolList.md) | List of volumes that are accessible by the initiator group. List of volumes. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


