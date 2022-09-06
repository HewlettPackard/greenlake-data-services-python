# IssueDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Primary identifier for the issue. | 
**additional_details** | **bool, date, datetime, dict, float, int, list, str, none_type** | A link to be displayed in the Issues UI. | [optional] 
**body** | **str** | Long description with more details including possible remediations. | [optional] 
**category** | **str** | Category of the issue. PERFORMANCE, CAPACITY, etc | [optional] 
**cleared_at** | **datetime** | Time when the issue was cleared. RFC 3339 timestamp | [optional] 
**created_at** | **datetime** | Time when the issue was created. RFC 3339 timestamp | [optional] 
**customer_id** | **str** | Primary identifier for the customer (UUID) associated with the issue. | [optional] 
**generation** | **str** | A monotonically increasing value incremented every time the resource is updated | [optional] 
**issue_type** | **str** | The type of the issue. Eg: ISSUE, RECOMMENDATION | [optional] 
**last_occurred_at** | **datetime** | Time when the issue last occurred. RFC 3339 timestamp | [optional] 
**name** | **str** | friendly name of the resource given by the system | [optional] 
**occurrence_count** | **int** | Indicates the number of occurrences of the issue | [optional] 
**related_resource** | **bool, date, datetime, dict, float, int, list, str, none_type** | Details of the resource related to the issue | [optional] 
**related_resource_owner** | **bool, date, datetime, dict, float, int, list, str, none_type** | Details of the owner of the resource related to the issue | [optional] 
**resource_uri** | **str** | URI of the issue. Eg: /api/v1/issues/{id} | [optional] 
**rule_id** | **str** | Indicates the problem associated with the issue. Disambiguated per system. | [optional] 
**severity** | **str** | Severity of the issue. For issue: CRITICAL, WARNING, INFO. For reco: HIGH, MEDIUM, LOW | [optional] 
**state** | **str** | State of the issue. Eg: CREATED, ASSIGNED, CLOSED, SNOOZED, DELETED, etc | [optional] 
**title** | **str** | One line description of the issue | [optional] 
**type** | **str** | Type of the resource. In this case - issue | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


