# NimbleEventsWithRequestUri


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str, none_type** | requestUri for detailed events object | [optional] 
**alarm_id** | **str, none_type** | The alarm ID if the event is related to an alarm. A 42 digit hexadecimal number. | [optional] 
**category** | **str, none_type** | Category of the event record. Possible values: &#39;unknown&#39;, &#39;hardware&#39;, &#39;service&#39;, &#39;replication&#39;, &#39;volume&#39;, &#39;update&#39;, &#39;configuration&#39;, &#39;test&#39;, &#39;security&#39;, &#39;array_upgrade&#39;. | [optional] 
**event_type** | **int, none_type** | Type of the event record. Non-negative integer in range [0,2147483647]. | [optional] 
**id** | **str, none_type** | Identifier for the event record. A 42 digit hexadecimal number. | [optional] 
**scope** | **str, none_type** | The array name for array level event. Possible values: array serial number, or &#39;-&#39;. | [optional] 
**severity** | **str, none_type** | Severity level of the event. Possible values: &#39;info&#39;, &#39;notice&#39;, &#39;warning&#39;, &#39;critical&#39;. | [optional] 
**target** | **str, none_type** | Name of object upon which the event occurred. String of up to 400 alphanumeric characters, - and . and : and \&quot; \&quot; are allowed after first character. | [optional] 
**target_type** | **str, none_type** | Target type of the event record. Possible values: &#39;anon&#39;, &#39;array&#39;, &#39;controller&#39;, &#39;disk&#39;, &#39;nic&#39;, &#39;temperature&#39;, &#39;service&#39;, &#39;volume&#39;, &#39;protection_set&#39;, &#39;nvram&#39;, &#39;fan&#39;, &#39;power_supply&#39;, &#39;partner&#39;, &#39;raid&#39;, &#39;test&#39;, &#39;iscsi&#39;, &#39;pool&#39;, &#39;group&#39;, &#39;shelf&#39;, &#39;ntb&#39;, &#39;fc&#39;, &#39;initiator_group&#39;. | [optional] 
**timestamp** | **int, none_type** | Time when this event happened. Seconds since last epoch i.e. 00:00 January 1, 1970. | [optional] 
**activity** | **str, none_type** | Description of the event. String of 1-1476 printable characters. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**summary** | **str, none_type** | Summary of the event. Plain string. | [optional] 
**type** | **str, none_type** | type | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


