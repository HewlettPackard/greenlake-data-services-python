# greenlake-data-services.RestorePointsApi

All URIs are relative to *https://eu1.data.cloud.hpe.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**device_type2_clone_action_on_snapshot_collections**](RestorePointsApi.md#device_type2_clone_action_on_snapshot_collections) | **POST** /api/v1/storage-systems/device-type2/{systemId}/snapshot-collections/{snapshotCollectionId}/actions/clone | Perform action clone Nimble / Alletra 6K on a snapshot collection identified by {snapshotCollectionId} in system identified by {systemId}


# **device_type2_clone_action_on_snapshot_collections**
> TaskResponse device_type2_clone_action_on_snapshot_collections(system_id, snapshot_collection_id, nimble_clone_snapshot_collections_input)

Perform action clone Nimble / Alletra 6K on a snapshot collection identified by {snapshotCollectionId} in system identified by {systemId}

Perform action clone Nimble / Alletra 6K on a snapshot collection identified by {snapshotCollectionId} in system identified by {systemId}

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
api_instance = greenlake-data-services.RestorePointsApi(greenlake-data-services.ApiClient(configuration))
system_id = 'system_id_example' # str | ID of the storage system
snapshot_collection_id = 'snapshot_collection_id_example' # str | Identifier of snapshot Collection. A 42 digit hexadecimal number.
nimble_clone_snapshot_collections_input = greenlake-data-services.NimbleCloneSnapshotCollectionsInput() # NimbleCloneSnapshotCollectionsInput | 

try:
    # Perform action clone Nimble / Alletra 6K on a snapshot collection identified by {snapshotCollectionId} in system identified by {systemId}
    api_response = api_instance.device_type2_clone_action_on_snapshot_collections(system_id, snapshot_collection_id, nimble_clone_snapshot_collections_input)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RestorePointsApi->device_type2_clone_action_on_snapshot_collections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **str**| ID of the storage system | 
 **snapshot_collection_id** | **str**| Identifier of snapshot Collection. A 42 digit hexadecimal number. | 
 **nimble_clone_snapshot_collections_input** | [**NimbleCloneSnapshotCollectionsInput**](NimbleCloneSnapshotCollectionsInput.md)|  | 

### Return type

[**TaskResponse**](TaskResponse.md)

### Authorization

[JWTAuth](../README.md#JWTAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

