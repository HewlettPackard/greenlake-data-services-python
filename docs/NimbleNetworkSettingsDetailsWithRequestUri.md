# NimbleNetworkSettingsDetailsWithRequestUri


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str, none_type** | requestUri for detailed network setting object | [optional] 
**id** | **str, none_type** | Identifier for network settings. | [optional] 
**name** | **str, none_type** | Name of the network configuration. Possible values: &#39;active&#39;, &#39;backup&#39;, &#39;draft&#39; | [optional] 
**role** | **str, none_type** | Role of network configuration. Possible values: &#39;active&#39;, &#39;backup&#39;, &#39;draft&#39; | [optional] 
**active_since** | **int, none_type** | Start time of activity. | [optional] 
**array_list** | [**[NimbleArrayNet], none_type**](NimbleArrayNet.md) | List of array network configs. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**creation_time** | **int, none_type** | Time when this net configuration was created. | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**group_leader_array** | **str, none_type** | Name of the group leader array. | [optional] 
**iscsi_automatic_connection_method** | **bool, none_type** | Indicates whether automatic connection method is enabled. | [optional] 
**iscsi_connection_rebalancing** | **bool, none_type** | Indicates whether rebalancing is enabled. | [optional] 
**last_active** | **int, none_type** | Time of last activity. | [optional] 
**last_modified** | **int, none_type** | Time when this network configuration was last modified. | [optional] 
**mgmt_ip** | **str, none_type** | Management IP address for the Group. | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**route_list** | [**[NimbleRoute], none_type**](NimbleRoute.md) | List of static routes. | [optional] 
**secondary_mgmt_ip** | **str, none_type** | Secondary management IP address for the Group. | [optional] 
**subnet_list** | [**[NimbleSubnet], none_type**](NimbleSubnet.md) | List of subnet configs. | [optional] 
**type** | **str, none_type** | type | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


