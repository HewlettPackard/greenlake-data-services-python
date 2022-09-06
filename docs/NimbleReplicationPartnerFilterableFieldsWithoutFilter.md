# NimbleReplicationPartnerFilterableFieldsWithoutFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**array_serial** | **str, none_type** | Serial number of group leader array of the partner. Plain string. | [optional] 
**cfg_sync_status** | **str, none_type** | Indicates whether all volumes and volume collections have been synced to the partner. Possible values: N/A, Yes, No.  | [optional] 
**creation_time** | **int, none_type** | Time when this replication partner was created. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**folder_id** | **str, none_type** | The Folder ID within the pool where volumes replicated from this partner will be created. This is not supported for pool partners. A 42 digit hexadecimal number.  | [optional] 
**folder_name** | **str, none_type** | The Folder name within the pool where volumes replicated from this partner will be created. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**hostname** | **str, none_type** | IP address or hostname of partner interface. This must be the partners Group Management IP address. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**id** | **str, none_type** | Identifier for a replication partner. A 42 digit hexadecimal number. | [optional] 
**is_alive** | **bool, none_type** | Whether the partner is available, and responding to pings. Possible values: true, false | [optional] 
**name** | **str, none_type** | Name of replication partner. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**partner_type** | **str, none_type** | Type of the partner, Possible values: &#39;group&#39; or &#39;pool&#39;.  | [optional] 
**paused** | **bool, none_type** | Indicates whether replication traffic from/to this partner has been halted. Possible values: true, false | [optional] 
**pool_id** | **str, none_type** | The pool ID where volumes replicated from this partner will be created. Replica volumes created as clones ignore this parameter and are always created in the same pool as their parent volume. A 42 digit hexadecimal number. | [optional] 
**pool_name** | **str, none_type** | The pool name where volumes replicated from this partner will be created. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**repl_hostname** | **str, none_type** | IP address or hostname of partner data interface. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**subnet_label** | **str, none_type** | Label of the subnet used to replicate to this partner. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**subnet_netmask** | **str, none_type** | Subnet mask used to replicate to this partner. A netmask expressed as a 32 bit binary value must have the highest bit set (2^31) and the lowest bit clear (2^0) with the first zero followed by only zeros. | [optional] 
**subnet_network** | **str, none_type** | Subnet used to replicate to this partner. Four numbers in the range [0,255] separated by periods. | [optional] 
**subnet_type** | **str, none_type** | Type of the subnet used to replicate to this partner. Possible values: invalid, unconfigured, mgmt, data, mgmt_data | [optional] 
**system_id** | **str, none_type** | Identifier for a system or array. A 42 digit hexadecimal number. | [optional] 
**version** | **int, none_type** | Replication version of the partner. Signed 64-bit integer. | [optional] 
**volume_collection_list_count** | **int, none_type** | Count of volume collections that are replicating from/to this partner. Unsigned 64-bit integer. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


