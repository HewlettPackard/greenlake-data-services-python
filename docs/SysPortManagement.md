# SysPortManagement

Port Management details for a device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**SysAssociatedLinks**](SysAssociatedLinks.md) |  | [optional] 
**authentication_required** | **str, none_type** | Is authentication required. Allowed values are enabled or disabled | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**default_route_ipv4** | **str, none_type** | Default IPV4 route address of the network port | [optional] 
**default_route_ipv6** | **str, none_type** | Default IPV6 route address of the network port | [optional] 
**displayname** | **str, none_type** | Name to be used for display purposes | [optional] 
**dns_server** | **str, none_type** | DNS Server of the network port | [optional] 
**domain** | **str, none_type** | Domain that the resource belongs to | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date. | [optional] 
**id** | **str, none_type** | Unique Identifier of the resource | [optional] 
**ip_v4_data** | [**Address**](Address.md) |  | [optional] 
**ip_v6_data** | [**Address**](Address.md) |  | [optional] 
**new_default_route_ipv4** | **str, none_type** | New default IPV4 route address of the network port | [optional] 
**new_default_route_ipv6** | **str, none_type** | New default IPV6 route address of the network port | [optional] 
**new_ip_v4_data** | [**Address**](Address.md) |  | [optional] 
**new_ipv6_data** | [**Address**](Address.md) |  | [optional] 
**ntp_server** | **str, none_type** | NTP Server of the network port | [optional] 
**proxy_port** | **int, none_type** | Proxy Server Port. Allowed values are 1-65535 | [optional] 
**proxy_protocol** | **str, none_type** | Supported proxy protocols are HTTP, SOCKS4 and SOCKS5. | [optional] 
**proxy_server** | **str, none_type** | Proxy server IP address | [optional] 
**proxy_user** | **str, none_type** | Username for authentication. (Required only if Authentication required is enabled) | [optional] 
**system_id** | **str, none_type** | Serial Number of the array | [optional] 
**type** | **str** | The type of resource. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


