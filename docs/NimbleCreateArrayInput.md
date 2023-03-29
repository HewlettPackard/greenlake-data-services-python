# NimbleCreateArrayInput

Create Nimble array input

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ctrlr_a_support_ip** | **str** | Controller A Support IP address. | 
**ctrlr_b_support_ip** | **str** | Controller B Support IP address. | 
**name** | **str** | The user provided name of the array. It is also the array&#39;s hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | 
**nic_list** | [**[NICDetails]**](NICDetails.md) | List of NICs information. Used while creating an array. | 
**pool_name** | **str** | Name of pool to which this is a member. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | 
**serial** | **str** | Serial number of the array. | 
**allow_lower_limits** | **bool, none_type** | Whether to create associated pool during array create. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**create_pool** | **bool, none_type** | Whether to create associated pool during array create. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**dedupe_disabled** | **bool, none_type** | Is data deduplication disabled for this array. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**pool_description** | **str, none_type** | Text description of the pool to be created during array creation. String of up to 255 printable ASCII characters. | [optional] 
**secondary_mgmt_ip** | **str** | Secondary management IP address for the Group. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


