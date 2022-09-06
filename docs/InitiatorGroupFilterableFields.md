# InitiatorGroupFilterableFields


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_protocol** | **str, none_type** | Initiator group access protocol. Possible values: &#39;iscsi&#39;, &#39;fc&#39;.&#x60;Filter, Sort&#x60; | [optional] 
**app_uuid** | **str, none_type** | Application identifier of initiator group. String of up to 255 alphanumeric characters, hyphen, colon, dot and underscore are allowed.&#x60;Filter, Sort&#x60; | [optional] 
**host_type** | **str, none_type** | Initiator group host type. Available options are auto and hpux. The default option is auto. This attribute will be applied to all the initiators in the initiator group. Initiators with different host OSes should not be kept in the same initiator group having a non-default host type attribute. String of up to 64 alphanumeric characters, - and . and : are allowed after first character. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str, none_type** | Identifier for initiator group. A 42 digit hexadecimal number. &#x60;Filter&#x60; | [optional] 
**name** | **str, none_type** | Name of initiator group. String of up to 64 alphanumeric characters, - and . and : are allowed after first character.&#x60;Filter, Sort&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


