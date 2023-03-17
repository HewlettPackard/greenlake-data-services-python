# EditSnmpSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snmp_community** | **str** | Community string to be used with SNMP. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. | [optional] 
**snmp_get_enabled** | **bool** | Accept SNMP commands. | [optional] 
**snmp_get_port** | **int** | Port number to which SNMP get requests should be sent. Positive integer value up to 65535 representing TCP/IP port. | [optional] 
**snmp_sys_contact** | **str** | Name of the SNMP administrator. Plain string. | [optional] 
**snmp_sys_location** | **str** | Location of the group. Plain string. | [optional] 
**snmp_trap_enabled** | **bool** | Enable or disable SNMP traps | [optional] 
**snmp_trap_host** | **str** | Hostname or IP Address to send SNMP traps. String of alphanumeric characters, valid range is from 2 to 255; Each label must be between 1 and 63 characters long; - and . are allowed after the first and before the last character. | [optional] 
**snmp_trap_port** | **int** | Port number of SNMP trap host. Positive integer value up to 65535 representing TCP/IP port. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


