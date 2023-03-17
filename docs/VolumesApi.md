# greenlake-data-services.VolumesApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_get_clones**](VolumesApi.md#device_type1_get_clones) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/clones | Get the details of the clone volumes associated with a base volume identified by {volumeId} for Primera / Alletra 9K systems.
[**device_type1_promote_clone_volume**](VolumesApi.md#device_type1_promote_clone_volume) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/clones/{cloneId}/promote | Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_promote_snapshot**](VolumesApi.md#device_type1_promote_snapshot) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_resync_clone_volume**](VolumesApi.md#device_type1_resync_clone_volume) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/clones/{cloneId}/resync | Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
[**device_type1_snapshots_get_by_id**](VolumesApi.md#device_type1_snapshots_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Get details of snapshot identified by {snapshotId} for Volume identified by {volumeId} for Primera / Alletra 9K
[**device_type1_vlun_export**](VolumesApi.md#device_type1_vlun_export) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/export | Export vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_vlun_export_for_snapshot**](VolumesApi.md#device_type1_vlun_export_for_snapshot) | **POST** /api/v1/storage-systems/device-type1/{systemId}/snapshots/{snapshotId}/export | Export vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_vlun_unexport**](VolumesApi.md#device_type1_vlun_unexport) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/un-export | Unexport vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_vlun_unexport_for_snapshot**](VolumesApi.md#device_type1_vlun_unexport_for_snapshot) | **POST** /api/v1/storage-systems/device-type1/{systemId}/snapshots/{snapshotId}/un-export | Unexport vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_vluns_get_by_id**](VolumesApi.md#device_type1_vluns_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/vluns/{id} | Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K
[**device_type1_vluns_list**](VolumesApi.md#device_type1_vluns_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/vluns | Get details of vluns for Volume identified by {volumeId} for Primera / Alletra 9K
[**device_type1_volume_capacity_history_get_by_id**](VolumesApi.md#device_type1_volume_capacity_history_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/capacity-history | Get volume capacity trend data of Primera / Alletra 9K Volume identified by {id}
[**device_type1_volume_get_by_id**](VolumesApi.md#device_type1_volume_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id} | Get details of Primera / Alletra 9K Volume identified by {id}
[**device_type1_volume_performance_history_get_by_id**](VolumesApi.md#device_type1_volume_performance_history_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/performance-history | Get performance trend data of Primera / Alletra 9K Volume identified by {id}
[**device_type1_volume_performance_statistics_get_by_id**](VolumesApi.md#device_type1_volume_performance_statistics_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/performance-statistics | Get performance statistics of Primera / Alletra 9K Volume identified by {id}
[**device_type1_volume_snapshots_list**](VolumesApi.md#device_type1_volume_snapshots_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/snapshots | Get snapshot details of volume identified by {id} for Primera / Alletra 9K
[**device_type1_volumes_list**](VolumesApi.md#device_type1_volumes_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/volumes | Get all volumes details for Primera / Alletra 9K
[**device_type2_access_control_record_create**](VolumesApi.md#device_type2_access_control_record_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/access-control-records | Create Nimble / Alletra 6K access control record in system identified by {systemId}
[**device_type2_clone_volume_by_id**](VolumesApi.md#device_type2_clone_volume_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/clone | Create Nimble / Alletra 6K clone volume identified by {volumeId}.
[**device_type2_delete_snapshot_access_by_id**](VolumesApi.md#device_type2_delete_snapshot_access_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/snapshots/{snapshotId}/un-export | Delete access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}
[**device_type2_delete_volume_access_by_id**](VolumesApi.md#device_type2_delete_volume_access_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/un-export | Delete access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}
[**device_type2_edit_snapshot_by_id**](VolumesApi.md#device_type2_edit_snapshot_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/snapshots/actions/update | Edit Multiple Nimble / Alletra 6K snapshots in system identified by {systemId}
[**device_type2_edit_volume_by_id**](VolumesApi.md#device_type2_edit_volume_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId} | Edit  details of Nimble / Alletra 6K Volume identified by {volumeId}
[**device_type2_get_access_control_record_by_id**](VolumesApi.md#device_type2_get_access_control_record_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/access-control-records/{accessControlRecordId} | Get details of Nimble / Alletra 6K access-control-records identified by {accessControlRecordId}
[**device_type2_get_all_access_control_records**](VolumesApi.md#device_type2_get_all_access_control_records) | **GET** /api/v1/storage-systems/device-type2/{systemId}/access-control-records | Get all access-control-records details by Nimble / Alletra 6K
[**device_type2_get_all_snapshots_by_volume_id**](VolumesApi.md#device_type2_get_all_snapshots_by_volume_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/snapshots | Get all snapshots&#39; details of Nimble / Alletra 6K Volume identified by {volumeId}
[**device_type2_get_all_volumes**](VolumesApi.md#device_type2_get_all_volumes) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes | Get all volumes details for Nimble / Alletra 6K
[**device_type2_get_snapshot_by_id**](VolumesApi.md#device_type2_get_snapshot_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Get details of snapshot of Nimble / Alletra 6K Volume identified by {volumeId} by {snapshotId}
[**device_type2_get_volume_by_id**](VolumesApi.md#device_type2_get_volume_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId} | Get details of Nimble / Alletra 6K Volume identified by {volumeId}
[**device_type2_get_volume_capacity_history**](VolumesApi.md#device_type2_get_volume_capacity_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/capacity-history | Get volume capacity trend data of Nimble / Alletra 6K Volume identified by {volumeId}
[**device_type2_get_volume_performance_history**](VolumesApi.md#device_type2_get_volume_performance_history) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/performance-history | Get performance trend data of Nimble / Alletra 6K Volume identified by {id}
[**device_type2_get_volume_performance_statistics**](VolumesApi.md#device_type2_get_volume_performance_statistics) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/performance-statistics | Get performance statistics of Nimble / Alletra 6K Volume identified by {volumeId}
[**device_type2_move_volume**](VolumesApi.md#device_type2_move_volume) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/actions/move | Move Nimble / Alletra 6K volume identified by {volumeId} to another pool.
[**device_type2_provisioning_review**](VolumesApi.md#device_type2_provisioning_review) | **POST** /api/v1/storage-systems/device-type2/{systemId}/provisioning-review | Provisioning review for a storage system Nimble / Alletra 6K
[**device_type2_provisioning_worklow**](VolumesApi.md#device_type2_provisioning_worklow) | **POST** /api/v1/storage-systems/device-type2/{systemId}/provisioning | Create provisioning workflow for a Nimble / Alletra 6K storage system identified by {systemId}
[**device_type2_remove_access_control_record_by_id**](VolumesApi.md#device_type2_remove_access_control_record_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/access-control-records/{accessControlRecordId} | Remove access-control-record identified by {accessControlRecordId} from Nimble / Alletra 6K
[**device_type2_remove_snapshot_by_id**](VolumesApi.md#device_type2_remove_snapshot_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Remove Nimble / Alletra 6K snapshot in system identified by {snapshotId}
[**device_type2_remove_volume_by_id**](VolumesApi.md#device_type2_remove_volume_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId} | Remove volume identified by {volumeId} from Nimble / Alletra 6K
[**device_type2_restore_volume_by_id**](VolumesApi.md#device_type2_restore_volume_by_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/actions/restore | Restore Nimble / Alletra 6K volume identified by {volumeId} from a previous snapshot.
[**device_type2_snapshot_create**](VolumesApi.md#device_type2_snapshot_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/snapshots | Create Nimble / Alletra 6K snapshot in system identified by {systemId}
[**device_type2_snapshot_export**](VolumesApi.md#device_type2_snapshot_export) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/snapshots/{snapshotId}/export | Configure access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}
[**device_type2_volumes_create**](VolumesApi.md#device_type2_volumes_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes | Create Nimble / Alletra 6K volume in system identified by {systemId}
[**device_type2_volumes_export**](VolumesApi.md#device_type2_volumes_export) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volumes/{volumeId}/export | Configure access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}
[**snapshot_clone_create**](VolumesApi.md#snapshot_clone_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/snapshots/{snapshotId}/clone | Create a clone of a snapshot identified by {snapshotId} for Primera / Alletra 9K systems.
[**vluns_delete**](VolumesApi.md#vluns_delete) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/vluns/{id} | Remove vlun idenfied by {id} form volume identified by {volumeId} from Primera / Alletra 9K
[**volume_clone_create**](VolumesApi.md#volume_clone_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/clone | Create a clone volume identified by {id} for Primera / Alletra 9K systems.
[**volume_create**](VolumesApi.md#volume_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes | Create volume for a storage system Primera / Alletra 9K
[**volume_delete**](VolumesApi.md#volume_delete) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id} | Remove volume identified by {volumeId} from Primera / Alletra 9K
[**volume_edit**](VolumesApi.md#volume_edit) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id} | Edit volume identified by {volumeId} from Primera / Alletra 9K
[**volume_get_by_id**](VolumesApi.md#volume_get_by_id) | **GET** /api/v1/volumes/{id} | Get details of Volume identified by {id}
[**volume_list_for_system_by_system_id**](VolumesApi.md#volume_list_for_system_by_system_id) | **GET** /api/v1/storage-systems/{systemId}/volumes | Get details of volumes identified with {systemId}
[**volume_snapshot_create**](VolumesApi.md#volume_snapshot_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/volumes/{id}/snapshots | Create snapshot for volumes identified by {id}
[**volume_snapshot_get_by_id**](VolumesApi.md#volume_snapshot_get_by_id) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/volumes/{volumeId}/snapshots/{snapshotId} | Remove Primera / Alletra 9K snapshot in system identified by {snapshotId}
[**volumes_list**](VolumesApi.md#volumes_list) | **GET** /api/v1/volumes | Get all volumes


# **device_type1_get_clones**
> PrimeraVolumesList device_type1_get_clones(system_id, volume_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get the details of the clone volumes associated with a base volume identified by {volumeId} for Primera / Alletra 9K systems.

Get the details of the clone volumes associated with a base volume identified by {volumeId} for Primera / Alletra 9K systems.

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
volume_id = 'volume_id_example' # str | UID(volumeuid) of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter by Key. (optional)
sort = 'sort_example' # str | oData query to sort by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get the details of the clone volumes associated with a base volume identified by {volumeId} for Primera / Alletra 9K systems.
    api_response = api_instance.device_type1_get_clones(system_id, volume_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_get_clones: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraVolumesList**](PrimeraVolumesList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_promote_clone_volume**
> TaskResponse device_type1_promote_clone_volume(system_id, volume_id, clone_id, promote_clone_input=promote_clone_input)

Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
volume_id = 'volume_id_example' # str | UID(volumeuid) of the storage system
clone_id = 'clone_id_example' # str | UID of the clone
promote_clone_input = greenlake-data-services.PromoteCloneInput() # PromoteCloneInput |  (optional)

try:
    # Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_promote_clone_volume(system_id, volume_id, clone_id, promote_clone_input=promote_clone_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_promote_clone_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **clone_id** | **str**| UID of the clone | 
 **promote_clone_input** | [**PromoteCloneInput**](PromoteCloneInput.md)|  | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_promote_snapshot**
> TaskResponse device_type1_promote_snapshot(system_id, volume_id, snapshot_id, promote_snapshot_input=promote_snapshot_input)

Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
volume_id = 'volume_id_example' # str | UID(volumeuid) of the storage system
snapshot_id = 'snapshot_id_example' # str | UID of the snapshots
promote_snapshot_input = greenlake-data-services.PromoteSnapshotInput() # PromoteSnapshotInput |  (optional)

try:
    # Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_promote_snapshot(system_id, volume_id, snapshot_id, promote_snapshot_input=promote_snapshot_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_promote_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **promote_snapshot_input** | [**PromoteSnapshotInput**](PromoteSnapshotInput.md)|  | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_resync_clone_volume**
> TaskResponse device_type1_resync_clone_volume(system_id, volume_id, clone_id, resync_clone_volume_input=resync_clone_volume_input)

Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
volume_id = 'volume_id_example' # str | UID(volumeuid) of the storage system
clone_id = 'clone_id_example' # str | UID of the clone
resync_clone_volume_input = greenlake-data-services.ResyncCloneVolumeInput() # ResyncCloneVolumeInput |  (optional)

try:
    # Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_resync_clone_volume(system_id, volume_id, clone_id, resync_clone_volume_input=resync_clone_volume_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_resync_clone_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **clone_id** | **str**| UID of the clone | 
 **resync_clone_volume_input** | [**ResyncCloneVolumeInput**](ResyncCloneVolumeInput.md)|  | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_snapshots_get_by_id**
> SnapshotsListSingle device_type1_snapshots_get_by_id(system_id, volume_id, snapshot_id, select=select)

Get details of snapshot identified by {snapshotId} for Volume identified by {volumeId} for Primera / Alletra 9K

Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
volume_id = 'volume_id_example' # str | UID(volumeuid) of the storage system
snapshot_id = 'snapshot_id_example' # str | UID of the snapshots
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of snapshot identified by {snapshotId} for Volume identified by {volumeId} for Primera / Alletra 9K
    api_response = api_instance.device_type1_snapshots_get_by_id(system_id, volume_id, snapshot_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_snapshots_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**SnapshotsListSingle**](SnapshotsListSingle.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vlun_export**
> TaskResponse device_type1_vlun_export(system_id, id, vluns_create_input)

Export vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}

Export vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID(volumeuid) of the storage system
vluns_create_input = greenlake-data-services.VlunsCreateInput() # VlunsCreateInput | 

try:
    # Export vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_vlun_export(system_id, id, vluns_create_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_vlun_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **vluns_create_input** | [**VlunsCreateInput**](VlunsCreateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vlun_export_for_snapshot**
> TaskResponse device_type1_vlun_export_for_snapshot(system_id, snapshot_id, vluns_create_input)

Export vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}

Export vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
snapshot_id = 'snapshot_id_example' # str | UID of the snapshots
vluns_create_input = greenlake-data-services.VlunsCreateInput() # VlunsCreateInput | 

try:
    # Export vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_vlun_export_for_snapshot(system_id, snapshot_id, vluns_create_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_vlun_export_for_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **vluns_create_input** | [**VlunsCreateInput**](VlunsCreateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vlun_unexport**
> TaskResponse device_type1_vlun_unexport(system_id, id, un_export_vlun)

Unexport vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}

Unexport vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID(volumeuid) of the storage system
un_export_vlun = greenlake-data-services.UnExportVlun() # UnExportVlun | 

try:
    # Unexport vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_vlun_unexport(system_id, id, un_export_vlun)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_vlun_unexport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **un_export_vlun** | [**UnExportVlun**](UnExportVlun.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vlun_unexport_for_snapshot**
> TaskResponse device_type1_vlun_unexport_for_snapshot(system_id, snapshot_id, un_export_vlun)

Unexport vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}

Unexport vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
snapshot_id = 'snapshot_id_example' # str | UID of the snapshots
un_export_vlun = greenlake-data-services.UnExportVlun() # UnExportVlun | 

try:
    # Unexport vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_vlun_unexport_for_snapshot(system_id, snapshot_id, un_export_vlun)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_vlun_unexport_for_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **un_export_vlun** | [**UnExportVlun**](UnExportVlun.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vluns_get_by_id**
> VlunsListSingle device_type1_vluns_get_by_id(system_id, volume_id, id, select=select)

Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K

Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
volume_id = 'volume_id_example' # str | UID(volumeuid) of the storage system
id = 'id_example' # str | UID of the vlun
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K
    api_response = api_instance.device_type1_vluns_get_by_id(system_id, volume_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_vluns_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **id** | **str**| UID of the vlun | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**VlunsListSingle**](VlunsListSingle.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vluns_list**
> VlunsSummaryList device_type1_vluns_list(system_id, id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)

Get details of vluns for Volume identified by {volumeId} for Primera / Alletra 9K

Get details of vluns for Volume identified by {volumeId} for Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID(volumeuid) of the storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter by Key. (optional)
sort = 'sort_example' # str | Query to sort the response with specified key and order (optional)

try:
    # Get details of vluns for Volume identified by {volumeId} for Primera / Alletra 9K
    api_response = api_instance.device_type1_vluns_list(system_id, id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_vluns_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| Query to sort the response with specified key and order | [optional] 

### Return type

[**VlunsSummaryList**](VlunsSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_capacity_history_get_by_id**
> VolumeCapacityHistory device_type1_volume_capacity_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)

Get volume capacity trend data of Primera / Alletra 9K Volume identified by {id}

Get volume capacity trend data of Primera / Alletra 9K Volume identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID(volumeuid) of the storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
time_interval_min = 56 # int | It defines granularity in minutes. (optional)

try:
    # Get volume capacity trend data of Primera / Alletra 9K Volume identified by {id}
    api_response = api_instance.device_type1_volume_capacity_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_volume_capacity_history_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**VolumeCapacityHistory**](VolumeCapacityHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_get_by_id**
> PrimeraVolumeDetails device_type1_volume_get_by_id(system_id, id, select=select)

Get details of Primera / Alletra 9K Volume identified by {id}

Get details of Primera / Alletra 9K Volume identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID(volumeuid) of the storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Primera / Alletra 9K Volume identified by {id}
    api_response = api_instance.device_type1_volume_get_by_id(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_volume_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraVolumeDetails**](PrimeraVolumeDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_performance_history_get_by_id**
> VolumePerformanceHistory device_type1_volume_performance_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)

Get performance trend data of Primera / Alletra 9K Volume identified by {id}

Get performance trend data of Primera / Alletra 9K Volume identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID(volumeuid) of the storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
time_interval_min = 56 # int | It defines granularity in minutes. (optional)

try:
    # Get performance trend data of Primera / Alletra 9K Volume identified by {id}
    api_response = api_instance.device_type1_volume_performance_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_volume_performance_history_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**VolumePerformanceHistory**](VolumePerformanceHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_performance_statistics_get_by_id**
> VolumePerformance device_type1_volume_performance_statistics_get_by_id(system_id, id, select=select)

Get performance statistics of Primera / Alletra 9K Volume identified by {id}

Get performance statistics of Primera / Alletra 9K Volume identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID(volumeuid) of the storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get performance statistics of Primera / Alletra 9K Volume identified by {id}
    api_response = api_instance.device_type1_volume_performance_statistics_get_by_id(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_volume_performance_statistics_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**VolumePerformance**](VolumePerformance.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_snapshots_list**
> SnapshotsSummaryList device_type1_volume_snapshots_list(system_id, id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get snapshot details of volume identified by {id} for Primera / Alletra 9K

Get snapshot details of volume identified by {id} for Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID(volumeuid) of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter by Key. (optional)
sort = 'sort_example' # str | oData query to sort by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get snapshot details of volume identified by {id} for Primera / Alletra 9K
    api_response = api_instance.device_type1_volume_snapshots_list(system_id, id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_volume_snapshots_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**SnapshotsSummaryList**](SnapshotsSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volumes_list**
> PrimeraVolumesList device_type1_volumes_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volumes details for Primera / Alletra 9K

Get all volumes details for Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter by Key. (optional)
sort = 'sort_example' # str | oData query to sort by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all volumes details for Primera / Alletra 9K
    api_response = api_instance.device_type1_volumes_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type1_volumes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraVolumesList**](PrimeraVolumesList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_access_control_record_create**
> TaskResponse device_type2_access_control_record_create(system_id, nimble_create_access_control_record_input)

Create Nimble / Alletra 6K access control record in system identified by {systemId}

Create Nimble / Alletra 6K access control record in system identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_access_control_record_input = greenlake-data-services.NimbleCreateAccessControlRecordInput() # NimbleCreateAccessControlRecordInput | 

try:
    # Create Nimble / Alletra 6K access control record in system identified by {systemId}
    api_response = api_instance.device_type2_access_control_record_create(system_id, nimble_create_access_control_record_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_access_control_record_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_access_control_record_input** | [**NimbleCreateAccessControlRecordInput**](NimbleCreateAccessControlRecordInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_clone_volume_by_id**
> TaskResponse device_type2_clone_volume_by_id(system_id, volume_id, nimble_clone_volume_input)

Create Nimble / Alletra 6K clone volume identified by {volumeId}.

Create Nimble / Alletra 6K clone volume identified by {volumeId}.

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
nimble_clone_volume_input = greenlake-data-services.NimbleCloneVolumeInput() # NimbleCloneVolumeInput | 

try:
    # Create Nimble / Alletra 6K clone volume identified by {volumeId}.
    api_response = api_instance.device_type2_clone_volume_by_id(system_id, volume_id, nimble_clone_volume_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_clone_volume_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **nimble_clone_volume_input** | [**NimbleCloneVolumeInput**](NimbleCloneVolumeInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_delete_snapshot_access_by_id**
> TaskResponse device_type2_delete_snapshot_access_by_id(system_id, volume_id, snapshot_id, un_export_input)

Delete access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}

Delete access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
snapshot_id = 'snapshot_id_example' # str | Identifier of snapshot. A 42 digit hexadecimal number.
un_export_input = greenlake-data-services.UnExportInput() # UnExportInput | 

try:
    # Delete access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}
    api_response = api_instance.device_type2_delete_snapshot_access_by_id(system_id, volume_id, snapshot_id, un_export_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_delete_snapshot_access_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **snapshot_id** | **str**| Identifier of snapshot. A 42 digit hexadecimal number. | 
 **un_export_input** | [**UnExportInput**](UnExportInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_delete_volume_access_by_id**
> TaskResponse device_type2_delete_volume_access_by_id(system_id, volume_id, un_export_input)

Delete access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}

Delete access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
un_export_input = greenlake-data-services.UnExportInput() # UnExportInput | 

try:
    # Delete access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}
    api_response = api_instance.device_type2_delete_volume_access_by_id(system_id, volume_id, un_export_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_delete_volume_access_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **un_export_input** | [**UnExportInput**](UnExportInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_snapshot_by_id**
> TaskResponse device_type2_edit_snapshot_by_id(system_id, nimble_edit_multiple_snapshot_input)

Edit Multiple Nimble / Alletra 6K snapshots in system identified by {systemId}

Edit Multiple Nimble / Alletra 6K snapshots in system identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_edit_multiple_snapshot_input = greenlake-data-services.NimbleEditMultipleSnapshotInput() # NimbleEditMultipleSnapshotInput | 

try:
    # Edit Multiple Nimble / Alletra 6K snapshots in system identified by {systemId}
    api_response = api_instance.device_type2_edit_snapshot_by_id(system_id, nimble_edit_multiple_snapshot_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_edit_snapshot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_edit_multiple_snapshot_input** | [**NimbleEditMultipleSnapshotInput**](NimbleEditMultipleSnapshotInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_volume_by_id**
> TaskResponse device_type2_edit_volume_by_id(system_id, volume_id, nimble_edit_volume_input)

Edit  details of Nimble / Alletra 6K Volume identified by {volumeId}

Edit  details of Nimble / Alletra 6K Volume identified by {volumeId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
nimble_edit_volume_input = greenlake-data-services.NimbleEditVolumeInput() # NimbleEditVolumeInput | 

try:
    # Edit  details of Nimble / Alletra 6K Volume identified by {volumeId}
    api_response = api_instance.device_type2_edit_volume_by_id(system_id, volume_id, nimble_edit_volume_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_edit_volume_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **nimble_edit_volume_input** | [**NimbleEditVolumeInput**](NimbleEditVolumeInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_access_control_record_by_id**
> NimbleAccessControlRecordDetailsWithRequestUri device_type2_get_access_control_record_by_id(system_id, access_control_record_id, select=select)

Get details of Nimble / Alletra 6K access-control-records identified by {accessControlRecordId}

Get details of Nimble / Alletra 6K access-control-records identified by {accessControlRecordId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
access_control_record_id = 'access_control_record_id_example' # str | ID of the Access Control Record . A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K access-control-records identified by {accessControlRecordId}
    api_response = api_instance.device_type2_get_access_control_record_by_id(system_id, access_control_record_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_get_access_control_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **access_control_record_id** | **str**| ID of the Access Control Record . A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleAccessControlRecordDetailsWithRequestUri**](NimbleAccessControlRecordDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_access_control_records**
> NimbleAccessControlRecordList device_type2_get_all_access_control_records(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all access-control-records details by Nimble / Alletra 6K

Get all access-control-records details by Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter Access Control Record  by Key. (optional)
sort = 'sort_example' # str | oData query to sort Access Control Record  resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all access-control-records details by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_access_control_records(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_get_all_access_control_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter Access Control Record  by Key. | [optional] 
 **sort** | **str**| oData query to sort Access Control Record  resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleAccessControlRecordList**](NimbleAccessControlRecordList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_snapshots_by_volume_id**
> NimbleSnapshotList device_type2_get_all_snapshots_by_volume_id(system_id, volume_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all snapshots' details of Nimble / Alletra 6K Volume identified by {volumeId}

Get all snapshots' details of Nimble / Alletra 6K Volume identified by {volumeId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter snapshots by Key. (optional)
sort = 'sort_example' # str | oData query to sort snapshots resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all snapshots' details of Nimble / Alletra 6K Volume identified by {volumeId}
    api_response = api_instance.device_type2_get_all_snapshots_by_volume_id(system_id, volume_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_get_all_snapshots_by_volume_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter snapshots by Key. | [optional] 
 **sort** | **str**| oData query to sort snapshots resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleSnapshotList**](NimbleSnapshotList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_volumes**
> NimbleVolumesList device_type2_get_all_volumes(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volumes details for Nimble / Alletra 6K

Get all volumes details for Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter volumes by Key. (optional)
sort = 'sort_example' # str | oData query to sort volumes resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all volumes details for Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_volumes(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_get_all_volumes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter volumes by Key. | [optional] 
 **sort** | **str**| oData query to sort volumes resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleVolumesList**](NimbleVolumesList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_snapshot_by_id**
> NimbleSnapshotDetails device_type2_get_snapshot_by_id(system_id, volume_id, snapshot_id, select=select)

Get details of snapshot of Nimble / Alletra 6K Volume identified by {volumeId} by {snapshotId}

Get details of snapshot of Nimble / Alletra 6K Volume identified by {volumeId} by {snapshotId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
snapshot_id = 'snapshot_id_example' # str | Identifier of snapshot. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of snapshot of Nimble / Alletra 6K Volume identified by {volumeId} by {snapshotId}
    api_response = api_instance.device_type2_get_snapshot_by_id(system_id, volume_id, snapshot_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_get_snapshot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **snapshot_id** | **str**| Identifier of snapshot. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleSnapshotDetails**](NimbleSnapshotDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_volume_by_id**
> NimbleVolumeDetails device_type2_get_volume_by_id(system_id, volume_id, select=select)

Get details of Nimble / Alletra 6K Volume identified by {volumeId}

Get details of Nimble / Alletra 6K Volume identified by {volumeId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K Volume identified by {volumeId}
    api_response = api_instance.device_type2_get_volume_by_id(system_id, volume_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_get_volume_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleVolumeDetails**](NimbleVolumeDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_volume_capacity_history**
> NimblevolumeCapacityHistory device_type2_get_volume_capacity_history(system_id, volume_id, select=select, range=range, time_interval_min=time_interval_min)

Get volume capacity trend data of Nimble / Alletra 6K Volume identified by {volumeId}

Get volume capacity trend data of Nimble / Alletra 6K Volume identified by {volumeId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
time_interval_min = 56 # int | It defines granularity in minutes. (optional)

try:
    # Get volume capacity trend data of Nimble / Alletra 6K Volume identified by {volumeId}
    api_response = api_instance.device_type2_get_volume_capacity_history(system_id, volume_id, select=select, range=range, time_interval_min=time_interval_min)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_get_volume_capacity_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**NimblevolumeCapacityHistory**](NimblevolumeCapacityHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_volume_performance_history**
> NimblevolumePerformanceHistory device_type2_get_volume_performance_history(system_id, volume_id, select=select, range=range, time_interval_min=time_interval_min)

Get performance trend data of Nimble / Alletra 6K Volume identified by {id}

Get performance trend data of Nimble / Alletra 6K Volume identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
range = 'range_example' # str | range will define start and end time in which query has to be made. (optional)
time_interval_min = 56 # int | It defines granularity in minutes. (optional)

try:
    # Get performance trend data of Nimble / Alletra 6K Volume identified by {id}
    api_response = api_instance.device_type2_get_volume_performance_history(system_id, volume_id, select=select, range=range, time_interval_min=time_interval_min)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_get_volume_performance_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **range** | **str**| range will define start and end time in which query has to be made. | [optional] 
 **time_interval_min** | **int**| It defines granularity in minutes. | [optional] 

### Return type

[**NimblevolumePerformanceHistory**](NimblevolumePerformanceHistory.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_volume_performance_statistics**
> VolPerformance device_type2_get_volume_performance_statistics(system_id, volume_id, select=select)

Get performance statistics of Nimble / Alletra 6K Volume identified by {volumeId}

Get performance statistics of Nimble / Alletra 6K Volume identified by {volumeId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get performance statistics of Nimble / Alletra 6K Volume identified by {volumeId}
    api_response = api_instance.device_type2_get_volume_performance_statistics(system_id, volume_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_get_volume_performance_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**VolPerformance**](VolPerformance.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_move_volume**
> TaskResponse device_type2_move_volume(system_id, volume_id, nimble_move_volume_to_another_pool_input)

Move Nimble / Alletra 6K volume identified by {volumeId} to another pool.

Move Nimble / Alletra 6K volume identified by {volumeId} to another pool.

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
nimble_move_volume_to_another_pool_input = greenlake-data-services.NimbleMoveVolumeToAnotherPoolInput() # NimbleMoveVolumeToAnotherPoolInput | 

try:
    # Move Nimble / Alletra 6K volume identified by {volumeId} to another pool.
    api_response = api_instance.device_type2_move_volume(system_id, volume_id, nimble_move_volume_to_another_pool_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_move_volume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **nimble_move_volume_to_another_pool_input** | [**NimbleMoveVolumeToAnotherPoolInput**](NimbleMoveVolumeToAnotherPoolInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_provisioning_review**
> NimbleHostReviewOutput device_type2_provisioning_review(system_id, nimble_host_review_input)

Provisioning review for a storage system Nimble / Alletra 6K

Provisioning review for a storage system Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_host_review_input = greenlake-data-services.NimbleHostReviewInput() # NimbleHostReviewInput | 

try:
    # Provisioning review for a storage system Nimble / Alletra 6K
    api_response = api_instance.device_type2_provisioning_review(system_id, nimble_host_review_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_provisioning_review: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_host_review_input** | [**NimbleHostReviewInput**](NimbleHostReviewInput.md)|  | 

### Return type

[**NimbleHostReviewOutput**](NimbleHostReviewOutput.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_provisioning_worklow**
> TaskResponse device_type2_provisioning_worklow(system_id, nimble_create_volumes_workflow_input)

Create provisioning workflow for a Nimble / Alletra 6K storage system identified by {systemId}

Create provisioning workflow for a Nimble / Alletra 6K storage system identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_volumes_workflow_input = greenlake-data-services.NimbleCreateVolumesWorkflowInput() # NimbleCreateVolumesWorkflowInput | 

try:
    # Create provisioning workflow for a Nimble / Alletra 6K storage system identified by {systemId}
    api_response = api_instance.device_type2_provisioning_worklow(system_id, nimble_create_volumes_workflow_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_provisioning_worklow: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_volumes_workflow_input** | [**NimbleCreateVolumesWorkflowInput**](NimbleCreateVolumesWorkflowInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_access_control_record_by_id**
> TaskResponse device_type2_remove_access_control_record_by_id(system_id, access_control_record_id)

Remove access-control-record identified by {accessControlRecordId} from Nimble / Alletra 6K

Remove access-control-record identified by {accessControlRecordId} from Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
access_control_record_id = 'access_control_record_id_example' # str | Identifier of Access Control Record. A 42 digit hexadecimal number.

try:
    # Remove access-control-record identified by {accessControlRecordId} from Nimble / Alletra 6K
    api_response = api_instance.device_type2_remove_access_control_record_by_id(system_id, access_control_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_remove_access_control_record_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **access_control_record_id** | **str**| Identifier of Access Control Record. A 42 digit hexadecimal number. | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_snapshot_by_id**
> TaskResponse device_type2_remove_snapshot_by_id(system_id, volume_id, snapshot_id, force=force)

Remove Nimble / Alletra 6K snapshot in system identified by {snapshotId}

Remove Nimble / Alletra 6K snapshot in system identified by {snapshotId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
snapshot_id = 'snapshot_id_example' # str | Identifier of snapshot. A 42 digit hexadecimal number.
force = True # bool | Make snapshot offline and remove. (optional)

try:
    # Remove Nimble / Alletra 6K snapshot in system identified by {snapshotId}
    api_response = api_instance.device_type2_remove_snapshot_by_id(system_id, volume_id, snapshot_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_remove_snapshot_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **snapshot_id** | **str**| Identifier of snapshot. A 42 digit hexadecimal number. | 
 **force** | **bool**| Make snapshot offline and remove. | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_volume_by_id**
> TaskResponse device_type2_remove_volume_by_id(system_id, volume_id, offline=offline, force=force)

Remove volume identified by {volumeId} from Nimble / Alletra 6K

Remove volume identified by {volumeId} from Nimble / Alletra 6K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
offline = True # bool | Make volume offline and delete. Deprecated - Use force instead of offline. (optional)
force = True # bool | Make volume and associated snapshots offline, stop protection and delete. (optional)

try:
    # Remove volume identified by {volumeId} from Nimble / Alletra 6K
    api_response = api_instance.device_type2_remove_volume_by_id(system_id, volume_id, offline=offline, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_remove_volume_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **offline** | **bool**| Make volume offline and delete. Deprecated - Use force instead of offline. | [optional] 
 **force** | **bool**| Make volume and associated snapshots offline, stop protection and delete. | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_restore_volume_by_id**
> TaskResponse device_type2_restore_volume_by_id(system_id, volume_id, nimble_restore_volume_input)

Restore Nimble / Alletra 6K volume identified by {volumeId} from a previous snapshot.

Restore Nimble / Alletra 6K volume identified by {volumeId} from a previous snapshot.

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
nimble_restore_volume_input = greenlake-data-services.NimbleRestoreVolumeInput() # NimbleRestoreVolumeInput | 

try:
    # Restore Nimble / Alletra 6K volume identified by {volumeId} from a previous snapshot.
    api_response = api_instance.device_type2_restore_volume_by_id(system_id, volume_id, nimble_restore_volume_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_restore_volume_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **nimble_restore_volume_input** | [**NimbleRestoreVolumeInput**](NimbleRestoreVolumeInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_snapshot_create**
> TaskResponse device_type2_snapshot_create(system_id, volume_id, nimble_create_snapshot_input)

Create Nimble / Alletra 6K snapshot in system identified by {systemId}

Create Nimble / Alletra 6K snapshot in system identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
nimble_create_snapshot_input = greenlake-data-services.NimbleCreateSnapshotInput() # NimbleCreateSnapshotInput | 

try:
    # Create Nimble / Alletra 6K snapshot in system identified by {systemId}
    api_response = api_instance.device_type2_snapshot_create(system_id, volume_id, nimble_create_snapshot_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_snapshot_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **nimble_create_snapshot_input** | [**NimbleCreateSnapshotInput**](NimbleCreateSnapshotInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_snapshot_export**
> TaskResponse device_type2_snapshot_export(system_id, volume_id, snapshot_id, export_input)

Configure access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}

Configure access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
snapshot_id = 'snapshot_id_example' # str | Identifier of snapshot. A 42 digit hexadecimal number.
export_input = greenlake-data-services.ExportInput() # ExportInput | 

try:
    # Configure access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}
    api_response = api_instance.device_type2_snapshot_export(system_id, volume_id, snapshot_id, export_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_snapshot_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **snapshot_id** | **str**| Identifier of snapshot. A 42 digit hexadecimal number. | 
 **export_input** | [**ExportInput**](ExportInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_volumes_create**
> TaskResponse device_type2_volumes_create(system_id, nimble_create_volume_input)

Create Nimble / Alletra 6K volume in system identified by {systemId}

Create Nimble / Alletra 6K volume in system identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_volume_input = greenlake-data-services.NimbleCreateVolumeInput() # NimbleCreateVolumeInput | 

try:
    # Create Nimble / Alletra 6K volume in system identified by {systemId}
    api_response = api_instance.device_type2_volumes_create(system_id, nimble_create_volume_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_volumes_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_volume_input** | [**NimbleCreateVolumeInput**](NimbleCreateVolumeInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_volumes_export**
> TaskResponse device_type2_volumes_export(system_id, volume_id, export_input)

Configure access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}

Configure access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_id = 'volume_id_example' # str | Identifier of volume. A 42 digit hexadecimal number.
export_input = greenlake-data-services.ExportInput() # ExportInput | 

try:
    # Configure access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}
    api_response = api_instance.device_type2_volumes_export(system_id, volume_id, export_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->device_type2_volumes_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_id** | **str**| Identifier of volume. A 42 digit hexadecimal number. | 
 **export_input** | [**ExportInput**](ExportInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_clone_create**
> TaskResponse snapshot_clone_create(system_id, snapshot_id, create_clone_snapshot_input)

Create a clone of a snapshot identified by {snapshotId} for Primera / Alletra 9K systems.

Create a clone of a snapshot identified by {snapshotId} for Primera / Alletra 9K systems.

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
snapshot_id = 'snapshot_id_example' # str | UID of the snapshots
create_clone_snapshot_input = greenlake-data-services.CreateCloneSnapshotInput() # CreateCloneSnapshotInput | 

try:
    # Create a clone of a snapshot identified by {snapshotId} for Primera / Alletra 9K systems.
    api_response = api_instance.snapshot_clone_create(system_id, snapshot_id, create_clone_snapshot_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->snapshot_clone_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **snapshot_id** | **str**| UID of the snapshots | 
 **create_clone_snapshot_input** | [**CreateCloneSnapshotInput**](CreateCloneSnapshotInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vluns_delete**
> TaskResponse vluns_delete(system_id, volume_id, id)

Remove vlun idenfied by {id} form volume identified by {volumeId} from Primera / Alletra 9K

Remove vlun idenfied by {id} form volume identified by {volumeId} from Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
volume_id = 'volume_id_example' # str | UID(volumeuid) of the storage system
id = 'id_example' # str | UID of the vlun

try:
    # Remove vlun idenfied by {id} form volume identified by {volumeId} from Primera / Alletra 9K
    api_response = api_instance.vluns_delete(system_id, volume_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->vluns_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **id** | **str**| UID of the vlun | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_clone_create**
> TaskResponse volume_clone_create(system_id, id, create_clone_volume_input)

Create a clone volume identified by {id} for Primera / Alletra 9K systems.

Create a clone volume identified by {id} for Primera / Alletra 9K systems.

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID(volumeuid) of the storage system
create_clone_volume_input = greenlake-data-services.CreateCloneVolumeInput() # CreateCloneVolumeInput | 

try:
    # Create a clone volume identified by {id} for Primera / Alletra 9K systems.
    api_response = api_instance.volume_clone_create(system_id, id, create_clone_volume_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->volume_clone_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **create_clone_volume_input** | [**CreateCloneVolumeInput**](CreateCloneVolumeInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_create**
> TaskResponse volume_create(system_id, create_volume_input)

Create volume for a storage system Primera / Alletra 9K

Create volume for a storage system Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
create_volume_input = greenlake-data-services.CreateVolumeInput() # CreateVolumeInput | 

try:
    # Create volume for a storage system Primera / Alletra 9K
    api_response = api_instance.volume_create(system_id, create_volume_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->volume_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **create_volume_input** | [**CreateVolumeInput**](CreateVolumeInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_delete**
> TaskResponse volume_delete(system_id, id, un_export=un_export, cascade=cascade)

Remove volume identified by {volumeId} from Primera / Alletra 9K

Remove volume identified by {volumeId} from Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID(volumeuid) of the storage system
un_export = True # bool | UnExport Host,HostSet and delete volume (optional)
cascade = True # bool | Delete snapshot and volume (optional)

try:
    # Remove volume identified by {volumeId} from Primera / Alletra 9K
    api_response = api_instance.volume_delete(system_id, id, un_export=un_export, cascade=cascade)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->volume_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **un_export** | **bool**| UnExport Host,HostSet and delete volume | [optional] 
 **cascade** | **bool**| Delete snapshot and volume | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_edit**
> TaskResponse volume_edit(system_id, id, volume_put)

Edit volume identified by {volumeId} from Primera / Alletra 9K

Edit volume identified by {volumeId} from Primera / Alletra 9K

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID(volumeuid) of the storage system
volume_put = greenlake-data-services.VolumePut() # VolumePut | 

try:
    # Edit volume identified by {volumeId} from Primera / Alletra 9K
    api_response = api_instance.volume_edit(system_id, id, volume_put)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->volume_edit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **volume_put** | [**VolumePut**](VolumePut.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_get_by_id**
> FleetVolumeDetails volume_get_by_id(id, select=select)

Get details of Volume identified by {id}

Get details of Volume identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
id = 'id_example' # str | UID(volumeuid) of the storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Volume identified by {id}
    api_response = api_instance.volume_get_by_id(id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->volume_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UID(volumeuid) of the storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetVolumeDetails**](FleetVolumeDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_list_for_system_by_system_id**
> FleetVolumesList volume_list_for_system_by_system_id(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get details of volumes identified with {systemId}

Get details of volumes identified with {systemId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter by Key. (optional)
sort = 'sort_example' # str | oData query to sort by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of volumes identified with {systemId}
    api_response = api_instance.volume_list_for_system_by_system_id(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->volume_list_for_system_by_system_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetVolumesList**](FleetVolumesList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_snapshot_create**
> TaskResponse volume_snapshot_create(system_id, id, volume_post)

Create snapshot for volumes identified by {id}

Create snapshot for volumes identified by {id}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID(volumeuid) of the storage system
volume_post = greenlake-data-services.VolumePost() # VolumePost | 

try:
    # Create snapshot for volumes identified by {id}
    api_response = api_instance.volume_snapshot_create(system_id, id, volume_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->volume_snapshot_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID(volumeuid) of the storage system | 
 **volume_post** | [**VolumePost**](VolumePost.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_snapshot_get_by_id**
> TaskResponse volume_snapshot_get_by_id(system_id, volume_id, snapshot_id, force=force)

Remove Primera / Alletra 9K snapshot in system identified by {snapshotId}

Remove Primera / Alletra 9K snapshot in system identified by {snapshotId}

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
volume_id = 'volume_id_example' # str | UID(volumeuid) of the storage system
snapshot_id = 'snapshot_id_example' # str | Identifier of snapshot.
force = True # bool | Make snapshot offline and remove. (optional)

try:
    # Remove Primera / Alletra 9K snapshot in system identified by {snapshotId}
    api_response = api_instance.volume_snapshot_get_by_id(system_id, volume_id, snapshot_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->volume_snapshot_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **volume_id** | **str**| UID(volumeuid) of the storage system | 
 **snapshot_id** | **str**| Identifier of snapshot. | 
 **force** | **bool**| Make snapshot offline and remove. | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumes_list**
> FleetVolumesList volumes_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volumes

Get all volumes

### Example
```python
from __future__ import print_function
import time
import greenlake-data-services
from greenlake-data-services.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: JWTAuth
configuration = greenlake-data-services.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = greenlake-data-services.VolumesApi(greenlake-data-services.ApiClient(configuration))
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter by Key. (optional)
sort = 'sort_example' # str | oData query to sort by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all volumes
    api_response = api_instance.volumes_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumesApi->volumes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetVolumesList**](FleetVolumesList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

