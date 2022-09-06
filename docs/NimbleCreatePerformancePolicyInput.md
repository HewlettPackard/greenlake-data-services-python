# NimbleCreatePerformancePolicyInput

Create Device Type 2 performance policy.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the Performance Policy. String of up to 64 alphanumeric characters, - and . and : and space are allowed after first character. | 
**app_category** | **str, none_type** | Specifies the application category of the associated volume. Plain string. Defaults to &#39;Unassigned&#39;. | [optional] 
**block_size** | **int, none_type** | Block Size in bytes to be used by the volumes created with this specific performance policy. Supported block sizes are 4096 bytes (4 KB), 8192 bytes (8 KB), 16384 bytes(16 KB), and 32768 bytes (32 KB). Block size of a performance policy cannot be changed once the performance policy is created. Defaults to 4096. | [optional] 
**cache** | **bool, none_type** | Flag denoting if data in the associated volume should be cached. Defaults to &#39;true&#39;. | [optional] 
**cache_policy** | **str, none_type** | Specifies how data of associated volume should be cached. Supports two policies, &#39;normal&#39; and &#39;aggressive&#39;. &#39;normal&#39; policy caches data but skips in certain conditions such as sequential I/O. &#39;aggressive&#39; policy will accelerate caching of all data belonging to this volume, regardless of sequentiality. Possible values:&#39;normal&#39;, &#39;no_write&#39;, &#39;aggressive_read_no_write&#39;, &#39;disabled&#39;, &#39;aggressive&#39;. Defaults to &#39;normal&#39;. | [optional] 
**compress** | **bool, none_type** | Flag denoting if data in the associated volume should be compressed. Defaults to &#39;true&#39;. | [optional] 
**dedupe_enabled** | **bool, none_type** | Specifies if dedupe is enabled for volumes created with this performance policy. | [optional] 
**description** | **str, none_type** | Description of a performance policy. String of up to 255 printable ASCII characters. | [optional] 
**space_policy** | **str, none_type** | Specifies the state of the volume upon space constraint violation such as volume limit violation or volumes above their volume reserve, if the pool free space is exhausted. Supports two policies, &#39;offline&#39; and &#39;non_writable&#39;. Possible values:&#39;offline&#39;, &#39;login_only&#39;, &#39;non_writable&#39;, &#39;read_only&#39;, &#39;invalid&#39;. Defaults to &#39;offline&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


