# NimbleCreateProtectionTemplateInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_cluster_name** | **str** | If the application is running within a Windows cluster environment then this is the cluster name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**app_id** | **str** | Application ID running on the server. Application ID can only be specified if application synchronization is VSS. Possible values: &#39;inval&#39;, &#39;exchange&#39;, &#39;exchange_dag&#39;, &#39;hyperv&#39;, &#39;sql2005&#39;, &#39;sql2008&#39;, &#39;sql2012&#39;, &#39;sql2014&#39;, &#39;sql2016&#39;, &#39;sql2017&#39;. | [optional] 
**app_server** | **str** | Application server hostname. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**app_service_name** | **str** | If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**app_sync** | **str** | Application synchronization. Possible values: &#39;none&#39;, &#39;vss&#39;. | [optional] 
**description** | **str** | Text description of protection template. String of up to 255 printable ASCII characters. | [optional] 
**name** | **str** | Name of the protection template. User provided identifier. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**schedules** | [**list[ProtectionScheduleInput]**](ProtectionScheduleInput.md) | List of protection schedules. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


