# NimbleCreateVolumeCollectionInput

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
**is_standalone_volcoll** | **bool** | Indicates whether this is a standalone volume collection. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**metadata** | [**list[KeyValue]**](KeyValue.md) | Key-value pairs that augment a volume collection&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. | [optional] 
**name** | **str** | Name of volume collection. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | 
**prottmpl_id** | **str** | Identifier of the protection template whose attributes will be used to create this volume collection. This attribute is only used for input when creating a volume collection and is not outputed. A 42 digit hexadecimal number. | [optional] 
**replication_type** | **str** | Type of replication configured for the volume collection. Possible values are periodic snapshot and synchronous. Default value is periodic_snapshot. | [optional] 
**vcenter_hostname** | **str** | VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\\\\&quot;:\\\\\&quot;. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**vcenter_username** | **str** | Application VMware vCenter username. String of up to 80 alphanumeric characters, beginning with a letter. It can include ampersand (@), backslash (\\), dash (-), period (.), and underscore (_). | [optional] 
**volume_list** | **list[str]** | List of volume id&#39;s that need to be added to the volume collection. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


