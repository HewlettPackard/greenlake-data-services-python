# CollectSupportDataInput

Trigger and collect support data collection on the system

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str, none_type** | Type of a collection. | [optional] 
**options** | **[str], none_type** | Options needed for the collection. If options are not specified, default values will be used.   INSPLORECOLLECTION can have any or all of \&quot;clidata\&quot;, \&quot;nodedata\&quot; and \&quot;tocdata\&quot;     Default options - [\&quot;clidata\&quot;,\&quot;nodedata\&quot;,\&quot;tocdata\&quot;]   PERFCOLLECTION should have 3 options,   * Iteration - a number between 1 to 1000 as a string,   * Interval - a number in seconds between 1 to 172800 as a string   * Type of collection -default or -comprehensive   Default options - [\&quot;60\&quot;,\&quot;10\&quot;,\&quot;-default\&quot;]  Other collection types won&#39;t require any options, if provided will be ignored. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


