# TaskProperties


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_details** | **bool, date, datetime, dict, float, int, list, str, none_type** | A link to be displayed in the Tasks UI. This can be used when a task is paused to take the user to the console UI page with information on how to unpause the task, or for more general information when the task is in other states. | [optional] 
**associated_resources** | [**[ResourceReference]**](ResourceReference.md) | Resources that are associated with the task. These may be created by the task or other resources that are involved in the task. | [optional] 
**child_tasks** | [**[ResourceReference]**](ResourceReference.md) | A list of sub-tasks that were initiated by this task. | [optional] 
**created_at** | **datetime** | The time this task was created. | [optional] 
**display_name** | **str** | The displayed name for the task. | [optional] 
**ended_at** | **datetime, none_type** | The time this task completed. | [optional] 
**error** | **bool, date, datetime, dict, float, int, list, str, none_type** | The error response status of the operation. | [optional] 
**estimated_running_duration_minutes** | **int** | An estimate of how long the task will run before completing. | [optional] 
**health_status** | **str** | The health status indicates if any errors or problems have been encountered during the processing of the task.  Expected values are OK, ERROR, WARNING, UNKNOWN, and UNSPECIFIED.  | [optional] 
**log_messages** | [**[TaskLogMessage]**](TaskLogMessage.md) | Time stamped messages that record the progress of the task. | [optional] 
**parent_task** | **bool, date, datetime, dict, float, int, list, str, none_type** | The parent is the task that initiated this sub-task. If this is not a sub-task this will be a self reference. | [optional] 
**progress_percent** | **int** | A percentage representation of progress to completion. | [optional] 
**recommendations** | [**[TaskRecommendations]**](TaskRecommendations.md) | Recommendations on how to fix failing tasks. | [optional] 
**source_resource** | **bool, date, datetime, dict, float, int, list, str, none_type** | The resource that was used to initiate the task. | [optional] 
**started_at** | **datetime, none_type** | The time this task was started. | [optional] 
**state** | **str** | A message to indicate the current state of the task, for example the current step in a workflow. Expected values are INITIALIZED, RUNNING, FAILED, SUCCEEDED, TIMEDOUT, PAUSED, and UNSPECIFIED.  | [optional] 
**suggested_polling_interval_seconds** | **int** | This attribute suggests a suitable interval to use when polling for progress. Where specified this will be based on the frequency with which the task is likely to be updated. | [optional] 
**updated_at** | **datetime, none_type** | The time this task was last updated. | [optional] 
**user_id** | **str** | The ID or email address of the user that initiated the task. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


