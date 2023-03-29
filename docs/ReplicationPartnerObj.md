# ReplicationPartnerObj

The request body for replication partner.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**Source**](Source.md) |  | 
**target** | [**Target**](Target.md) |  | 
**target_system_id** | **str** | Target system ID | 
**control_port** | **int, none_type** | Port number of partner control interface. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**data_port** | **int, none_type** | Port number of partner data interface. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**description** | **str, none_type** | Description of replication partner. String of up to 255 printable ASCII characters. | [optional] 
**repl_hostname** | **str, none_type** | IP address or hostname of partner data interface. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | [optional] 
**subnet_label** | **str** | Label of the subnet used to replicate to this partner. String of up to 64 alphanumeric characters, - and . and colon are allowed after first character. | [optional] 
**subnet_type** | **str, none_type** | Type of the subnet used to replicate to this partner. Possible values are &#39;invalid&#39;, &#39;unconfigured&#39;, &#39;mgmt&#39;, &#39;data&#39;, &#39;mgmt_data&#39;. | [optional] 
**throttles** | [**[ReplicationThrottle], none_type**](ReplicationThrottle.md) | Throttles used while replicating from/to this partner. All the throttles for the partner. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


