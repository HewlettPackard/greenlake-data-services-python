# NimbleAccessControlRecordFieldsWithSortKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_protocol** | **str, none_type** | Access protocol of the volume. Possible values:&#39;iscsi&#39;, &#39;fc&#39;. &#x60;Filter, Sort&#x60; | [optional] 
**chap_user_id** | **str, none_type** | Identifier for the CHAP user. &#x60;Filter, Sort&#x60; | [optional] 
**chap_user_name** | **str, none_type** | Flag denoting if data in the associated volume should be compressed. &#x60;Filter, Sort&#x60; | [optional] 
**creation_time** | **int, none_type** | Time when this access control record was created. &#x60;Filter, Sort&#x60; | [optional] 
**id** | **str, none_type** | Identifier for the access control record. &#x60;Filter&#x60; | [optional] 
**initiator_group_id** | **str, none_type** | Identifier for the initiator group. &#x60;Filter, Sort&#x60; | [optional] 
**initiator_group_name** | **str, none_type** | Name of the initiator group. &#x60;Filter, Sort&#x60; | [optional] 
**last_modified** | **int, none_type** | Time when this access control record was last modified. &#x60;Filter, Sort&#x60; | [optional] 
**lun** | **int, none_type** | If this access control record applies to a regular volume, this attribute is the volume&#39;s LUN (Logical Unit Number). If the access protocol is iSCSI, the LUN will be 0. However, if the access protocol is Fibre Channel, the LUN will be in the range from 0 to 2047. If this record applies to a Virtual Volume, this attribute is the volume&#39;s secondary LUN in the range from 0 to 399999, for both iSCSI and Fibre Channel. If the record applies to a OpenstackV2 volume, the LUN will be in the range from 0 to 2047, for both iSCSI and Fibre Channel. If this record applies to a protocol endpoint or only a snapshot, this attribute is not meaningful and is set to null. &#x60;Filter, Sort&#x60; | [optional] 
**pe_id** | **str, none_type** | Identifier for the protocol endpoint this access control record applies to. &#x60;Filter, Sort&#x60; | [optional] 
**pe_lun** | **int, none_type** | LUN (Logical Unit Number) to associate with this protocol endpoint. Valid LUNs are in the 0-2047 range. &#x60;Filter, Sort&#x60; | [optional] 
**pe_name** | **str, none_type** | Name of the protocol endpoint this access control record applies to. &#x60;Filter, Sort&#x60; | [optional] 
**snap_id** | **str, none_type** | Identifier for the snapshot this access control record applies to. &#x60;Filter, Sort&#x60; | [optional] 
**snap_name** | **str, none_type** | Name of the snapshot this access control record applies to. &#x60;Filter, Sort&#x60; | [optional] 
**vol_id** | **str, none_type** | Identifier for the volume this access control record applies to. &#x60;Filter, Sort&#x60; | [optional] 
**vol_name** | **str, none_type** | Name of the volume this access control record applies to. &#x60;Filter, Sort&#x60; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


