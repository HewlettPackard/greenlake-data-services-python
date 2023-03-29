# greenlake_data_services.VolumesApi

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
> PrimeraVolumesList device_type1_get_clones(system_id, volume_id)

Get the details of the clone volumes associated with a base volume identified by {volumeId} for Primera / Alletra 9K systems.

Get the details of the clone volumes associated with a base volume identified by {volumeId} for Primera / Alletra 9K systems.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.primera_volumes_list import PrimeraVolumesList
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    volume_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "name eq array1 and wwn eq 2FF70002AC018D94" # str | oData query to filter by Key. (optional)
    sort = "systemWWN desc" # str | oData query to sort by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the details of the clone volumes associated with a base volume identified by {volumeId} for Primera / Alletra 9K systems.
        api_response = api_instance.device_type1_get_clones(system_id, volume_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_get_clones: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the details of the clone volumes associated with a base volume identified by {volumeId} for Primera / Alletra 9K systems.
        api_response = api_instance.device_type1_get_clones(system_id, volume_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_promote_clone_volume**
> TaskResponse device_type1_promote_clone_volume(system_id, volume_id, clone_id)

Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.promote_clone_input import PromoteCloneInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    volume_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    clone_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID of the clone
    promote_clone_input = PromoteCloneInput(
        priority=ClonePriority("PRIORITYTYPE_MED"),
    ) # PromoteCloneInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_promote_clone_volume(system_id, volume_id, clone_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_promote_clone_volume: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Promote a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_promote_clone_volume(system_id, volume_id, clone_id, promote_clone_input=promote_clone_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_promote_snapshot**
> TaskResponse device_type1_promote_snapshot(system_id, volume_id, snapshot_id)

Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.promote_snapshot_input import PromoteSnapshotInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    volume_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    snapshot_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID of the snapshots
    promote_snapshot_input = PromoteSnapshotInput(
        pri=Priority("PRIORITYTYPE_HIGH"),
        target="volume1",
    ) # PromoteSnapshotInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_promote_snapshot(system_id, volume_id, snapshot_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_promote_snapshot: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Promote a snapshot identified by {snapshotId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_promote_snapshot(system_id, volume_id, snapshot_id, promote_snapshot_input=promote_snapshot_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_resync_clone_volume**
> TaskResponse device_type1_resync_clone_volume(system_id, volume_id, clone_id)

Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.resync_clone_volume_input import ResyncCloneVolumeInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    volume_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    clone_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID of the clone
    resync_clone_volume_input = ResyncCloneVolumeInput(
        priority=ClonePriority("PRIORITYTYPE_MED"),
    ) # ResyncCloneVolumeInput |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_resync_clone_volume(system_id, volume_id, clone_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_resync_clone_volume: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Resynchronize a clone volume identified by {cloneId} of a volume identified by {volumeId} on storage system Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_resync_clone_volume(system_id, volume_id, clone_id, resync_clone_volume_input=resync_clone_volume_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_snapshots_get_by_id**
> SnapshotsListSingle device_type1_snapshots_get_by_id(system_id, volume_id, snapshot_id)

Get details of snapshot identified by {snapshotId} for Volume identified by {volumeId} for Primera / Alletra 9K

Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.snapshots_list_single import SnapshotsListSingle
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    volume_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    snapshot_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID of the snapshots
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of snapshot identified by {snapshotId} for Volume identified by {volumeId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_snapshots_get_by_id(system_id, volume_id, snapshot_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_snapshots_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of snapshot identified by {snapshotId} for Volume identified by {volumeId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_snapshots_get_by_id(system_id, volume_id, snapshot_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vlun_export**
> TaskResponse device_type1_vlun_export(system_id, id, vluns_create_input)

Export vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}

Export vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.vluns_create_input import VlunsCreateInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    vluns_create_input = VlunsCreateInput(
        auto_lun=True,
        host_group_ids=[
            "host_group_ids_example",
        ],
        max_auto_lun=1,
        no_vcn=True,
        override=True,
        position="position_1",
        proximity="PRIMARY",
    ) # VlunsCreateInput | 

    # example passing only required values which don't have defaults set
    try:
        # Export vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_vlun_export(system_id, id, vluns_create_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vlun_export_for_snapshot**
> TaskResponse device_type1_vlun_export_for_snapshot(system_id, snapshot_id, vluns_create_input)

Export vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}

Export vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.vluns_create_input import VlunsCreateInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    snapshot_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID of the snapshots
    vluns_create_input = VlunsCreateInput(
        auto_lun=True,
        host_group_ids=[
            "host_group_ids_example",
        ],
        max_auto_lun=1,
        no_vcn=True,
        override=True,
        position="position_1",
        proximity="PRIMARY",
    ) # VlunsCreateInput | 

    # example passing only required values which don't have defaults set
    try:
        # Export vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_vlun_export_for_snapshot(system_id, snapshot_id, vluns_create_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vlun_unexport**
> TaskResponse device_type1_vlun_unexport(system_id, id, un_export_vlun)

Unexport vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}

Unexport vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.un_export_vlun import UnExportVlun
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    un_export_vlun = UnExportVlun(
        host_group_ids=["host Group1","Host Group2"],
    ) # UnExportVlun | 

    # example passing only required values which don't have defaults set
    try:
        # Unexport vlun for volume identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_vlun_unexport(system_id, id, un_export_vlun)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vlun_unexport_for_snapshot**
> TaskResponse device_type1_vlun_unexport_for_snapshot(system_id, snapshot_id, un_export_vlun)

Unexport vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}

Unexport vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.un_export_vlun import UnExportVlun
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    snapshot_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID of the snapshots
    un_export_vlun = UnExportVlun(
        host_group_ids=["host Group1","Host Group2"],
    ) # UnExportVlun | 

    # example passing only required values which don't have defaults set
    try:
        # Unexport vlun for snapshot identified by {id} from Primera / Alletra 9K identified by {systemId}
        api_response = api_instance.device_type1_vlun_unexport_for_snapshot(system_id, snapshot_id, un_export_vlun)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vluns_get_by_id**
> VlunsListSingle device_type1_vluns_get_by_id(system_id, volume_id, id)

Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K

Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.vluns_list_single import VlunsListSingle
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    volume_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID of the vlun
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_vluns_get_by_id(system_id, volume_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_vluns_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of vlun identified by {id} for Volume identified by {volumeId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_vluns_get_by_id(system_id, volume_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_vluns_list**
> VlunsSummaryList device_type1_vluns_list(system_id, id)

Get details of vluns for Volume identified by {volumeId} for Primera / Alletra 9K

Get details of vluns for Volume identified by {volumeId} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.vluns_summary_list import VlunsSummaryList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "name eq array1 and wwn eq 2FF70002AC018D94" # str | oData query to filter by Key. (optional)
    sort = "id asc,name desc" # str | Query to sort the response with specified key and order (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of vluns for Volume identified by {volumeId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_vluns_list(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_vluns_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of vluns for Volume identified by {volumeId} for Primera / Alletra 9K
        api_response = api_instance.device_type1_vluns_list(system_id, id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_capacity_history_get_by_id**
> VolumeCapacityHistory device_type1_volume_capacity_history_get_by_id(system_id, id)

Get volume capacity trend data of Primera / Alletra 9K Volume identified by {id}

Get volume capacity trend data of Primera / Alletra 9K Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.volume_capacity_history import VolumeCapacityHistory
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    range = "startTime eq 1605063600 and endTime eq 1605186000" # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get volume capacity trend data of Primera / Alletra 9K Volume identified by {id}
        api_response = api_instance.device_type1_volume_capacity_history_get_by_id(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_volume_capacity_history_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get volume capacity trend data of Primera / Alletra 9K Volume identified by {id}
        api_response = api_instance.device_type1_volume_capacity_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_get_by_id**
> PrimeraVolumeDetails device_type1_volume_get_by_id(system_id, id)

Get details of Primera / Alletra 9K Volume identified by {id}

Get details of Primera / Alletra 9K Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.primera_volume_details import PrimeraVolumeDetails
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Primera / Alletra 9K Volume identified by {id}
        api_response = api_instance.device_type1_volume_get_by_id(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_volume_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Primera / Alletra 9K Volume identified by {id}
        api_response = api_instance.device_type1_volume_get_by_id(system_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_performance_history_get_by_id**
> VolumePerformanceHistory device_type1_volume_performance_history_get_by_id(system_id, id)

Get performance trend data of Primera / Alletra 9K Volume identified by {id}

Get performance trend data of Primera / Alletra 9K Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.volume_performance_history import VolumePerformanceHistory
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    range = "startTime eq 1605063600 and endTime eq 1605186000" # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get performance trend data of Primera / Alletra 9K Volume identified by {id}
        api_response = api_instance.device_type1_volume_performance_history_get_by_id(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_volume_performance_history_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get performance trend data of Primera / Alletra 9K Volume identified by {id}
        api_response = api_instance.device_type1_volume_performance_history_get_by_id(system_id, id, select=select, range=range, time_interval_min=time_interval_min)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_performance_statistics_get_by_id**
> VolumePerformance device_type1_volume_performance_statistics_get_by_id(system_id, id)

Get performance statistics of Primera / Alletra 9K Volume identified by {id}

Get performance statistics of Primera / Alletra 9K Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.volume_performance import VolumePerformance
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get performance statistics of Primera / Alletra 9K Volume identified by {id}
        api_response = api_instance.device_type1_volume_performance_statistics_get_by_id(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_volume_performance_statistics_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get performance statistics of Primera / Alletra 9K Volume identified by {id}
        api_response = api_instance.device_type1_volume_performance_statistics_get_by_id(system_id, id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_snapshots_list**
> SnapshotsSummaryList device_type1_volume_snapshots_list(system_id, id)

Get snapshot details of volume identified by {id} for Primera / Alletra 9K

Get snapshot details of volume identified by {id} for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.snapshots_summary_list import SnapshotsSummaryList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "name eq array1 and wwn eq 2FF70002AC018D94" # str | oData query to filter by Key. (optional)
    sort = "systemWWN desc" # str | oData query to sort by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get snapshot details of volume identified by {id} for Primera / Alletra 9K
        api_response = api_instance.device_type1_volume_snapshots_list(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_volume_snapshots_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get snapshot details of volume identified by {id} for Primera / Alletra 9K
        api_response = api_instance.device_type1_volume_snapshots_list(system_id, id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volumes_list**
> PrimeraVolumesList device_type1_volumes_list(system_id)

Get all volumes details for Primera / Alletra 9K

Get all volumes details for Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.primera_volumes_list import PrimeraVolumesList
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "name eq array1 and wwn eq 2FF70002AC018D94" # str | oData query to filter by Key. (optional)
    sort = "systemWWN desc" # str | oData query to sort by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all volumes details for Primera / Alletra 9K
        api_response = api_instance.device_type1_volumes_list(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type1_volumes_list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all volumes details for Primera / Alletra 9K
        api_response = api_instance.device_type1_volumes_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_access_control_record_create**
> TaskResponse device_type2_access_control_record_create(system_id, nimble_create_access_control_record_input)

Create Nimble / Alletra 6K access control record in system identified by {systemId}

Create Nimble / Alletra 6K access control record in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_create_access_control_record_input import NimbleCreateAccessControlRecordInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_create_access_control_record_input = NimbleCreateAccessControlRecordInput(
        apply_to="pe",
        chap_user_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        initiator_group_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        lun=8,
        pe_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        pe_ids=[
            "2a0df0fe6f7dc7bb16000000000000000000004817",
        ],
        snap_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        vol_id="064323bdd90b39c3a7000000000000000000000016",
    ) # NimbleCreateAccessControlRecordInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create Nimble / Alletra 6K access control record in system identified by {systemId}
        api_response = api_instance.device_type2_access_control_record_create(system_id, nimble_create_access_control_record_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_clone_volume_by_id**
> TaskResponse device_type2_clone_volume_by_id(system_id, volume_id, nimble_clone_volume_input)

Create Nimble / Alletra 6K clone volume identified by {volumeId}.

Create Nimble / Alletra 6K clone volume identified by {volumeId}.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from greenlake_data_services.model.nimble_clone_volume_input import NimbleCloneVolumeInput
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    nimble_clone_volume_input = NimbleCloneVolumeInput(
        clone_volume_name="clone_volume",
        host_group_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        lun=100,
    ) # NimbleCloneVolumeInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create Nimble / Alletra 6K clone volume identified by {volumeId}.
        api_response = api_instance.device_type2_clone_volume_by_id(system_id, volume_id, nimble_clone_volume_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_delete_snapshot_access_by_id**
> TaskResponse device_type2_delete_snapshot_access_by_id(system_id, volume_id, snapshot_id, un_export_input)

Delete access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}

Delete access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.un_export_input import UnExportInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    snapshot_id = "2a0df0fe6f7dc7bb17000000000000000000000008" # str | Identifier of snapshot. A 42 digit hexadecimal number.
    un_export_input = UnExportInput(
        host_groups=[
            "host_groups_example",
        ],
    ) # UnExportInput | 

    # example passing only required values which don't have defaults set
    try:
        # Delete access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}
        api_response = api_instance.device_type2_delete_snapshot_access_by_id(system_id, volume_id, snapshot_id, un_export_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_delete_volume_access_by_id**
> TaskResponse device_type2_delete_volume_access_by_id(system_id, volume_id, un_export_input)

Delete access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}

Delete access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.un_export_input import UnExportInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    un_export_input = UnExportInput(
        host_groups=[
            "host_groups_example",
        ],
    ) # UnExportInput | 

    # example passing only required values which don't have defaults set
    try:
        # Delete access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}
        api_response = api_instance.device_type2_delete_volume_access_by_id(system_id, volume_id, un_export_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_snapshot_by_id**
> TaskResponse device_type2_edit_snapshot_by_id(system_id, nimble_edit_multiple_snapshot_input)

Edit Multiple Nimble / Alletra 6K snapshots in system identified by {systemId}

Edit Multiple Nimble / Alletra 6K snapshots in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from greenlake_data_services.model.nimble_edit_multiple_snapshot_input import NimbleEditMultipleSnapshotInput
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_edit_multiple_snapshot_input = NimbleEditMultipleSnapshotInput(
        snapshot_list=[
            NimbleEditSnapshotInput(
                app_uuid="rfc4122.943f7dc1-5853-497c-b530-f689ccf1bf18",
                description="99.9999% availability",
                id="2a0df0fe6f7dc7bb16000000000000000000004817",
                metadata=[
                    KeyValue(
                        key="key1",
                        value="value1",
                    ),
                ],
                online=False,
            ),
        ],
    ) # NimbleEditMultipleSnapshotInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit Multiple Nimble / Alletra 6K snapshots in system identified by {systemId}
        api_response = api_instance.device_type2_edit_snapshot_by_id(system_id, nimble_edit_multiple_snapshot_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_volume_by_id**
> TaskResponse device_type2_edit_volume_by_id(system_id, volume_id, nimble_edit_volume_input)

Edit  details of Nimble / Alletra 6K Volume identified by {volumeId}

Edit  details of Nimble / Alletra 6K Volume identified by {volumeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_edit_volume_input import NimbleEditVolumeInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    nimble_edit_volume_input = NimbleEditVolumeInput(
        app_uuid="rfc4122.943f7dc1-5853-497c-b530-f689ccf1bf18",
        caching_enabled=True,
        dedupe_enabled=True,
        description="99.9999% availability",
        folder_id="1234123412341234123412341234123412341234cd",
        force=True,
        limit=1,
        limit_iops=-1,
        limit_mbps=-1,
        name="volume1",
        online=True,
        owned_by_group_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        perfpolicy_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        size=1024,
    ) # NimbleEditVolumeInput | 

    # example passing only required values which don't have defaults set
    try:
        # Edit  details of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_edit_volume_by_id(system_id, volume_id, nimble_edit_volume_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_access_control_record_by_id**
> NimbleAccessControlRecordDetailsWithRequestUri device_type2_get_access_control_record_by_id(system_id, access_control_record_id)

Get details of Nimble / Alletra 6K access-control-records identified by {accessControlRecordId}

Get details of Nimble / Alletra 6K access-control-records identified by {accessControlRecordId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.nimble_access_control_record_details_with_request_uri import NimbleAccessControlRecordDetailsWithRequestUri
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    access_control_record_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the Access Control Record . A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K access-control-records identified by {accessControlRecordId}
        api_response = api_instance.device_type2_get_access_control_record_by_id(system_id, access_control_record_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type2_get_access_control_record_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K access-control-records identified by {accessControlRecordId}
        api_response = api_instance.device_type2_get_access_control_record_by_id(system_id, access_control_record_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_access_control_records**
> NimbleAccessControlRecordList device_type2_get_all_access_control_records(system_id)

Get all access-control-records details by Nimble / Alletra 6K

Get all access-control-records details by Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_access_control_record_list import NimbleAccessControlRecordList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter Access Control Record  by Key. (optional)
    sort = "name desc" # str | oData query to sort Access Control Record  resource by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all access-control-records details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_access_control_records(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type2_get_all_access_control_records: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all access-control-records details by Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_access_control_records(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_snapshots_by_volume_id**
> NimbleSnapshotList device_type2_get_all_snapshots_by_volume_id(system_id, volume_id)

Get all snapshots' details of Nimble / Alletra 6K Volume identified by {volumeId}

Get all snapshots' details of Nimble / Alletra 6K Volume identified by {volumeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_snapshot_list import NimbleSnapshotList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter snapshots by Key. (optional)
    sort = "name desc" # str | oData query to sort snapshots resource by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all snapshots' details of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_get_all_snapshots_by_volume_id(system_id, volume_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type2_get_all_snapshots_by_volume_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all snapshots' details of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_get_all_snapshots_by_volume_id(system_id, volume_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_volumes**
> NimbleVolumesList device_type2_get_all_volumes(system_id)

Get all volumes details for Nimble / Alletra 6K

Get all volumes details for Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_volumes_list import NimbleVolumesList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "id eq 2a0df0fe6f7dc7bb16000000000000000000004817" # str | Lucene query to filter volumes by Key. (optional)
    sort = "name desc" # str | oData query to sort volumes resource by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all volumes details for Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_volumes(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type2_get_all_volumes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all volumes details for Nimble / Alletra 6K
        api_response = api_instance.device_type2_get_all_volumes(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_snapshot_by_id**
> NimbleSnapshotDetails device_type2_get_snapshot_by_id(system_id, volume_id, snapshot_id)

Get details of snapshot of Nimble / Alletra 6K Volume identified by {volumeId} by {snapshotId}

Get details of snapshot of Nimble / Alletra 6K Volume identified by {volumeId} by {snapshotId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.nimble_snapshot_details import NimbleSnapshotDetails
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    snapshot_id = "2a0df0fe6f7dc7bb17000000000000000000000008" # str | Identifier of snapshot. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of snapshot of Nimble / Alletra 6K Volume identified by {volumeId} by {snapshotId}
        api_response = api_instance.device_type2_get_snapshot_by_id(system_id, volume_id, snapshot_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type2_get_snapshot_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of snapshot of Nimble / Alletra 6K Volume identified by {volumeId} by {snapshotId}
        api_response = api_instance.device_type2_get_snapshot_by_id(system_id, volume_id, snapshot_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_volume_by_id**
> NimbleVolumeDetails device_type2_get_volume_by_id(system_id, volume_id)

Get details of Nimble / Alletra 6K Volume identified by {volumeId}

Get details of Nimble / Alletra 6K Volume identified by {volumeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_volume_details import NimbleVolumeDetails
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_get_volume_by_id(system_id, volume_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type2_get_volume_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_get_volume_by_id(system_id, volume_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_volume_capacity_history**
> NimblevolumeCapacityHistory device_type2_get_volume_capacity_history(system_id, volume_id)

Get volume capacity trend data of Nimble / Alletra 6K Volume identified by {volumeId}

Get volume capacity trend data of Nimble / Alletra 6K Volume identified by {volumeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimblevolume_capacity_history import NimblevolumeCapacityHistory
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    range = "startTime eq 1605063600 and endTime eq 1605186000" # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get volume capacity trend data of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_get_volume_capacity_history(system_id, volume_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type2_get_volume_capacity_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get volume capacity trend data of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_get_volume_capacity_history(system_id, volume_id, select=select, range=range, time_interval_min=time_interval_min)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_volume_performance_history**
> NimblevolumePerformanceHistory device_type2_get_volume_performance_history(system_id, volume_id)

Get performance trend data of Nimble / Alletra 6K Volume identified by {id}

Get performance trend data of Nimble / Alletra 6K Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimblevolume_performance_history import NimblevolumePerformanceHistory
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)
    range = "startTime eq 1605063600 and endTime eq 1605186000" # str | range will define start and end time in which query has to be made. (optional)
    time_interval_min = 60 # int | It defines granularity in minutes. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get performance trend data of Nimble / Alletra 6K Volume identified by {id}
        api_response = api_instance.device_type2_get_volume_performance_history(system_id, volume_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type2_get_volume_performance_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get performance trend data of Nimble / Alletra 6K Volume identified by {id}
        api_response = api_instance.device_type2_get_volume_performance_history(system_id, volume_id, select=select, range=range, time_interval_min=time_interval_min)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_volume_performance_statistics**
> VolPerformance device_type2_get_volume_performance_statistics(system_id, volume_id)

Get performance statistics of Nimble / Alletra 6K Volume identified by {volumeId}

Get performance statistics of Nimble / Alletra 6K Volume identified by {volumeId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.vol_performance import VolPerformance
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get performance statistics of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_get_volume_performance_statistics(system_id, volume_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type2_get_volume_performance_statistics: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get performance statistics of Nimble / Alletra 6K Volume identified by {volumeId}
        api_response = api_instance.device_type2_get_volume_performance_statistics(system_id, volume_id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_move_volume**
> TaskResponse device_type2_move_volume(system_id, volume_id, nimble_move_volume_to_another_pool_input)

Move Nimble / Alletra 6K volume identified by {volumeId} to another pool.

Move Nimble / Alletra 6K volume identified by {volumeId} to another pool.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_move_volume_to_another_pool_input import NimbleMoveVolumeToAnotherPoolInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    nimble_move_volume_to_another_pool_input = NimbleMoveVolumeToAnotherPoolInput(
        dest_pool_id="0a00000000000004d3000000000000000000000001",
    ) # NimbleMoveVolumeToAnotherPoolInput | 

    # example passing only required values which don't have defaults set
    try:
        # Move Nimble / Alletra 6K volume identified by {volumeId} to another pool.
        api_response = api_instance.device_type2_move_volume(system_id, volume_id, nimble_move_volume_to_another_pool_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_provisioning_review**
> NimbleHostReviewOutput device_type2_provisioning_review(system_id, nimble_host_review_input)

Provisioning review for a storage system Nimble / Alletra 6K

Provisioning review for a storage system Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.nimble_host_review_input import NimbleHostReviewInput
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.nimble_host_review_output import NimbleHostReviewOutput
from greenlake_data_services.model.error import Error
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_host_review_input = NimbleHostReviewInput(
        host_groups=[
            "host_groups_example",
        ],
    ) # NimbleHostReviewInput | 

    # example passing only required values which don't have defaults set
    try:
        # Provisioning review for a storage system Nimble / Alletra 6K
        api_response = api_instance.device_type2_provisioning_review(system_id, nimble_host_review_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_provisioning_worklow**
> TaskResponse device_type2_provisioning_worklow(system_id, nimble_create_volumes_workflow_input)

Create provisioning workflow for a Nimble / Alletra 6K storage system identified by {systemId}

Create provisioning workflow for a Nimble / Alletra 6K storage system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.nimble_create_volumes_workflow_input import NimbleCreateVolumesWorkflowInput
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_create_volumes_workflow_input = NimbleCreateVolumesWorkflowInput(
        agent_type="none",
        app_uuid="rfc4122.943f7dc1-5853-497c-b530-f689ccf1bf18",
        count=3,
        dedupe_enabled=False,
        downstream_partner="<resource_name>",
        downstream_partner_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        folder_id="1234123412341234123412341234123412341234cd",
        host_groups=[
            NimbleHostGroupDetails(
                host_group_id="2a0df0fe6f7dc7bb16000000000000000000004817",
                lun=100,
            ),
        ],
        limit=100,
        limit_iops=-1,
        limit_mbps=-1,
        name="volume1",
        perfpolicy=CustomApp(
            compression=True,
            deduplication=True,
            name="CUSTOM-LOG-SERVER",
        ),
        perfpolicy_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        pool_id="0a00000000000004d3000000000000000000000001",
        protection_policy_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        protection_policy_schedules=[
            NimbleCreateVolumesWorkflowInputProtectionPolicySchedulesInner(
                name="<name>",
                start_time="8:30",
            ),
        ],
        replication_start_time=16384456,
        size=16,
        vol_col_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        vol_col_name="appset_1",
        warn_level=80,
    ) # NimbleCreateVolumesWorkflowInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create provisioning workflow for a Nimble / Alletra 6K storage system identified by {systemId}
        api_response = api_instance.device_type2_provisioning_worklow(system_id, nimble_create_volumes_workflow_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_access_control_record_by_id**
> TaskResponse device_type2_remove_access_control_record_by_id(system_id, access_control_record_id)

Remove access-control-record identified by {accessControlRecordId} from Nimble / Alletra 6K

Remove access-control-record identified by {accessControlRecordId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    access_control_record_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of Access Control Record. A 42 digit hexadecimal number.

    # example passing only required values which don't have defaults set
    try:
        # Remove access-control-record identified by {accessControlRecordId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_access_control_record_by_id(system_id, access_control_record_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_snapshot_by_id**
> TaskResponse device_type2_remove_snapshot_by_id(system_id, volume_id, snapshot_id)

Remove Nimble / Alletra 6K snapshot in system identified by {snapshotId}

Remove Nimble / Alletra 6K snapshot in system identified by {snapshotId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    snapshot_id = "2a0df0fe6f7dc7bb17000000000000000000000008" # str | Identifier of snapshot. A 42 digit hexadecimal number.
    force = True # bool | Make snapshot offline and remove. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove Nimble / Alletra 6K snapshot in system identified by {snapshotId}
        api_response = api_instance.device_type2_remove_snapshot_by_id(system_id, volume_id, snapshot_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type2_remove_snapshot_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Nimble / Alletra 6K snapshot in system identified by {snapshotId}
        api_response = api_instance.device_type2_remove_snapshot_by_id(system_id, volume_id, snapshot_id, force=force)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_volume_by_id**
> TaskResponse device_type2_remove_volume_by_id(system_id, volume_id)

Remove volume identified by {volumeId} from Nimble / Alletra 6K

Remove volume identified by {volumeId} from Nimble / Alletra 6K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    offline = True # bool | Make volume offline and delete. Deprecated - Use force instead of offline. (optional)
    force = True # bool | Make volume and associated snapshots offline, stop protection and delete. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove volume identified by {volumeId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_volume_by_id(system_id, volume_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->device_type2_remove_volume_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove volume identified by {volumeId} from Nimble / Alletra 6K
        api_response = api_instance.device_type2_remove_volume_by_id(system_id, volume_id, offline=offline, force=force)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_restore_volume_by_id**
> TaskResponse device_type2_restore_volume_by_id(system_id, volume_id, nimble_restore_volume_input)

Restore Nimble / Alletra 6K volume identified by {volumeId} from a previous snapshot.

Restore Nimble / Alletra 6K volume identified by {volumeId} from a previous snapshot.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_restore_volume_input import NimbleRestoreVolumeInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    nimble_restore_volume_input = NimbleRestoreVolumeInput(
        base_snap_id="0a00000000000004d3000000000000000000000481",
        enable_vol_offline=True,
    ) # NimbleRestoreVolumeInput | 

    # example passing only required values which don't have defaults set
    try:
        # Restore Nimble / Alletra 6K volume identified by {volumeId} from a previous snapshot.
        api_response = api_instance.device_type2_restore_volume_by_id(system_id, volume_id, nimble_restore_volume_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_snapshot_create**
> TaskResponse device_type2_snapshot_create(system_id, volume_id, nimble_create_snapshot_input)

Create Nimble / Alletra 6K snapshot in system identified by {systemId}

Create Nimble / Alletra 6K snapshot in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_create_snapshot_input import NimbleCreateSnapshotInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    nimble_create_snapshot_input = NimbleCreateSnapshotInput(
        app_uuid="rfc4122.943f7dc1-5853-497c-b530-f689ccf1bf18",
        description="99.9999% availability",
        metadata=[
            KeyValue(
                key="key1",
                value="value1",
            ),
        ],
        name="snap1",
        online=False,
        writable=False,
    ) # NimbleCreateSnapshotInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create Nimble / Alletra 6K snapshot in system identified by {systemId}
        api_response = api_instance.device_type2_snapshot_create(system_id, volume_id, nimble_create_snapshot_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_snapshot_export**
> TaskResponse device_type2_snapshot_export(system_id, volume_id, snapshot_id, export_input)

Configure access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}

Configure access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.export_input import ExportInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    snapshot_id = "2a0df0fe6f7dc7bb17000000000000000000000008" # str | Identifier of snapshot. A 42 digit hexadecimal number.
    export_input = ExportInput(
        host_groups=[
            "host_groups_example",
        ],
    ) # ExportInput | 

    # example passing only required values which don't have defaults set
    try:
        # Configure access for snapshot identified by {snapshotId} from Nimble / Alletra 6K identified by {systemId}
        api_response = api_instance.device_type2_snapshot_export(system_id, volume_id, snapshot_id, export_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_volumes_create**
> TaskResponse device_type2_volumes_create(system_id, nimble_create_volume_input)

Create Nimble / Alletra 6K volume in system identified by {systemId}

Create Nimble / Alletra 6K volume in system identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.nimble_create_volume_input import NimbleCreateVolumeInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    nimble_create_volume_input = NimbleCreateVolumeInput(
        agent_type="none",
        app_uuid="rfc4122.943f7dc1-5853-497c-b530-f689ccf1bf18",
        base_snap_id="2a0df0fe6f7dc7bb16000000000000000000004017",
        block_size=4096,
        cache_pinned=False,
        clone=False,
        dedupe_enabled=False,
        description="99.9999% availability",
        dest_pool_id="0a00000000000004d3000000000000000000000001",
        encryption_cipher="none",
        folder_id="1234123412341234123412341234123412341234cd",
        limit=100,
        limit_iops=-1,
        limit_mbps=-1,
        metadata=[
            KeyValue(
                key="key1",
                value="value1",
            ),
        ],
        multi_initiator=False,
        name="volume1",
        online=True,
        owned_by_group_id="2a0df0fe6f7dc7bb16000000000000000000004007",
        perfpolicy_id="2a0df0fe6f7dc7bb16000000000000000000004817",
        pool_id="0a00000000000004d3000000000000000000000001",
        read_only=False,
        reserve=0,
        size=1024,
        snap_reserve=0,
        snap_warn_level=0,
        suffix=4,
        warn_level=80,
    ) # NimbleCreateVolumeInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create Nimble / Alletra 6K volume in system identified by {systemId}
        api_response = api_instance.device_type2_volumes_create(system_id, nimble_create_volume_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_volumes_export**
> TaskResponse device_type2_volumes_export(system_id, volume_id, export_input)

Configure access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}

Configure access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.export_input import ExportInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "2a0df0fe6f7dc7bb16000000000000000000004817" # str | ID of the storage system
    volume_id = "2a0df0fe6f7dc7bb16000000000000000000000007" # str | Identifier of volume. A 42 digit hexadecimal number.
    export_input = ExportInput(
        host_groups=[
            "host_groups_example",
        ],
    ) # ExportInput | 

    # example passing only required values which don't have defaults set
    try:
        # Configure access for volume identified by {volumeId} from Nimble / Alletra 6K identified by {systemId}
        api_response = api_instance.device_type2_volumes_export(system_id, volume_id, export_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_clone_create**
> TaskResponse snapshot_clone_create(system_id, snapshot_id, create_clone_snapshot_input)

Create a clone of a snapshot identified by {snapshotId} for Primera / Alletra 9K systems.

Create a clone of a snapshot identified by {snapshotId} for Primera / Alletra 9K systems.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.create_clone_snapshot_input import CreateCloneSnapshotInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    snapshot_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID of the snapshots
    create_clone_snapshot_input = CreateCloneSnapshotInput(
        auto_lun=True,
        destination_cpg="SSD_r6",
        destination_volume="destinationVol1",
        host_group_id="fd3244ef7f1ab8bd16500c7a41bdf8f8",
        lun=0,
        priority="PRIORITYTYPE_MED",
    ) # CreateCloneSnapshotInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create a clone of a snapshot identified by {snapshotId} for Primera / Alletra 9K systems.
        api_response = api_instance.snapshot_clone_create(system_id, snapshot_id, create_clone_snapshot_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vluns_delete**
> TaskResponse vluns_delete(system_id, volume_id, id)

Remove vlun idenfied by {id} form volume identified by {volumeId} from Primera / Alletra 9K

Remove vlun idenfied by {id} form volume identified by {volumeId} from Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    volume_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID of the vlun

    # example passing only required values which don't have defaults set
    try:
        # Remove vlun idenfied by {id} form volume identified by {volumeId} from Primera / Alletra 9K
        api_response = api_instance.vluns_delete(system_id, volume_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_clone_create**
> TaskResponse volume_clone_create(system_id, id, create_clone_volume_input)

Create a clone volume identified by {id} for Primera / Alletra 9K systems.

Create a clone volume identified by {id} for Primera / Alletra 9K systems.

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.create_clone_volume_input import CreateCloneVolumeInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    create_clone_volume_input = CreateCloneVolumeInput(
        destination_volume="destinationVol1",
        offline_clone=[
            OfflineClone(
                create_volume=[
                    CreateVolume(
                        destination_cpg="SSD_r6",
                    ),
                ],
                enable_resync=True,
                use_existing_volume=True,
            ),
        ],
        online=True,
        online_clone=[
            OnlineClone(
                auto_lun=True,
                destination_cpg="SSD_r6",
                host_group_id="fd3244ef7f1ab8bd16500c7a41bdf8f8",
                lun=0,
            ),
        ],
        priority="PRIORITYTYPE_MED",
    ) # CreateCloneVolumeInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create a clone volume identified by {id} for Primera / Alletra 9K systems.
        api_response = api_instance.volume_clone_create(system_id, id, create_clone_volume_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_create**
> TaskResponse volume_create(system_id, create_volume_input)

Create volume for a storage system Primera / Alletra 9K

Create volume for a storage system Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.create_volume_input import CreateVolumeInput
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    create_volume_input = CreateVolumeInput(
        comments="test",
        count=2,
        data_reduction=True,
        name="<resource_name>",
        size_mib=16384,
        snap_cpg="SSD_r6",
        snapshot_alloc_warning=5,
        user_alloc_warning=5,
        user_cpg="SSD_r6",
    ) # CreateVolumeInput | 

    # example passing only required values which don't have defaults set
    try:
        # Create volume for a storage system Primera / Alletra 9K
        api_response = api_instance.volume_create(system_id, create_volume_input)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_delete**
> TaskResponse volume_delete(system_id, id)

Remove volume identified by {volumeId} from Primera / Alletra 9K

Remove volume identified by {volumeId} from Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    un_export = True # bool | UnExport Host,HostSet and delete volume (optional)
    cascade = True # bool | Delete snapshot and volume (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove volume identified by {volumeId} from Primera / Alletra 9K
        api_response = api_instance.volume_delete(system_id, id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->volume_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove volume identified by {volumeId} from Primera / Alletra 9K
        api_response = api_instance.volume_delete(system_id, id, un_export=un_export, cascade=cascade)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_edit**
> TaskResponse volume_edit(system_id, id, volume_put)

Edit volume identified by {volumeId} from Primera / Alletra 9K

Edit volume identified by {volumeId} from Primera / Alletra 9K

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from greenlake_data_services.model.volume_put import VolumePut
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    volume_put = VolumePut(
        conversion_type="CONVERSIONTYPE_THIN",
        data_reduction=True,
        name="volume_Name",
        size_mib=1,
        snapshot_alloc_warning=1,
        user_alloc_warning=1,
        user_cpg_name="cpg_1",
    ) # VolumePut | 

    # example passing only required values which don't have defaults set
    try:
        # Edit volume identified by {volumeId} from Primera / Alletra 9K
        api_response = api_instance.volume_edit(system_id, id, volume_put)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_get_by_id**
> FleetVolumeDetails volume_get_by_id(id)

Get details of Volume identified by {id}

Get details of Volume identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.fleet_volume_details import FleetVolumeDetails
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of Volume identified by {id}
        api_response = api_instance.volume_get_by_id(id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->volume_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of Volume identified by {id}
        api_response = api_instance.volume_get_by_id(id, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_list_for_system_by_system_id**
> FleetVolumesList volume_list_for_system_by_system_id(system_id)

Get details of volumes identified with {systemId}

Get details of volumes identified with {systemId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.fleet_volumes_list import FleetVolumesList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "name eq array1 and wwn eq 2FF70002AC018D94" # str | oData query to filter by Key. (optional)
    sort = "systemWWN desc" # str | oData query to sort by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get details of volumes identified with {systemId}
        api_response = api_instance.volume_list_for_system_by_system_id(system_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->volume_list_for_system_by_system_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get details of volumes identified with {systemId}
        api_response = api_instance.volume_list_for_system_by_system_id(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_snapshot_create**
> TaskResponse volume_snapshot_create(system_id, id, volume_post)

Create snapshot for volumes identified by {id}

Create snapshot for volumes identified by {id}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.volume_post import VolumePost
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    volume_post = VolumePost(
        comment="",
        custom_name="snap1",
        expire_secs=86400,
        name_pattern=NamePattern("PARENT_TIMESTAMP"),
        read_only=False,
        retain_secs=86400,
    ) # VolumePost | 

    # example passing only required values which don't have defaults set
    try:
        # Create snapshot for volumes identified by {id}
        api_response = api_instance.volume_snapshot_create(system_id, id, volume_post)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_snapshot_get_by_id**
> TaskResponse volume_snapshot_get_by_id(system_id, volume_id, snapshot_id)

Remove Primera / Alletra 9K snapshot in system identified by {snapshotId}

Remove Primera / Alletra 9K snapshot in system identified by {snapshotId}

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.task_response import TaskResponse
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    system_id = "7CE751P312" # str | systemId of the device-type1 storage system
    volume_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | UID(volumeuid) of the storage system
    snapshot_id = "a7c4e6593f51d0b98f0e40d7e6df04fd" # str | Identifier of snapshot.
    force = True # bool | Make snapshot offline and remove. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Remove Primera / Alletra 9K snapshot in system identified by {snapshotId}
        api_response = api_instance.volume_snapshot_get_by_id(system_id, volume_id, snapshot_id)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
        print("Exception when calling VolumesApi->volume_snapshot_get_by_id: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Remove Primera / Alletra 9K snapshot in system identified by {snapshotId}
        api_response = api_instance.volume_snapshot_get_by_id(system_id, volume_id, snapshot_id, force=force)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumes_list**
> FleetVolumesList volumes_list()

Get all volumes

Get all volumes

### Example

* Bearer (JWT) Authentication (JWTAuth):

```python
import time
import greenlake_data_services
from greenlake_data_services.api import volumes_api
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.error import Error
from greenlake_data_services.model.fleet_volumes_list import FleetVolumesList
from pprint import pprint
# Defining the host is optional and defaults to https://eu1.data.cloud.hpe.com
# See configuration.py for a list of all supported configuration parameters.
configuration = greenlake_data_services.Configuration(
    host = "https://eu1.data.cloud.hpe.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWTAuth
configuration = greenlake_data_services.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with greenlake_data_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = volumes_api.VolumesApi(api_client)
    limit = 10 # int | Number of items to return at a time (optional)
    offset = 5 # int | The offset of the first item in the collection to return (optional)
    filter = "name eq array1 and wwn eq 2FF70002AC018D94" # str | oData query to filter by Key. (optional)
    sort = "systemWWN desc" # str | oData query to sort by Key. (optional)
    select = "id" # str | Query to select only the required parameters, separated by . if nested (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all volumes
        api_response = api_instance.volumes_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
        pprint(api_response)
    except greenlake_data_services.ApiException as e:
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


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**304** | Not Modified |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Storage system object not found |  -  |
**500** | Internal / unexpected error |  -  |
**503** | Appliance in maintenance mode |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

