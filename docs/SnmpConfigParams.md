# SnmpConfigParams


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manager_ip** | **str** | Specify the IP address of the host from which the manager runs | [optional] 
**notify** | **str, none_type** | Indicates the trap notification types defined by the HPE deviceType1 MIB | [optional] 
**port** | **int, none_type** | Specify the port number where the SNMP manager receives traps | [optional] 
**retry** | **int, none_type** | Specify the number of times to send a trap (retry) if the SNMP manager is not available. | [optional] 
**timeout_secs** | **int, none_type** | Specify the number of seconds to wait before sending a trap (timeout). | [optional] 
**user** | **str, none_type** | Specify the SNMPv3 user name | [optional] 
**version** | **int, none_type** | Specify the SNMP version supported | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


