# greenlake-data-services.VolumeSetsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type1_edit_proximity_settings**](VolumeSetsApi.md#device_type1_edit_proximity_settings) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/proximity-settings | Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from Primera / Alletra 9K
[**device_type1_get_proximity_settings**](VolumeSetsApi.md#device_type1_get_proximity_settings) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/proximity-settings | Get hosts and proximity details identified by application set {id} for Primera / Alletra 9K identified by {systemId}
[**device_type1_get_replication_partner_volumes_by_app_set_id**](VolumeSetsApi.md#device_type1_get_replication_partner_volumes_by_app_set_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/replication-partners/{replicationPartnerId}/volumes | Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for Primera / Alletra 9K
[**device_type1_get_replication_partners_by_app_set_id**](VolumeSetsApi.md#device_type1_get_replication_partners_by_app_set_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/replication-partners | Get details of Primera / Alletra 9K replication partners identified by {systemId} and {appsetId}
[**device_type1_snapsets_get_by_id**](VolumeSetsApi.md#device_type1_snapsets_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/snapsets/{snapsetId} | Get details of snapsets identified by {snapsetId} for Applicationset identified by {appsetId} for Primera / Alletra 9K
[**device_type1_volume_set_capacity_statistics_get_by_id**](VolumeSetsApi.md#device_type1_volume_set_capacity_statistics_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/capacity-statistics | Get capacity details for an applicationset identified by appsetUid
[**device_type1_volume_set_export**](VolumeSetsApi.md#device_type1_volume_set_export) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/export | Export applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}
[**device_type1_volume_set_snapshot_get_by_id**](VolumeSetsApi.md#device_type1_volume_set_snapshot_get_by_id) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/snapsets/{snapsetId} | Remove Primera / Alletra 9K snapset in system identified by {snapsetId}
[**device_type1_volume_set_snapshots_list**](VolumeSetsApi.md#device_type1_volume_set_snapshots_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/snapsets | Get snapshot details of volume sets identified by {id} for Primera / Alletra 9K
[**device_type1_volume_set_unexport**](VolumeSetsApi.md#device_type1_volume_set_unexport) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/un-export | Unexport applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}
[**device_type1_volume_set_volumes_list**](VolumeSetsApi.md#device_type1_volume_set_volumes_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{appsetId}/volumes | Get volumes for an applicationset identified by appsetUid
[**device_type1_volume_sets_create**](VolumeSetsApi.md#device_type1_volume_sets_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets | Create Application Set for a storage system Primera / Alletra 9K
[**device_type1_volume_sets_delete_by_id**](VolumeSetsApi.md#device_type1_volume_sets_delete_by_id) | **DELETE** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id} | Remove applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_volume_sets_edit_by_id**](VolumeSetsApi.md#device_type1_volume_sets_edit_by_id) | **PUT** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id} | Edit applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}
[**device_type1_volume_sets_get_by_id**](VolumeSetsApi.md#device_type1_volume_sets_get_by_id) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id} | Get applicationset details for an applicationset identified by appsetUid
[**device_type1_volume_sets_list**](VolumeSetsApi.md#device_type1_volume_sets_list) | **GET** /api/v1/storage-systems/device-type1/{systemId}/applicationsets | Get all applicationset details for Primera / Alletra 9K
[**device_type1_volume_sets_snapshot_create**](VolumeSetsApi.md#device_type1_volume_sets_snapshot_create) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/snapsets | Create snapshot for application set identified by {id}
[**device_type1action_on_volume_sets**](VolumeSetsApi.md#device_type1action_on_volume_sets) | **POST** /api/v1/storage-systems/device-type1/{systemId}/applicationsets/{id}/remote-protection/actions | Actions on volume set identified by {id} and {systemId} from Primera / Alletra 9K
[**device_type2_action_on_snapshot_collection**](VolumeSetsApi.md#device_type2_action_on_snapshot_collection) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/snapshot-collections/update | Perform offline/online action on  snapshot collections of Nimble / Alletra 6K and associated with volume collection {volumeCollectionId}  in the system identified by {systemId}
[**device_type2_action_on_volume_collection**](VolumeSetsApi.md#device_type2_action_on_volume_collection) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/actions/handover | Perform handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
[**device_type2_action_on_volume_collection_id**](VolumeSetsApi.md#device_type2_action_on_volume_collection_id) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/actions/demote | Perform demote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
[**device_type2_actionon_volume_collection**](VolumeSetsApi.md#device_type2_actionon_volume_collection) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/actions/abort-handover | Perform abort handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
[**device_type2_add_volumes_to_volume_collections**](VolumeSetsApi.md#device_type2_add_volumes_to_volume_collections) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/actions/add-volumes | Add volumes to Nimble / Alletra 6K volumes collection in system identified by {systemId}
[**device_type2_create_snapshot_collections**](VolumeSetsApi.md#device_type2_create_snapshot_collections) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/snapshot-collections | Create Nimble / Alletra 6K snapshot collection in system identified by {systemId}
[**device_type2_edit_volume_collection_by_id**](VolumeSetsApi.md#device_type2_edit_volume_collection_by_id) | **PUT** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId} | Edit  details of Nimble / Alletra 6K Volume-collections identified by {volumeCollectionId}
[**device_type2_get_all_folders**](VolumeSetsApi.md#device_type2_get_all_folders) | **GET** /api/v1/storage-systems/device-type2/{systemId}/folders | Get all folders details by Nimble / Alletra 6K
[**device_type2_get_all_volume_collections**](VolumeSetsApi.md#device_type2_get_all_volume_collections) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volume-collections | Get all volume-collections details by Nimble / Alletra 6K
[**device_type2_get_snapshot_collections_by_id**](VolumeSetsApi.md#device_type2_get_snapshot_collections_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/snapshot-collections/{snapshotCollectionId} | Get details of snapshot collection of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId} by {snapshotId}
[**device_type2_get_snapshots_by_volume_collection_id**](VolumeSetsApi.md#device_type2_get_snapshots_by_volume_collection_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/snapshot-collections | Get all snapshot collections&#39; details of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId}
[**device_type2_get_volume_collection_by_id**](VolumeSetsApi.md#device_type2_get_volume_collection_by_id) | **GET** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId} | Get details of Nimble / Alletra 6K volume-collections identified by {volumeCollectionId}
[**device_type2_promote_action_on_volume_collection**](VolumeSetsApi.md#device_type2_promote_action_on_volume_collection) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/actions/promote | Perform promote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
[**device_type2_remove_snap_shot_collection**](VolumeSetsApi.md#device_type2_remove_snap_shot_collection) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/snapshot-collections/remove | Remove multiple snapshot collections identified by {volumeCollectionId} from Nimble / Alletra 6K
[**device_type2_remove_volume_collection_by_id**](VolumeSetsApi.md#device_type2_remove_volume_collection_by_id) | **DELETE** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId} | Remove Volume-collection identified by {volumeCollectionId} from Nimble / Alletra 6K
[**device_type2_remove_volumes_from_volume_collection**](VolumeSetsApi.md#device_type2_remove_volumes_from_volume_collection) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections/{volumeCollectionId}/actions/remove-volumes | Remove volumes from Nimble / Alletra 6K volumes collection in system identified by {systemId}
[**device_type2_volume_collection_create**](VolumeSetsApi.md#device_type2_volume_collection_create) | **POST** /api/v1/storage-systems/device-type2/{systemId}/volume-collections | Create Nimble / Alletra 6K volume collection in system identified by {systemId}
[**volumeset_get_by_id**](VolumeSetsApi.md#volumeset_get_by_id) | **GET** /api/v1/volume-sets/{id} | Get volume-set identified by id
[**volumeset_get_byvolumeset_id**](VolumeSetsApi.md#volumeset_get_byvolumeset_id) | **GET** /api/v1/volume-sets/{id}/volumes | Get volumes identified by volume set id
[**volumeset_list**](VolumeSetsApi.md#volumeset_list) | **GET** /api/v1/volume-sets | Get all volume-sets
[**volumeset_list_for_system_by_system_id**](VolumeSetsApi.md#volumeset_list_for_system_by_system_id) | **GET** /api/v1/storage-systems/{systemId}/volume-sets | Get all volume-sets for a systemId
[**volumeset_system_get_by_id**](VolumeSetsApi.md#volumeset_system_get_by_id) | **GET** /api/v1/storage-systems/{systemId}/volume-sets/{id} | Get volume-set identified by id


# **device_type1_edit_proximity_settings**
> TaskResponse device_type1_edit_proximity_settings(system_id, id, change_proximity_settings_input)

Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from Primera / Alletra 9K

Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from Primera / Alletra 9K

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the applicationset
change_proximity_settings_input = greenlake-data-services.ChangeProximitySettingsInput() # ChangeProximitySettingsInput | 

try:
    # Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from Primera / Alletra 9K
    api_response = api_instance.device_type1_edit_proximity_settings(system_id, id, change_proximity_settings_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_edit_proximity_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the applicationset | 
 **change_proximity_settings_input** | [**ChangeProximitySettingsInput**](ChangeProximitySettingsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_proximity_settings**
> VolumeSetProximitySettings device_type1_get_proximity_settings(id, system_id)

Get hosts and proximity details identified by application set {id} for Primera / Alletra 9K identified by {systemId}

Get hosts and proximity details identified by application set {id} for Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
id = 'id_example' # str | ID of the applicationset
system_id = 'system_id_example' # str | systemId of the device-type1 storage system

try:
    # Get hosts and proximity details identified by application set {id} for Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_get_proximity_settings(id, system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_get_proximity_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the applicationset | 
 **system_id** | **str**| systemId of the device-type1 storage system | 

### Return type

[**VolumeSetProximitySettings**](VolumeSetProximitySettings.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_replication_partner_volumes_by_app_set_id**
> ReplicationPartnerVolumesSummaryList device_type1_get_replication_partner_volumes_by_app_set_id(system_id, appset_id, replication_partner_id, limit=limit, offset=offset)

Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for Primera / Alletra 9K

Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for Primera / Alletra 9K

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
appset_id = 'appset_id_example' # str | UID of the applicationset
replication_partner_id = 'replication_partner_id_example' # str | id of device-type1 replication partner
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)

try:
    # Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for Primera / Alletra 9K
    api_response = api_instance.device_type1_get_replication_partner_volumes_by_app_set_id(system_id, appset_id, replication_partner_id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_get_replication_partner_volumes_by_app_set_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **replication_partner_id** | **str**| id of device-type1 replication partner | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 

### Return type

[**ReplicationPartnerVolumesSummaryList**](ReplicationPartnerVolumesSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_get_replication_partners_by_app_set_id**
> ReplicationPartnersSummaryList device_type1_get_replication_partners_by_app_set_id(system_id, appset_id)

Get details of Primera / Alletra 9K replication partners identified by {systemId} and {appsetId}

Get details of Primera / Alletra 9K replication partners identified by {systemId} and {appsetId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
appset_id = 'appset_id_example' # str | UID of the applicationset

try:
    # Get details of Primera / Alletra 9K replication partners identified by {systemId} and {appsetId}
    api_response = api_instance.device_type1_get_replication_partners_by_app_set_id(system_id, appset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_get_replication_partners_by_app_set_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **appset_id** | **str**| UID of the applicationset | 

### Return type

[**ReplicationPartnersSummaryList**](ReplicationPartnersSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_snapsets_get_by_id**
> SnapshotsetListSingle device_type1_snapsets_get_by_id(system_id, appset_id, snapset_id, select=select)

Get details of snapsets identified by {snapsetId} for Applicationset identified by {appsetId} for Primera / Alletra 9K

Get details of snapset identified by {snapsetId} for Applicationset identified by {appsetId} for Primera / Alletra 9K

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
appset_id = 'appset_id_example' # str | UID of the applicationset
snapset_id = 'snapset_id_example' # str | Identifier of snapset.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of snapsets identified by {snapsetId} for Applicationset identified by {appsetId} for Primera / Alletra 9K
    api_response = api_instance.device_type1_snapsets_get_by_id(system_id, appset_id, snapset_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_snapsets_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **snapset_id** | **str**| Identifier of snapset. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**SnapshotsetListSingle**](SnapshotsetListSingle.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_set_capacity_statistics_get_by_id**
> PrimeraApplicationSetCapacityStats device_type1_volume_set_capacity_statistics_get_by_id(id, system_id, select=select)

Get capacity details for an applicationset identified by appsetUid

Get capacity details for an applicationset identified by appsetUid

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
id = 'id_example' # str | UID of the applicationset
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get capacity details for an applicationset identified by appsetUid
    api_response = api_instance.device_type1_volume_set_capacity_statistics_get_by_id(id, system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_volume_set_capacity_statistics_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UID of the applicationset | 
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraApplicationSetCapacityStats**](PrimeraApplicationSetCapacityStats.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_set_export**
> TaskResponse device_type1_volume_set_export(system_id, appset_id, export_app_set_post)

Export applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}

Export applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
appset_id = 'appset_id_example' # str | UID of the applicationset
export_app_set_post = greenlake-data-services.ExportAppSetPost() # ExportAppSetPost | 

try:
    # Export applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_volume_set_export(system_id, appset_id, export_app_set_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_volume_set_export: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **export_app_set_post** | [**ExportAppSetPost**](ExportAppSetPost.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_set_snapshot_get_by_id**
> TaskResponse device_type1_volume_set_snapshot_get_by_id(system_id, appset_id, snapset_id, force=force)

Remove Primera / Alletra 9K snapset in system identified by {snapsetId}

Remove Primera / Alletra 9K snapset in system identified by {snapsetId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
appset_id = 'appset_id_example' # str | UID of the applicationset
snapset_id = 'snapset_id_example' # str | Identifier of snapset.
force = True # bool | Make snapset offline and remove. (optional)

try:
    # Remove Primera / Alletra 9K snapset in system identified by {snapsetId}
    api_response = api_instance.device_type1_volume_set_snapshot_get_by_id(system_id, appset_id, snapset_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_volume_set_snapshot_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **snapset_id** | **str**| Identifier of snapset. | 
 **force** | **bool**| Make snapset offline and remove. | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_set_snapshots_list**
> SnapshotSetsSummaryList device_type1_volume_set_snapshots_list(system_id, id, limit=limit, offset=offset, select=select, filter=filter, sort=sort)

Get snapshot details of volume sets identified by {id} for Primera / Alletra 9K

Get snapshot details of volume sets identified by {id} for Primera / Alletra 9K

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the applicationset
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
filter = 'filter_example' # str | oData query to filter by Key. (optional)
sort = 'sort_example' # str | oData query to sort by Key. (optional)

try:
    # Get snapshot details of volume sets identified by {id} for Primera / Alletra 9K
    api_response = api_instance.device_type1_volume_set_snapshots_list(system_id, id, limit=limit, offset=offset, select=select, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_volume_set_snapshots_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the applicationset | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 

### Return type

[**SnapshotSetsSummaryList**](SnapshotSetsSummaryList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_set_unexport**
> TaskResponse device_type1_volume_set_unexport(system_id, appset_id, un_export_app_set_post)

Unexport applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}

Unexport applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
appset_id = 'appset_id_example' # str | UID of the applicationset
un_export_app_set_post = greenlake-data-services.UnExportAppSetPost() # UnExportAppSetPost | 

try:
    # Unexport applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_volume_set_unexport(system_id, appset_id, un_export_app_set_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_volume_set_unexport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **appset_id** | **str**| UID of the applicationset | 
 **un_export_app_set_post** | [**UnExportAppSetPost**](UnExportAppSetPost.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_set_volumes_list**
> PrimeraAppSetVolumes device_type1_volume_set_volumes_list(appset_id, system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get volumes for an applicationset identified by appsetUid

Get volumes for an applicationset identified by appsetUid

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
appset_id = 'appset_id_example' # str | UID of the applicationset
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter by Key. (optional)
sort = 'sort_example' # str | oData query to sort by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get volumes for an applicationset identified by appsetUid
    api_response = api_instance.device_type1_volume_set_volumes_list(appset_id, system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_volume_set_volumes_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **appset_id** | **str**| UID of the applicationset | 
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraAppSetVolumes**](PrimeraAppSetVolumes.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_sets_create**
> TaskResponse device_type1_volume_sets_create(system_id, create_app_set_input)

Create Application Set for a storage system Primera / Alletra 9K

Create Application Set for a storage system Primera / Alletra 9K

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
create_app_set_input = greenlake-data-services.CreateAppSetInput() # CreateAppSetInput | 

try:
    # Create Application Set for a storage system Primera / Alletra 9K
    api_response = api_instance.device_type1_volume_sets_create(system_id, create_app_set_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_volume_sets_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **create_app_set_input** | [**CreateAppSetInput**](CreateAppSetInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_sets_delete_by_id**
> TaskResponse device_type1_volume_sets_delete_by_id(system_id, id)

Remove applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}

Remove applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the applicationset

try:
    # Remove applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_volume_sets_delete_by_id(system_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_volume_sets_delete_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the applicationset | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_sets_edit_by_id**
> TaskResponse device_type1_volume_sets_edit_by_id(system_id, id, volume_set_put)

Edit applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}

Edit applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the applicationset
volume_set_put = greenlake-data-services.VolumeSetPut() # VolumeSetPut | 

try:
    # Edit applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}
    api_response = api_instance.device_type1_volume_sets_edit_by_id(system_id, id, volume_set_put)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_volume_sets_edit_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the applicationset | 
 **volume_set_put** | [**VolumeSetPut**](VolumeSetPut.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_sets_get_by_id**
> PrimeraApplicationSetDetails device_type1_volume_sets_get_by_id(id, system_id, select=select)

Get applicationset details for an applicationset identified by appsetUid

Get applicationset details for an applicationset identified by appsetUid

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
id = 'id_example' # str | UID of the applicationset
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get applicationset details for an applicationset identified by appsetUid
    api_response = api_instance.device_type1_volume_sets_get_by_id(id, system_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_volume_sets_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UID of the applicationset | 
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraApplicationSetDetails**](PrimeraApplicationSetDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_sets_list**
> PrimeraApplicationSetsList device_type1_volume_sets_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all applicationset details for Primera / Alletra 9K

Get all applicationset details for Primera / Alletra 9K

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter application-sets by Key. (optional)
sort = 'sort_example' # str | Lucene query to sort application-sets by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all applicationset details for Primera / Alletra 9K
    api_response = api_instance.device_type1_volume_sets_list(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_volume_sets_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter application-sets by Key. | [optional] 
 **sort** | **str**| Lucene query to sort application-sets by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**PrimeraApplicationSetsList**](PrimeraApplicationSetsList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1_volume_sets_snapshot_create**
> TaskResponse device_type1_volume_sets_snapshot_create(system_id, id, appset_post)

Create snapshot for application set identified by {id}

Create snapshot for application set identified by {id}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of the applicationset
appset_post = greenlake-data-services.AppsetPost() # AppsetPost | 

try:
    # Create snapshot for application set identified by {id}
    api_response = api_instance.device_type1_volume_sets_snapshot_create(system_id, id, appset_post)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1_volume_sets_snapshot_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of the applicationset | 
 **appset_post** | [**AppsetPost**](AppsetPost.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type1action_on_volume_sets**
> TaskResponse device_type1action_on_volume_sets(system_id, id, remote_protection_actions_input)

Actions on volume set identified by {id} and {systemId} from Primera / Alletra 9K

Actions on volume set identified by {id} and {systemId} from Primera / Alletra 9K

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | ID of the applicationset
remote_protection_actions_input = greenlake-data-services.RemoteProtectionActionsInput() # RemoteProtectionActionsInput | 

try:
    # Actions on volume set identified by {id} and {systemId} from Primera / Alletra 9K
    api_response = api_instance.device_type1action_on_volume_sets(system_id, id, remote_protection_actions_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type1action_on_volume_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| ID of the applicationset | 
 **remote_protection_actions_input** | [**RemoteProtectionActionsInput**](RemoteProtectionActionsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_action_on_snapshot_collection**
> TaskResponse device_type2_action_on_snapshot_collection(system_id, volume_collection_id, nimble_update_snapshot_collections_state_input)

Perform offline/online action on  snapshot collections of Nimble / Alletra 6K and associated with volume collection {volumeCollectionId}  in the system identified by {systemId}

Perform offline/online action on  snapshot collections of Nimble / Alletra 6K and associated with volume collection {volumeCollectionId}  in the system identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
nimble_update_snapshot_collections_state_input = greenlake-data-services.NimbleUpdateSnapshotCollectionsStateInput() # NimbleUpdateSnapshotCollectionsStateInput | 

try:
    # Perform offline/online action on  snapshot collections of Nimble / Alletra 6K and associated with volume collection {volumeCollectionId}  in the system identified by {systemId}
    api_response = api_instance.device_type2_action_on_snapshot_collection(system_id, volume_collection_id, nimble_update_snapshot_collections_state_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_action_on_snapshot_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **nimble_update_snapshot_collections_state_input** | [**NimbleUpdateSnapshotCollectionsStateInput**](NimbleUpdateSnapshotCollectionsStateInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_action_on_volume_collection**
> TaskResponse device_type2_action_on_volume_collection(system_id, volume_collection_id, nimble_handover_volume_collections_input)

Perform handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

Perform handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
nimble_handover_volume_collections_input = greenlake-data-services.NimbleHandoverVolumeCollectionsInput() # NimbleHandoverVolumeCollectionsInput | 

try:
    # Perform handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
    api_response = api_instance.device_type2_action_on_volume_collection(system_id, volume_collection_id, nimble_handover_volume_collections_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_action_on_volume_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **nimble_handover_volume_collections_input** | [**NimbleHandoverVolumeCollectionsInput**](NimbleHandoverVolumeCollectionsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_action_on_volume_collection_id**
> TaskResponse device_type2_action_on_volume_collection_id(system_id, volume_collection_id, nimble_demote_volume_collections_input)

Perform demote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

Perform demote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
nimble_demote_volume_collections_input = greenlake-data-services.NimbleDemoteVolumeCollectionsInput() # NimbleDemoteVolumeCollectionsInput | 

try:
    # Perform demote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
    api_response = api_instance.device_type2_action_on_volume_collection_id(system_id, volume_collection_id, nimble_demote_volume_collections_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_action_on_volume_collection_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **nimble_demote_volume_collections_input** | [**NimbleDemoteVolumeCollectionsInput**](NimbleDemoteVolumeCollectionsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_actionon_volume_collection**
> TaskResponse device_type2_actionon_volume_collection(system_id, volume_collection_id)

Perform abort handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

Perform abort handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.

try:
    # Perform abort handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
    api_response = api_instance.device_type2_actionon_volume_collection(system_id, volume_collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_actionon_volume_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_add_volumes_to_volume_collections**
> TaskResponse device_type2_add_volumes_to_volume_collections(system_id, volume_collection_id, nimble_add_volume_to_volume_collection_input)

Add volumes to Nimble / Alletra 6K volumes collection in system identified by {systemId}

Add volumes to Nimble / Alletra 6K volumes collection in system identified by {systemId

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of volumeCollection. A 42 digit hexadecimal number.
nimble_add_volume_to_volume_collection_input = greenlake-data-services.NimbleAddVolumeToVolumeCollectionInput() # NimbleAddVolumeToVolumeCollectionInput | 

try:
    # Add volumes to Nimble / Alletra 6K volumes collection in system identified by {systemId}
    api_response = api_instance.device_type2_add_volumes_to_volume_collections(system_id, volume_collection_id, nimble_add_volume_to_volume_collection_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_add_volumes_to_volume_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of volumeCollection. A 42 digit hexadecimal number. | 
 **nimble_add_volume_to_volume_collection_input** | [**NimbleAddVolumeToVolumeCollectionInput**](NimbleAddVolumeToVolumeCollectionInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_create_snapshot_collections**
> TaskResponse device_type2_create_snapshot_collections(system_id, volume_collection_id, nimble_create_snapshot_collections_input)

Create Nimble / Alletra 6K snapshot collection in system identified by {systemId}

Create Nimble / Alletra 6K snapshot collection in system identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
nimble_create_snapshot_collections_input = greenlake-data-services.NimbleCreateSnapshotCollectionsInput() # NimbleCreateSnapshotCollectionsInput | 

try:
    # Create Nimble / Alletra 6K snapshot collection in system identified by {systemId}
    api_response = api_instance.device_type2_create_snapshot_collections(system_id, volume_collection_id, nimble_create_snapshot_collections_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_create_snapshot_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **nimble_create_snapshot_collections_input** | [**NimbleCreateSnapshotCollectionsInput**](NimbleCreateSnapshotCollectionsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_edit_volume_collection_by_id**
> TaskResponse device_type2_edit_volume_collection_by_id(system_id, volume_collection_id, nimble_edit_volume_collection_input)

Edit  details of Nimble / Alletra 6K Volume-collections identified by {volumeCollectionId}

Edit  details of Nimble / Alletra 6K Volume-collections identified by {volumeCollectionId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of volumeCollection. A 42 digit hexadecimal number.
nimble_edit_volume_collection_input = greenlake-data-services.NimbleEditVolumeCollectionInput() # NimbleEditVolumeCollectionInput | 

try:
    # Edit  details of Nimble / Alletra 6K Volume-collections identified by {volumeCollectionId}
    api_response = api_instance.device_type2_edit_volume_collection_by_id(system_id, volume_collection_id, nimble_edit_volume_collection_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_edit_volume_collection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of volumeCollection. A 42 digit hexadecimal number. | 
 **nimble_edit_volume_collection_input** | [**NimbleEditVolumeCollectionInput**](NimbleEditVolumeCollectionInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_folders**
> NimbleFolderList device_type2_get_all_folders(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all folders details by Nimble / Alletra 6K

Get all folders details by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter folders by Key. (optional)
sort = 'sort_example' # str | oData query to sort folders resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all folders details by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_folders(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_get_all_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter folders by Key. | [optional] 
 **sort** | **str**| oData query to sort folders resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleFolderList**](NimbleFolderList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_all_volume_collections**
> NimbleVolumeCollectionList device_type2_get_all_volume_collections(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volume-collections details by Nimble / Alletra 6K

Get all volume-collections details by Nimble / Alletra 6K

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter volume-collection by Key. (optional)
sort = 'sort_example' # str | oData query to sort volume-collection resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all volume-collections details by Nimble / Alletra 6K
    api_response = api_instance.device_type2_get_all_volume_collections(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_get_all_volume_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter volume-collection by Key. | [optional] 
 **sort** | **str**| oData query to sort volume-collection resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleVolumeCollectionList**](NimbleVolumeCollectionList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_snapshot_collections_by_id**
> NimbleSnapshotCollectionDetails device_type2_get_snapshot_collections_by_id(system_id, volume_collection_id, snapshot_collection_id, select=select)

Get details of snapshot collection of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId} by {snapshotId}

Get details of snapshot collection of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId} by {snapshotId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
snapshot_collection_id = 'snapshot_collection_id_example' # str | Identifier of snapshot Collection. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of snapshot collection of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId} by {snapshotId}
    api_response = api_instance.device_type2_get_snapshot_collections_by_id(system_id, volume_collection_id, snapshot_collection_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_get_snapshot_collections_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **snapshot_collection_id** | **str**| Identifier of snapshot Collection. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleSnapshotCollectionDetails**](NimbleSnapshotCollectionDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_snapshots_by_volume_collection_id**
> NimbleSnapshotCollectionList device_type2_get_snapshots_by_volume_collection_id(system_id, volume_collection_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all snapshot collections' details of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId}

Get all snapshot collections' details of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | Lucene query to filter snapshot collections by Key. (optional)
sort = 'sort_example' # str | oData query to sort snapshot collections resource by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all snapshot collections' details of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId}
    api_response = api_instance.device_type2_get_snapshots_by_volume_collection_id(system_id, volume_collection_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_get_snapshots_by_volume_collection_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| Lucene query to filter snapshot collections by Key. | [optional] 
 **sort** | **str**| oData query to sort snapshot collections resource by Key. | [optional] 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleSnapshotCollectionList**](NimbleSnapshotCollectionList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_get_volume_collection_by_id**
> NimbleVCollectionDetailsWithRequestUri device_type2_get_volume_collection_by_id(system_id, volume_collection_id, select=select)

Get details of Nimble / Alletra 6K volume-collections identified by {volumeCollectionId}

Get details of Nimble / Alletra 6K volume-collections identified by {volumeCollectionId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of volumeCollection. A 42 digit hexadecimal number.
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get details of Nimble / Alletra 6K volume-collections identified by {volumeCollectionId}
    api_response = api_instance.device_type2_get_volume_collection_by_id(system_id, volume_collection_id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_get_volume_collection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of volumeCollection. A 42 digit hexadecimal number. | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**NimbleVCollectionDetailsWithRequestUri**](NimbleVCollectionDetailsWithRequestUri.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_promote_action_on_volume_collection**
> TaskResponse device_type2_promote_action_on_volume_collection(system_id, volume_collection_id)

Perform promote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

Perform promote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.

try:
    # Perform promote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}
    api_response = api_instance.device_type2_promote_action_on_volume_collection(system_id, volume_collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_promote_action_on_volume_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_snap_shot_collection**
> TaskResponse device_type2_remove_snap_shot_collection(system_id, volume_collection_id, remove_snapshot_collection_input)

Remove multiple snapshot collections identified by {volumeCollectionId} from Nimble / Alletra 6K

Remove multiple snapshot collections identified by {volumeCollectionId} from Nimble / Alletra 6K

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
remove_snapshot_collection_input = greenlake-data-services.RemoveSnapshotCollectionInput() # RemoveSnapshotCollectionInput | 

try:
    # Remove multiple snapshot collections identified by {volumeCollectionId} from Nimble / Alletra 6K
    api_response = api_instance.device_type2_remove_snap_shot_collection(system_id, volume_collection_id, remove_snapshot_collection_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_remove_snap_shot_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **remove_snapshot_collection_input** | [**RemoveSnapshotCollectionInput**](RemoveSnapshotCollectionInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_volume_collection_by_id**
> TaskResponse device_type2_remove_volume_collection_by_id(system_id, volume_collection_id, force=force)

Remove Volume-collection identified by {volumeCollectionId} from Nimble / Alletra 6K

Remove Volume-collection identified by {volumeCollectionId} from Nimble / Alletra 6K

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of Volume Collection. A 42 digit hexadecimal number.
force = True # bool | Forceful delete volume collection option. (optional)

try:
    # Remove Volume-collection identified by {volumeCollectionId} from Nimble / Alletra 6K
    api_response = api_instance.device_type2_remove_volume_collection_by_id(system_id, volume_collection_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_remove_volume_collection_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of Volume Collection. A 42 digit hexadecimal number. | 
 **force** | **bool**| Forceful delete volume collection option. | [optional] 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_remove_volumes_from_volume_collection**
> TaskResponse device_type2_remove_volumes_from_volume_collection(system_id, volume_collection_id, nimble_remove_volume_from_volume_collection_input)

Remove volumes from Nimble / Alletra 6K volumes collection in system identified by {systemId}

Remove volumes from Nimble / Alletra 6K volumes collection in system identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
volume_collection_id = 'volume_collection_id_example' # str | Identifier of volumeCollection. A 42 digit hexadecimal number.
nimble_remove_volume_from_volume_collection_input = greenlake-data-services.NimbleRemoveVolumeFromVolumeCollectionInput() # NimbleRemoveVolumeFromVolumeCollectionInput | 

try:
    # Remove volumes from Nimble / Alletra 6K volumes collection in system identified by {systemId}
    api_response = api_instance.device_type2_remove_volumes_from_volume_collection(system_id, volume_collection_id, nimble_remove_volume_from_volume_collection_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_remove_volumes_from_volume_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **volume_collection_id** | **str**| Identifier of volumeCollection. A 42 digit hexadecimal number. | 
 **nimble_remove_volume_from_volume_collection_input** | [**NimbleRemoveVolumeFromVolumeCollectionInput**](NimbleRemoveVolumeFromVolumeCollectionInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **device_type2_volume_collection_create**
> TaskResponse device_type2_volume_collection_create(system_id, nimble_create_volume_collection_input)

Create Nimble / Alletra 6K volume collection in system identified by {systemId}

Create Nimble / Alletra 6K volume collection in system identified by {systemId}

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
nimble_create_volume_collection_input = greenlake-data-services.NimbleCreateVolumeCollectionInput() # NimbleCreateVolumeCollectionInput | 

try:
    # Create Nimble / Alletra 6K volume collection in system identified by {systemId}
    api_response = api_instance.device_type2_volume_collection_create(system_id, nimble_create_volume_collection_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->device_type2_volume_collection_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **nimble_create_volume_collection_input** | [**NimbleCreateVolumeCollectionInput**](NimbleCreateVolumeCollectionInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumeset_get_by_id**
> FleetVolumeSetDetails volumeset_get_by_id(id, select=select)

Get volume-set identified by id

Get volume-set identified by id

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
id = 'id_example' # str | UID of Volume Set
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get volume-set identified by id
    api_response = api_instance.volumeset_get_by_id(id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->volumeset_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UID of Volume Set | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetVolumeSetDetails**](FleetVolumeSetDetails.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumeset_get_byvolumeset_id**
> FleetVolumeset volumeset_get_byvolumeset_id(id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)

Get volumes identified by volume set id

Get volumes  identified by volume set id

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
id = 'id_example' # str | UID of Volume Set
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter by Key. (optional)
sort = 'sort_example' # str | oData query to sort by Key. (optional)

try:
    # Get volumes identified by volume set id
    api_response = api_instance.volumeset_get_byvolumeset_id(id, select=select, limit=limit, offset=offset, filter=filter, sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->volumeset_get_byvolumeset_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| UID of Volume Set | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 
 **limit** | **int**| Number of items to return at a time | [optional] 
 **offset** | **int**| The offset of the first item in the collection to return | [optional] 
 **filter** | **str**| oData query to filter by Key. | [optional] 
 **sort** | **str**| oData query to sort by Key. | [optional] 

### Return type

[**FleetVolumeset**](FleetVolumeset.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumeset_list**
> FleetVolumeSetList volumeset_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volume-sets

Get all volume sets

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter by Key. (optional)
sort = 'sort_example' # str | oData query to sort by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all volume-sets
    api_response = api_instance.volumeset_list(limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->volumeset_list: %s\n" % e)
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

[**FleetVolumeSetList**](FleetVolumeSetList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumeset_list_for_system_by_system_id**
> FleetVolumeSetList volumeset_list_for_system_by_system_id(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)

Get all volume-sets for a systemId

Get all volume sets for a systemId

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
limit = 56 # int | Number of items to return at a time (optional)
offset = 56 # int | The offset of the first item in the collection to return (optional)
filter = 'filter_example' # str | oData query to filter by Key. (optional)
sort = 'sort_example' # str | oData query to sort by Key. (optional)
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get all volume-sets for a systemId
    api_response = api_instance.volumeset_list_for_system_by_system_id(system_id, limit=limit, offset=offset, filter=filter, sort=sort, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->volumeset_list_for_system_by_system_id: %s\n" % e)
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

[**FleetVolumeSetList**](FleetVolumeSetList.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumeset_system_get_by_id**
> FleetSystemVolumeset volumeset_system_get_by_id(system_id, id, select=select)

Get volume-set identified by id

Get volume-set identified by id

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
api_instance = greenlake-data-services.VolumeSetsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | systemId of the device-type1 storage system
id = 'id_example' # str | UID of Volume Set
select = 'select_example' # str | Query to select only the required parameters, separated by . if nested (optional)

try:
    # Get volume-set identified by id
    api_response = api_instance.volumeset_system_get_by_id(system_id, id, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VolumeSetsApi->volumeset_system_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| systemId of the device-type1 storage system | 
 **id** | **str**| UID of Volume Set | 
 **select** | **str**| Query to select only the required parameters, separated by . if nested | [optional] 

### Return type

[**FleetSystemVolumeset**](FleetSystemVolumeset.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

