# NimbleVCollectionFieldsWithSortKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_cluster_name** | **str, none_type** | If the application is running within a Windows cluster environment, this is the cluster name. &#x60;Filter, Sort&#x60; | [optional] 
**app_id** | **str, none_type** | Application ID running on the server. Application ID can only be specified if application synchronization is \\\\\&quot;vss\\\\\&quot;. &#x60;Filter, Sort&#x60; Possible values: &#39;exchange_dag&#39;, &#39;sql2012&#39;, &#39;inval&#39;, &#39;sql2014&#39;, &#39;sql2005&#39;, &#39;sql2016&#39;, &#39;exchange&#39;, &#39;sql2017&#39;, &#39;sql2018&#39;, &#39;hyperv&#39;. | [optional] 
**app_server** | **str, none_type** | Application server hostname. &#x60;Filter, Sort&#x60; | [optional] 
**app_service_name** | **str, none_type** | If the application is running within a Windows cluster environment then this is the instance name of the service running within the cluster environment. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str, none_type** | Identifier of the Volume-Collection. &#x60;Filter&#x60; | [optional] 
**name** | **str, none_type** | Name of volume collection. &#x60;Filter, Sort&#x60; | [optional] 
**prottmpl_id** | **str, none_type** | Identifier of the protection template whose attributes will be used to create this volume collection. This attribute is only used for input when creating a volume collection and is not outputed. &#x60;Filter, Sort&#x60; | [optional] 
**replication_type** | **str, none_type** | Type of replication configured for the volume collection. Possible values: &#39;synchronous&#39;, &#39;periodic_snapshot&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**synchronous_replication_state** | **str, none_type** | State of synchronous replication on the volume collection. Possible values: &#39;in_sync&#39;, &#39;not_applicable&#39;, &#39;out_of_sync&#39;, &#39;unknown&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**synchronous_replication_type** | **str, none_type** | Type of synchronous replication configured for the volume collection. Possible values: &#39;soft_available&#39;, &#39;not_applicable&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


