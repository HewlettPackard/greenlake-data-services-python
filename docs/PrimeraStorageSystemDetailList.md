# PrimeraStorageSystemDetailList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**PrimeraAssociatedLinks**](PrimeraAssociatedLinks.md) |  | [optional] 
**centerplane_type** | **str** | Centerplane type | [optional] 
**chunklet_size_mi_b** | **int** | Size of chunklet in MiB | [optional] 
**cluster_led** | **str** | Cluster LED state | [optional] 
**customer_id** | **str** | customerId | [optional] 
**descriptors** | [**Descriptors**](Descriptors.md) |  | [optional] 
**device_id** | **int** | Numeric ID of the resource &#x60;Filter&#x60; | [optional] 
**device_type** | [**PrimeraStorageSystemDetailDeviceType**](PrimeraStorageSystemDetailDeviceType.md) |  | [optional] 
**displayname** | **str** | Array Display name | [optional] 
**domain** | **str** | Domain that the resource belongs to | [optional] 
**generation** | **int** | generation &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | SystemWWN/UUID string uniquely identifying the storage system object. &#x60;Filter&#x60; | [optional] 
**in_cluster_nodes** | **list[int]** | IDs of the nodes that are in cluster | [optional] 
**is_fips_enabled** | **bool** | Flag for FIPS | [optional] 
**locate_enabled** | **bool** | Indicates if the locate beacon is enabled or not | [optional] 
**maintenance_mode** | [**MaintenanceMode**](MaintenanceMode.md) |  | [optional] 
**manufacturing** | [**ManufacturingSys**](ManufacturingSys.md) |  | [optional] 
**master_node** | **int** | ID of the master node | [optional] 
**minimum_password_length** | **int** | Minimum length of password for users | [optional] 
**name** | **str** | Name of the resource &#x60;Filter, Sort&#x60; | [optional] 
**network_master_node** | **int** | The Node ID of the current network master &#x60;Filter, Sort&#x60; | [optional] 
**node_memory** | **str** | Node memory size | [optional] 
**nodes_count** | **int** | Number of nodes in the system | [optional] 
**nodes_present** | **list[int]** | IDs of the nodes that are present | [optional] 
**online_nodes** | **list[int]** | IDs of the nodes that are online | [optional] 
**overall_state** | **str** | overallState state derived from enclosure, disk and node state For deviceType1 State derived from ports, enclosure, disk and node state for deviceType2 state is state reported by deviceType2 array &#x60;Filter, Sort&#x60; | [optional] 
**parameters** | [**Parameters**](Parameters.md) |  | [optional] 
**resource_uri** | **str** | resourceUri for detailed storage object | [optional] 
**safe_to_remove** | **bool** | Indicates if the component is safe to remove | [optional] 
**software_versions** | [**SoftwareVersions**](SoftwareVersions.md) |  | [optional] 
**state** | [**SystemState**](SystemState.md) |  | [optional] 
**sys_log_status** | [**SysLogStatus**](SysLogStatus.md) |  | [optional] 
**system_date** | **int** | Current date of the system | [optional] 
**system_headroom** | [**SystemHeadroom**](SystemHeadroom.md) |  | [optional] 
**system_wwn** | **str** | WWN of the array &#x60;Filter, Sort&#x60; | [optional] 
**timezone** | **str** | Current timezone of the system | [optional] 
**type** | **str** | type | [optional] 
**uptime** | [**Uptime**](Uptime.md) |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


