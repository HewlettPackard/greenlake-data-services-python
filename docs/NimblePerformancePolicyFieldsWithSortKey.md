# NimblePerformancePolicyFieldsWithSortKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_category** | **str, none_type** | Specifies the application category of the associated volume. &#x60;Filter, Sort&#x60; | [optional] 
**cache** | **bool, none_type** | Flag denoting if data in the associated volume should be cached. &#x60;Filter, Sort&#x60; | [optional] 
**cache_policy** | **str, none_type** | Specifies how data of associated volume should be cached. Supports two policies, &#39;normal&#39; and &#39;aggressive&#39;. &#39;normal&#39; policy caches data but skips in certain conditions such as sequential I/O. &#39;aggressive&#39; policy will accelerate caching of all data belonging to this volume, regardless of sequentiality. Possible values:&#39;normal&#39;, &#39;no_write&#39;, &#39;aggressive_read_no_write&#39;, &#39;disabled&#39;, &#39;aggressive&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**compress** | **bool, none_type** | Flag denoting if data in the associated volume should be compressed. &#x60;Filter, Sort&#x60; | [optional] 
**creation_time** | **int, none_type** | Time when the performance policy was created. &#x60;Filter, Sort&#x60; | [optional] 
**dedupe_enabled** | **bool, none_type** | Specifies if dedupe is enabled for volumes created with this performance policy. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str, none_type** | Unique Identifier for the Performance Policy. &#x60;Filter&#x60; | [optional] 
**last_modified** | **int, none_type** | Time when the performance policy&#39;s configurations were last modified. &#x60;Filter, Sort&#x60; | [optional] 
**name** | **str, none_type** | Name of the Performance Policy. &#x60;Filter, Sort&#x60; | [optional] 
**predefined** | **bool, none_type** | Specifies if this performance policy is predefined (read-only). &#x60;Filter, Sort&#x60; | [optional] 
**space_policy** | **str, none_type** | Specifies the state of the volume upon space constraint violation such as volume limit violation or volumes above their volume reserve, if the pool free space is exhausted. Supports two policies, &#39;offline&#39; and &#39;non_writable&#39;. Possible values:&#39;offline&#39;, &#39;login_only&#39;, &#39;non_writable&#39;, &#39;read_only&#39;, &#39;invalid&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


