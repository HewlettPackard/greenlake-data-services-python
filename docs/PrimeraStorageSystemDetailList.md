# PrimeraStorageSystemDetailList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**PrimeraAssociatedLinks**](PrimeraAssociatedLinks.md) |  | [optional] 
**centerplane_type** | **str, none_type** | Centerplane type | [optional] 
**chunklet_size_mi_b** | **int, none_type** | Size of chunklet in MiB | [optional] 
**cluster_led** | **str, none_type** | Cluster LED state | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**descriptors** | [**Descriptors**](Descriptors.md) |  | [optional] 
**device_id** | **int, none_type** | Numeric ID of the resource &#x60;Filter&#x60; | [optional] 
**device_type** | [**PrimeraStorageSystemDetailDeviceType**](PrimeraStorageSystemDetailDeviceType.md) |  | [optional] 
**displayname** | **str, none_type** | Array Display name | [optional] 
**domain** | **str, none_type** | Domain that the resource belongs to | [optional] 
**generation** | **int, none_type** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str, none_type** | SystemWWN/UUID string uniquely identifying the storage system object. &#x60;Filter&#x60; | [optional] 
**in_cluster_nodes** | **[int], none_type** | IDs of the nodes that are in cluster | [optional] 
**is_fips_enabled** | **bool, none_type** | Flag for FIPS | [optional] 
**locate_enabled** | **bool, none_type** | Indicates if the locate beacon is enabled or not | [optional] 
**maintenance_mode** | [**MaintenanceMode**](MaintenanceMode.md) |  | [optional] 
**manufacturing** | [**ManufacturingSys**](ManufacturingSys.md) |  | [optional] 
**master_node** | **int, none_type** | ID of the master node | [optional] 
**minimum_password_length** | **int, none_type** | Minimum length of password for users | [optional] 
**name** | **str, none_type** | Name of the resource &#x60;Filter, Sort&#x60; | [optional] 
**network_master_node** | **int, none_type** | The Node ID of the current network master &#x60;Filter, Sort&#x60; | [optional] 
**node_memory** | **str, none_type** | Node memory size | [optional] 
**nodes_count** | **int, none_type** | Number of nodes in the system | [optional] 
**nodes_present** | **[int], none_type** | IDs of the nodes that are present | [optional] 
**online_nodes** | **[int], none_type** | IDs of the nodes that are online | [optional] 
**overall_state** | **str, none_type** | overallState state derived from enclosure, disk and node state For deviceType1 State derived from ports, enclosure, disk and node state for deviceType2 state is state reported by deviceType2 array &#x60;Filter, Sort&#x60; | [optional] 
**parameters** | [**Parameters**](Parameters.md) |  | [optional] 
**resource_uri** | **str, none_type** | resourceUri for detailed storage object | [optional] 
**safe_to_remove** | **bool, none_type** | Indicates if the component is safe to remove | [optional] 
**software_versions** | [**SoftwareVersions**](SoftwareVersions.md) |  | [optional] 
**state** | [**SystemState**](SystemState.md) |  | [optional] 
**sys_log_status** | [**SysLogStatus**](SysLogStatus.md) |  | [optional] 
**system_date** | **int, none_type** | Current date of the system | [optional] 
**system_headroom** | [**SystemHeadroom**](SystemHeadroom.md) |  | [optional] 
**system_wwn** | **str, none_type** | WWN of the array &#x60;Filter, Sort&#x60; | [optional] 
**timezone** | **str, none_type** | Current timezone of the system | [optional] 
**type** | **str, none_type** | type | [optional] 
**uptime** | [**Uptime**](Uptime.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


