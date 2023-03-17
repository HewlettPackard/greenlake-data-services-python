# UninitializedArrayResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_flash** | **bool** | True if it is an All-Flash array, False otherwise.Possible values : true, false. | [optional] 
**array_name** | **str** | Name of the uninitialized array.String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**console_uri** | **str** | consoleUri for detailed storage object | [optional] 
**count_of_fc_ports** | **int** | Number of Fibre Channel ports of the uninitialized array. Unsigned 64-bit integer. | [optional] 
**customer_id** | **str** | customerId | [optional] 
**dedupe_configurable** | **bool** | True if it is a hybrid array that is capable of updating data deduplication setting, False otherwise.Possible values : true, false. | [optional] 
**generation** | **int** | generation | [optional] 
**id** | **str** | Identifier for the uninitialized array. A 42 digit hexadecimal number. | [optional] 
**model_str** | **str** | Model description of the uninitialized array.String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**resource_uri** | **str** |  | [optional] 
**serial** | **str** | Serial Number of the uninitialized array. A 42 digit hexadecimal number. | [optional] 
**type** | **str** | type | [optional] 
**version** | **str** | Version of the uninitialized array. String of up to 64 alphanumeric characters, - and . and :are allowed after first character. | [optional] 
**zconf_ipaddrs** | [**list[NimbleZConfIP]**](NimbleZConfIP.md) | List of link local zero conf address of the uninitialized array. List of IP Addresses | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


