# AlertContactsDetailsList

Contacts details set to receive alerts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | **str, none_type** | Company | [optional] 
**company_code** | **str, none_type** | Company code | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**country** | **str, none_type** | Country | [optional] 
**customer_id** | **str** | The customer application identifier | [optional] 
**fax** | **str, none_type** | Fax number | [optional] 
**first_name** | **str, none_type** | First name | [optional] 
**generation** | **int** | A monotonically increasing value. This value updates when the resource is updated and can be used as a short way to determine if a resource has changed or which of two different copies of a resource is more up to date.  | [optional] 
**id** | **str, none_type** | Unique Identifier of the contact | [optional] 
**include_svc_alerts** | **bool, none_type** | Email sent to contact shall include service alert | [optional] 
**last_name** | **str, none_type** | Last name | [optional] 
**notification_severities** | **[int], none_type** | Severities of notifications the contact will be notificated. An array of number: 0 - Fatal, 1 - Critical, 2 - Major, 3 - Minor, 4 - Degraded, 5 - Info, 6 - Debug | [optional] 
**preferred_language** | **str, none_type** | Preferred language when being contacted or emailed | [optional] 
**primary_email** | **str, none_type** | Primary email address | [optional] 
**primary_phone** | **str, none_type** | Primary phone | [optional] 
**receive_email** | **bool, none_type** | Contact will receive email notifications. This is a deprecated field and will always pass true to be inline with UI. | [optional] 
**receive_grouped** | **bool, none_type** | Contact will receive grouped low urgency email notifications | [optional] 
**request_uri** | **str, none_type** | requestUri for alert contact details | [optional] 
**secondary_email** | **str, none_type** | Secondary email address | [optional] 
**secondary_phone** | **str, none_type** | Secondary phone | [optional] 
**system_id** | **str, none_type** | SystemId/serialNumber of the array. | [optional] 
**system_support_contact** | **bool, none_type** | Contact will be called for any system issues | [optional] 
**type** | **str** | The type of resource | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


