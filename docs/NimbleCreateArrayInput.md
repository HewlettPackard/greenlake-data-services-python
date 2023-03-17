# NimbleCreateArrayInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_lower_limits** | **bool** | Whether to create associated pool during array create. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**create_pool** | **bool** | Whether to create associated pool during array create. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**ctrlr_a_support_ip** | **str** | Controller A Support IP address. | 
**ctrlr_b_support_ip** | **str** | Controller B Support IP address. | 
**dedupe_disabled** | **bool** | Is data deduplication disabled for this array. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**name** | **str** | The user provided name of the array. It is also the array&#39;s hostname. String of up to 63 alphanumeric and can include hyphens characters but cannot start with hyphen. | 
**nic_list** | [**list[NICDetails]**](NICDetails.md) | List of NICs information. Used while creating an array. | 
**pool_description** | **str** | Text description of the pool to be created during array creation. String of up to 255 printable ASCII characters. | [optional] 
**pool_name** | **str** | Name of pool to which this is a member. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | 
**secondary_mgmt_ip** | **str** | Secondary management IP address for the Group. | [optional] 
**serial** | **str** | Serial number of the array. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


