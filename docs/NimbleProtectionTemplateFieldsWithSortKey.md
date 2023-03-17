# NimbleProtectionTemplateFieldsWithSortKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_hostname** | **str** | Generic Backup agent hostname. Custom port number can be specified with agent hostname using \\\\\&quot;:\\\\\&quot;. &#x60;Filter, Sort&#x60; | [optional] 
**app_cluster_name** | **str** | If the application is running within a Windows cluster environment then this is the cluster name. &#x60;Filter, Sort&#x60; | [optional] 
**app_id** | **str** | Application ID running on the server. Application ID can only be specified if application synchronization is VSS.  Possible values:&#39;exchange_dag&#39;, &#39;sql2012&#39;, &#39;sql2014&#39;, &#39;inval&#39;, &#39;sql2005&#39;, &#39;sql2016&#39;, &#39;exchange&#39;, &#39;sql2017&#39;, &#39;sql2018&#39;, &#39;hyperv&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**app_server** | **str** | Application server hostname. &#x60;Filter, Sort&#x60; | [optional] 
**app_service_name** | **str** | If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. &#x60;Filter, Sort&#x60; | [optional] 
**app_sync** | **str** | Application synchronization ({none|vss|vmware|generic}). Possible values:&#39;vss&#39;, &#39;vmware&#39;, &#39;none&#39;, &#39;generic&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**creation_time** | **int** | Time when this protection template was created. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str** | Identifier for protection template. &#x60;Filter&#x60; | [optional] 
**last_modified** | **int** | Time when this protection template was last modified. &#x60;Filter, Sort&#x60; | [optional] 
**name** | **str** | Fully qualified name of protection template. &#x60;Filter, Sort&#x60; | [optional] 
**vcenter_hostname** | **str** | VMware vCenter hostname. Custom port number can be specified with vCenter hostname. &#x60;Filter, Sort&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


