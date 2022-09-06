# AccessControlRecord


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_protocol** | **str, none_type** | Access protocol of snapshot or volume. Possible values: &#39;iscsi&#39;, &#39;fc&#39;. | [optional] 
**acl_id** | **str, none_type** | ID of access control record. | [optional] 
**apply_to** | **str, none_type** | State of apply to. Possible values: &#39;volume&#39;. &#39;pe&#39;, &#39;vvol_volume&#39;, &#39;vvol_snapshot&#39;, &#39;snapshot&#39;, &#39;both&#39;. | [optional] 
**chap_user_id** | **str, none_type** | ID of chap user. | [optional] 
**chap_user_name** | **str, none_type** | Name of chap user. | [optional] 
**id** | **str, none_type** | ID of access control record. | [optional] 
**initiator_group_id** | **str, none_type** | ID of initiator group. | [optional] 
**initiator_group_name** | **str, none_type** | Name of initiator group. | [optional] 
**lun** | **int, none_type** | LUN of snapshot or volume. Secondary LUN if this is Virtual Volume. | [optional] 
**pe_id** | **str, none_type** | ID of protocol endpoint. | [optional] 
**pe_lun** | **int, none_type** | LUN of protocol endpoint. | [optional] 
**pe_name** | **str, none_type** | Name of protocol endpoint. | [optional] 
**snap_id** | **str, none_type** | ID of snapshot. | [optional] 
**snap_name** | **str, none_type** | Name of snapshot. | [optional] 
**snapluns** | [**[SnapshotLunInfo], none_type**](SnapshotLunInfo.md) |  | [optional] 
**vol_id** | **str, none_type** | ID of volume. | [optional] 
**vol_name** | **str, none_type** | Name of volume. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


