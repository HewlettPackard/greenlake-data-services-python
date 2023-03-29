# Source

Source partner.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** | IP address or hostname of partner interface. This must be the partner&#39;s Group Management IP address. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | 
**name** | **str** | Name of the replication partner. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | 
**subnet_label** | **str** | Label of the subnet used to replicate to this partner. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | [optional] 
**subnet_type** | **str** | Type of the subnet used to replicate to this partner. Possible values are &#39;invalid&#39;, &#39;unconfigured&#39;, &#39;mgmt&#39;, &#39;data&#39;, &#39;mgmt_data&#39;. | [optional] 
**pool_id** | **str, none_type** | prop0 is \&quot;pool_id\&quot;. The pool ID where volumes replicated from this partner will be created. Replica volumes created as clones ignore this parameter and are always created in the same pool as their parent volume. A 42 digit hexadecimal number. | [optional] 
**folder_id** | **str, none_type** | prop1 is \&quot;folder_id\&quot;. The Folder ID within the pool where volumes replicated from this partner will be created. A 42 digit hexadecimal number. example: 2a0df0fe6f7dc7bb16000000000000000000004818 | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


