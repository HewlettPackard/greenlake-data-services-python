# NimbleEditVolumeCollectionInput

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_hostname** | **str** | Generic backup agent hostname. Custom port number can be specified with agent hostname using \\\\\&quot;:\\\\\&quot;. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**agent_username** | **str** | Generic backup agent username. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**app_cluster_name** | **str** | If the application is running within a Windows cluster environment, this is the cluster name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**app_id** | **str** | Application ID running on the server. Application ID can only be specified if application synchronization is \\\\\&quot;vss\\\\\&quot;. Possible values: &#39;inval&#39;, &#39;exchange&#39;, &#39;exchange_dag&#39;, &#39;hyperv&#39;, &#39;sql2005&#39;, &#39;sql2008&#39;, &#39;sql2012&#39;, &#39;sql2014&#39;, &#39;sql2016&#39;, &#39;sql2017&#39;. | [optional] 
**app_server** | **str** | Application server hostname. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**app_service_name** | **str** | If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**app_sync** | **str** | Application Synchronization. Possible values: &#39;none&#39;, &#39;vss&#39;, &#39;vmware&#39;, &#39;generic&#39;. | [optional] 
**description** | **str** | Text description of volume collection. String of up to 255 printable ASCII characters. | [optional] 
**name** | **str** | Name of volume collection. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**vcenter_hostname** | **str** | VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\\\\&quot;:\\\\\&quot;. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**vcenter_username** | **str** | Application VMware vCenter username. String of up to 80 alphanumeric characters, beginning with a letter. It can include ampersand (@), backslash (\\), dash (-), period (.), and underscore (_). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


