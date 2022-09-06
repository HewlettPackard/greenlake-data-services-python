# NimbleCreateVolumeCollectionInput

Create Nimble volume-collection input.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of volume collection. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | 
**agent_hostname** | **str, none_type** | Generic backup agent hostname. Custom port number can be specified with agent hostname using \\\\\&quot;:\\\\\&quot;. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**agent_username** | **str, none_type** | Generic backup agent username. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**app_cluster_name** | **str, none_type** | If the application is running within a Windows cluster environment, this is the cluster name. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**app_id** | **str, none_type** | Application ID running on the server. Application ID can only be specified if application synchronization is \\\\\&quot;vss\\\\\&quot;. Possible values: &#39;inval&#39;, &#39;exchange&#39;, &#39;exchange_dag&#39;, &#39;hyperv&#39;, &#39;sql2005&#39;, &#39;sql2008&#39;, &#39;sql2012&#39;, &#39;sql2014&#39;, &#39;sql2016&#39;, &#39;sql2017&#39;. | [optional] 
**app_server** | **str, none_type** | Application server hostname. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**app_service_name** | **str, none_type** | If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**app_sync** | **str, none_type** | Application Synchronization. Possible values: &#39;none&#39;, &#39;vss&#39;, &#39;vmware&#39;, &#39;generic&#39;. | [optional] 
**description** | **str, none_type** | Text description of volume collection. String of up to 255 printable ASCII characters. | [optional] 
**is_standalone_volcoll** | **bool, none_type** | Indicates whether this is a standalone volume collection. Possible values: &#39;true&#39;, &#39;false&#39;. | [optional] 
**metadata** | [**[KeyValue], none_type**](KeyValue.md) | Key-value pairs that augment a volume collection&#39;s attributes. List of key-value pairs. Keys must be unique and non-empty. When creating an object, values must be non-empty. When updating an object, an empty value causes the corresponding key to be removed. | [optional] 
**prottmpl_id** | **str, none_type** | Identifier of the protection template whose attributes will be used to create this volume collection. This attribute is only used for input when creating a volume collection and is not outputed. A 42 digit hexadecimal number. | [optional] 
**replication_type** | **str, none_type** | Type of replication configured for the volume collection. Possible values are periodic snapshot and synchronous. Default value is periodic_snapshot. | [optional] 
**vcenter_hostname** | **str, none_type** | VMware vCenter hostname. Custom port number can be specified with vCenter hostname using \\\\\&quot;:\\\\\&quot;. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**vcenter_username** | **str, none_type** | Application VMware vCenter username. String of up to 80 alphanumeric characters, beginning with a letter. It can include ampersand (@), backslash (\\), dash (-), period (.), and underscore (_). | [optional] 
**volume_list** | **[str, none_type], none_type** | List of volume id&#39;s that need to be added to the volume collection. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


