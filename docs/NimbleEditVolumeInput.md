# NimbleEditVolumeInput

Edit Nimble volume input.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_uuid** | **str, none_type** | Application identifier of volume. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed. | [optional] 
**caching_enabled** | **bool, none_type** | Indicate caching the volume is enabled. | [optional] 
**dedupe_enabled** | **bool, none_type** | Indicate whether dedupe is enabled. | [optional] 
**description** | **str, none_type** | Text description of volume. String of up to 255 printable ASCII characters. | [optional] 
**folder_id** | **str, none_type** | ID of the folder holding this volume. An optional NsObjectID. A 42 digit hexadecimal number or the empty string. | [optional] 
**force** | **bool, none_type** | Forcibly offline, reduce size or change read-only status a volume. | [optional] 
**limit** | **int, none_type** | Limit for the volume as a percentage of volume size. Percentage as integer from 0 to 100. | [optional] 
**limit_iops** | **int, none_type** | IOPS limit for this volume. If limit_iops is not specified when a volume is created, or if limit_iops is set to -1, then the volume has no IOPS limit. If limit_iops is not specified while creating a clone, IOPS limit of parent volume will be used as limit. IOPS limit should be in range [256, 4294967294] or -1 for unlimited. If both limit_iops and limit_mbps are specified, limit_mbps must not be hit before limit_iops. In other words, IOPS and MBPS limits should honor limit_iops _ampersand_amp;lt;&#x3D; ((limit_mbps MB/s * 2^20 B/MB) / block_size B). | [optional] 
**limit_mbps** | **int, none_type** | Throughput limit for this volume in MB/s. If limit_mbps is not specified when a volume is created, or if limit_mbps is set to -1, then the volume has no MBPS limit. MBPS limit should be in range [1, 4294967294] or -1 for unlimited. If both limit_iops and limit_mbps are specified, limit_mbps must not be hit before limit_iops. In other words, IOPS and MBPS limits should honor limit_iops _ampersand_amp;lt;&#x3D; ((limit_mbps MB/s * 2^20 B/MB) / block_size B). | [optional] 
**name** | **str, none_type** | Name of the volume. String of up to 215 alphanumeric, hyphenated, colon, or period-separated characters; but cannot begin with hyphen, colon or period. | [optional] 
**online** | **bool, none_type** | Online state of volume, available for host initiators to establish connections. | [optional] 
**owned_by_group_id** | **str, none_type** | ID of group that currently owns the volume. A 42 digit hexadecimal number. | [optional] 
**perfpolicy_id** | **str, none_type** | Identifier of the performance policy. After creating a volume, performance policy for the volume can only be changed to another performance policy with same block size. A 42 digit hexadecimal number. &#x60;Filter, Sort&#x60; | [optional] 
**size** | **int, none_type** | Volume size in megabytes. Size is required for creating a volume but not for cloning an existing volume. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


