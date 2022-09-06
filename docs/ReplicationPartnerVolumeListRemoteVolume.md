# ReplicationPartnerVolumeListRemoteVolume

remote volume properties associated with replication partner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**async_outstanding** | **int, none_type** | Total outstanding data to be synchronized in MB. You can calculate backlog data for the Remote Copy Async group by summing up the asyncOutsstanding value for all the volumes in the group. Defaults to -1. | [optional] 
**remote_volume_id** | **int, none_type** | Volume ID on the target system. | [optional] 
**remote_volume_name** | **str, none_type** | Volume name on the target system. | [optional] 
**resync_iteration** | **str, none_type** | A correlator used to determine the data consistency point of the resynchroniztion snapshot relative to the remote volume and/or snapshots. Returns &#39;NA&#39; if not set. | [optional] 
**resync_snapshot_name** | **str, none_type** | Snapshot indicating the starting point of the remote volume. The primary array uses this snapshot to determine which changes to synchronize to the secondary volume. The target array uses this snapshot as a recovery point if there is a resynchronization failure. | [optional] 
**sync_iteration** | **str, none_type** | A correlator used to determine the data consistency point of the synchronization snapshot relative to the remote volume and/or snapshots. Returns &#39;NA&#39; if not set. | [optional] 
**sync_percentage** | **int, none_type** | Synchronization percentage of the volume. | [optional] 
**sync_snapshot_name** | **str, none_type** | Snapshot indicating the destination point of the Remote Copy volume on successful completion of resynchronization. Upon completion of a resynchronization, the remote base volume mirrors this synchronization snapshot. This snapshot becomes the resync snapshot when resynchronization completes. | [optional] 
**sync_status** | **str, none_type** | Synchronization status of the volume. Can be New, Syncing, Synced, Not Synced, Stale, New Pre Synced, New Sync from Snap, Failsafe, Logging, New Pending, Pending Dismiss or Remote Pending Dismiss. Null if unset. | [optional] 
**target_name** | **str, none_type** | Target to which the volume group is mirrored. | [optional] 
**volume_iteration** | **str, none_type** | A correlator used to determine the data consistency point of the volume relative to the remote volume and/or snapshots. Returns &#39;NA&#39; if not set. | [optional] 
**volume_last_sync_time** | [**SyncTime**](SyncTime.md) |  | [optional] 
**volume_sync_length** | **int, none_type** | Volume synchronization total length. Returns -1 if unset | [optional] 
**volume_sync_offset** | **int, none_type** | Volume synchronization offset. Returns -1 if unset. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


