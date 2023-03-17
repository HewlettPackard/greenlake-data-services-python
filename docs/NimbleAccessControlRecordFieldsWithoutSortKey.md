# NimbleAccessControlRecordFieldsWithoutSortKey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_protocol** | **str** | Access protocol of the volume. Possible values:&#39;iscsi&#39;, &#39;fc&#39;. | [optional] 
**chap_user_id** | **str** | Identifier for the CHAP user. | [optional] 
**chap_user_name** | **str** | Flag denoting if data in the associated volume should be compressed. | [optional] 
**creation_time** | **int** | Time when this access control record was created. | [optional] 
**id** | **str** | Identifier for the access control record. | [optional] 
**initiator_group_id** | **str** | Identifier for the initiator group. | [optional] 
**initiator_group_name** | **str** | Name of the initiator group. | [optional] 
**last_modified** | **int** | Time when this access control record was last modified. | [optional] 
**lun** | **int** | If this access control record applies to a regular volume, this attribute is the volume&#39;s LUN (Logical Unit Number). If the access protocol is iSCSI, the LUN will be 0. However, if the access protocol is Fibre Channel, the LUN will be in the range from 0 to 2047. If this record applies to a Virtual Volume, this attribute is the volume&#39;s secondary LUN in the range from 0 to 399999, for both iSCSI and Fibre Channel. If the record applies to a OpenstackV2 volume, the LUN will be in the range from 0 to 2047, for both iSCSI and Fibre Channel. If this record applies to a protocol endpoint or only a snapshot, this attribute is not meaningful and is set to null. | [optional] 
**pe_id** | **str** | Identifier for the protocol endpoint this access control record applies to. | [optional] 
**pe_lun** | **int** | LUN (Logical Unit Number) to associate with this protocol endpoint. Valid LUNs are in the 0-2047 range. | [optional] 
**pe_name** | **str** | Name of the protocol endpoint this access control record applies to. | [optional] 
**snap_id** | **str** | Identifier for the snapshot this access control record applies to. | [optional] 
**snap_name** | **str** | Name of the snapshot this access control record applies to. | [optional] 
**vol_id** | **str** | Identifier for the volume this access control record applies to. | [optional] 
**vol_name** | **str** | Name of the volume this access control record applies to. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


