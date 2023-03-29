# UpgradeDetails

Array upgrade data

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**[NimbleErrorWithArguments], none_type**](NimbleErrorWithArguments.md) | List of error or info messages. | [optional] 
**stage** | **str, none_type** | Array upgrade stage. Possible values: &#39;prepare&#39;, &#39;finish&#39;, &#39;none&#39;. | [optional] 
**state** | **str, none_type** | Array upgrade state. Possible values: &#39;abort_failed&#39;, &#39;precheck&#39;, &#39;in_progress&#39;, &#39;paused&#39;, &#39;aborted&#39;, &#39;aborting&#39;, &#39;started&#39;, &#39;none&#39;, &#39;failed&#39;, &#39;awaiting_next_stage&#39;, &#39;complete&#39;. | [optional] 
**type** | **str, none_type** | Array upgrade type. Possible values: &#39;offline&#39;, &#39;invalid&#39;. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


