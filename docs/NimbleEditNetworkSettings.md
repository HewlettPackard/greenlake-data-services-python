# NimbleEditNetworkSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_list** | [**list[NimbleEditArrayNet]**](NimbleEditArrayNet.md) | List of array network configs. | [optional] 
**iscsi_automatic_connection_method** | **bool** | Enable automatic connection method. Enabling this means means redirecting connections from the specified iSCSI discovery IP to the best data IP based on connection counts. | [optional] 
**iscsi_connection_rebalancing** | **bool** | Enable connection rebalancing. Enabling this means rebalancing iSCSI connections by periodically breaking existing connections that are out-of-balance, allowing the host to reconnect to a more appropriate data IP. | [optional] 
**mgmt_ip** | **str** | Management IP for the Group. Four numbers in the range [0,255] separated by periods. | [optional] 
**name** | **str** | Name of the network configuration. Use the name &#39;draft&#39; when creating a draft configuration. Possible values are &#39;active&#39;, &#39;backup&#39; and &#39;draft&#39;. | [optional] 
**route_list** | [**list[NimbleRoute]**](NimbleRoute.md) | List of static routes. | [optional] 
**secondary_mgmt_ip** | **str** | Secondary management IP address for the Group. Four numbers in the range [0,255] separated by periods. | [optional] 
**subnet_list** | [**list[NimbleSubnet]**](NimbleSubnet.md) | List of subnet configs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


