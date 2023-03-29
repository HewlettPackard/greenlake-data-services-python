# NimbleProtectionTemplateDetailsWithRequestUri


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_uri** | **str, none_type** | requestUri for detailed protection-templates object | [optional] 
**agent_hostname** | **str, none_type** | Generic Backup agent hostname. Custom port number can be specified with agent hostname using \\\\\&quot;:\\\\\&quot;. | [optional] 
**app_cluster_name** | **str, none_type** | If the application is running within a Windows cluster environment then this is the cluster name. | [optional] 
**app_id** | **str, none_type** | Application ID running on the server. Application ID can only be specified if application synchronization is VSS.  Possible values:&#39;exchange_dag&#39;, &#39;sql2012&#39;, &#39;sql2014&#39;, &#39;inval&#39;, &#39;sql2005&#39;, &#39;sql2016&#39;, &#39;exchange&#39;, &#39;sql2017&#39;, &#39;sql2018&#39;, &#39;hyperv&#39;. | [optional] 
**app_server** | **str, none_type** | Application server hostname. | [optional] 
**app_service_name** | **str, none_type** | If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. | [optional] 
**app_sync** | **str, none_type** | Application synchronization ({none|vss|vmware|generic}). Possible values:&#39;vss&#39;, &#39;vmware&#39;, &#39;none&#39;, &#39;generic&#39;. | [optional] 
**creation_time** | **int, none_type** | Time when this protection template was created. | [optional] 
**id** | **str, none_type** | Identifier for protection template. | [optional] 
**last_modified** | **int, none_type** | Time when this protection template was last modified. | [optional] 
**name** | **str, none_type** | Fully qualified name of protection template. | [optional] 
**vcenter_hostname** | **str, none_type** | VMware vCenter hostname. Custom port number can be specified with vCenter hostname. | [optional] 
**agent_username** | **str, none_type** | Generic Backup agent username. | [optional] 
**associated_links** | [**AssociatedLinks**](AssociatedLinks.md) |  | [optional] 
**console_uri** | **str, none_type** | consoleUri for detailed storage object | [optional] 
**customer_id** | **str, none_type** | customerId | [optional] 
**description** | **str, none_type** | Text description of protection template. | [optional] 
**full_name** | **str, none_type** | Fully qualified name of protection template. | [optional] 
**generation** | **int, none_type** | generation | [optional] 
**repl_priority** | **str, none_type** | Replication priority for the protection template with the following choices: {normal | high}. Possible values:&#39;normal&#39;, &#39;high&#39;. | [optional] 
**resource_uri** | **str, none_type** | Link to the object URI | [optional] 
**schedule_list** | [**[NimbleNsSchedule], none_type**](NimbleNsSchedule.md) | List of schedules for this protection policy. | [optional] 
**search_name** | **str, none_type** | Name of protection template used for object search. | [optional] 
**type** | **str, none_type** | type | [optional] 
**vcenter_username** | **str, none_type** | VMware vCenter username. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


