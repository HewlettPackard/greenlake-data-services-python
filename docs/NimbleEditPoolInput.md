# NimbleEditPoolInput

Update pool attributes

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_list** | [**[EditPoolNimbleArrayDetail]**](EditPoolNimbleArrayDetail.md) | List of arrays identified by their IDs, in the pool. | [optional] 
**dedupe_all_volumes** | **bool, none_type** | Indicates if dedupe is enabled by default for new volumes on this pool. | [optional] 
**dedupe_capable** | **bool, none_type** | Indicates whether the pool is capable of hosting deduped volumes. | [optional] 
**description** | **str, none_type** | Text description of pool. String of up to 255 printable ASCII characters. | [optional] 
**force** | **bool, none_type** | Forcibly delete the specified pool even if it contains deleted volumes whose space is being reclaimed. Forcibly remove an array from array_list via an update operation even if the array is not reachable. There should no volumes currently in the pool for the forced update operation to succeed. | [optional] 
**is_default** | **bool, none_type** | Indicates if this is the default pool. | [optional] 
**name** | **str, none_type** | Name of pool. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


