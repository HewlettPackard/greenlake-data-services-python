# AuditData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Required: Unique ID for this audit event message, for example a GUID | 
**message** | **str** | Required: Human readable message string that describes the action that occurred | 
**occurred_at** | **str** | Required: UTC timestamp when the event occurred | 
**state** | **str** | Required: Enum that identifies whether the action was successful or not: Success, Failure, PermissionDenied, Initiated | 
**version** | **int** | Required: Version of the event structure, allowing for changes in the future | 
**associated_resource** | [**AuditResource**](AuditResource.md) |  | [optional] 
**code** | **str** | Unique code that describes the type of audit event that occurred | [optional] 
**context_id** | **str** | Unique id used to track a request across services | [optional] 
**customer_id** | **str** | Application Customer ID associated with this event | [optional] 
**permission** | **str** | Which privilege was used to grant/deny the action. E.g. controller.edit. | [optional] 
**scope** | **str** | Provides additional limits on the authorization of the request. | [optional] 
**source** | **str** | Which service/device is responsible for sending this event | [optional] 
**source_ip_address** | **str** | IP address from where the request originated | [optional] 
**task_id** | **str** | Identifier linking asynchronous operations allowing initiation and completion of operations to be linked | [optional] 
**unique_id** | **str** | Unique identifier generated internally | [optional] 
**user_email** | **str** | User who is associated with this event | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


