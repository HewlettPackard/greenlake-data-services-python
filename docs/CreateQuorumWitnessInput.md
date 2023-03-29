# CreateQuorumWitnessInput

Request body to configure quorum witness

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameters** | [**CreateQuorumWitnessInputParameters**](CreateQuorumWitnessInputParameters.md) |  | 
**replication_partner_system_id** | **str** | SystemId of target replication partner | 
**src_replication_id** | **str** | Id of source replication partner on which quorum witness is to be configured | 
**target_replication_id** | **str** | Id of target replication partner on which quorum witness is to be configured | 
**start_quorum_witness** | **bool, none_type** | Specifies start/stop Quorum Witness connectivity on the storage system. If set true, ATF configuration is activated. If set false, ATF configuration is deactivated. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


