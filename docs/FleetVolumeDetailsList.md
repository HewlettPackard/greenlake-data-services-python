# FleetVolumeDetailsList

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associated_links** | [**list[PrimeraVolumeDetailsAssociatedLinks]**](PrimeraVolumeDetailsAssociatedLinks.md) | Associated Links | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str** | customerId | [optional] 
**generation** | **int** | generation | [optional] 
**health_state** | **str** | Health State of volume. &#x60;Filter, Sort&#x60; | [optional] 
**host_written_capacity_mi_b** | **float** | Host written data size in MiB. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | UUID string uniquely identifying the storage system object. &#x60;Filter&#x60; | [optional] 
**initiators** | [**list[PrimeraApplicationSetDetailsInitiators]**](PrimeraApplicationSetDetailsInitiators.md) | Initiator details | [optional] 
**is_internal** | **bool** | boolean value which specifies if it is a systemVolume or not &#x60;Filter&#x60; | [optional] 
**is_system_volume** | **bool** | boolean value which specifies if it is a systemVolume or not &#x60;Filter&#x60; | [optional] 
**name** | **str** | A user friendly name to identify the storage system volume (resourceName). &#x60;Filter, Sort&#x60; | [optional] 
**product_family** | **str** | Product Family | [optional] 
**resource_uri** | **str** | resourceUri for detailed volume object | [optional] 
**size_mi_b** | **float** | Size in MiB &#x60;Filter, Sort&#x60; | [optional] 
**space_warning** | **float** |  | [optional] 
**sub_type** | **str** | subType of the volume | [optional] 
**system_id** | **str** | SystemUid/Serial Number  of the array. &#x60;Filter, Sort&#x60; | [optional] 
**thin_savings** | **str** | Thin savings | [optional] 
**type** | **str** | type | [optional] 
**used_capacity_percent** | **float** | Used capacity percentage of volume. &#x60;Filter, Sort&#x60; | [optional] 
**used_size_mi_b** | **float** | Size in MiB | [optional] 
**volume_set_id** | **str** | SystemUid/serialNumber of the volumeSet. | [optional] 
**volume_type** | **str** | VV Type | [optional] 
**wwn** | **str** | Volume wwn. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


