"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import greenlake_data_services
from greenlake_data_services.api.volume_sets_api import VolumeSetsApi  # noqa: E501


class TestVolumeSetsApi(unittest.TestCase):
    """VolumeSetsApi unit test stubs"""

    def setUp(self):
        self.api = VolumeSetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_type1_edit_proximity_settings(self):
        """Test case for device_type1_edit_proximity_settings

        Change proximity settings of hosts where volume sets are exported identified by {id} and {systemId} from Primera / Alletra 9K  # noqa: E501
        """
        pass

    def test_device_type1_get_proximity_settings(self):
        """Test case for device_type1_get_proximity_settings

        Get hosts and proximity details identified by application set {id} for Primera / Alletra 9K identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type1_get_replication_partner_volumes_by_app_set_id(self):
        """Test case for device_type1_get_replication_partner_volumes_by_app_set_id

        Get volume details of replication partners identified by {appsetId} and {replicationPartnerId} for Primera / Alletra 9K  # noqa: E501
        """
        pass

    def test_device_type1_get_replication_partners_by_app_set_id(self):
        """Test case for device_type1_get_replication_partners_by_app_set_id

        Get details of Primera / Alletra 9K replication partners identified by {systemId} and {appsetId}  # noqa: E501
        """
        pass

    def test_device_type1_snapsets_get_by_id(self):
        """Test case for device_type1_snapsets_get_by_id

        Get details of snapsets identified by {snapsetId} for Applicationset identified by {appsetId} for Primera / Alletra 9K  # noqa: E501
        """
        pass

    def test_device_type1_volume_set_capacity_statistics_get_by_id(self):
        """Test case for device_type1_volume_set_capacity_statistics_get_by_id

        Get capacity details for an applicationset identified by appsetUid  # noqa: E501
        """
        pass

    def test_device_type1_volume_set_export(self):
        """Test case for device_type1_volume_set_export

        Export applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type1_volume_set_snapshot_get_by_id(self):
        """Test case for device_type1_volume_set_snapshot_get_by_id

        Remove Primera / Alletra 9K snapset in system identified by {snapsetId}  # noqa: E501
        """
        pass

    def test_device_type1_volume_set_snapshots_list(self):
        """Test case for device_type1_volume_set_snapshots_list

        Get snapshot details of volume sets identified by {id} for Primera / Alletra 9K  # noqa: E501
        """
        pass

    def test_device_type1_volume_set_unexport(self):
        """Test case for device_type1_volume_set_unexport

        Unexport applicationset identified by {appsetId} from Primera / Alletra 9K identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type1_volume_set_volumes_list(self):
        """Test case for device_type1_volume_set_volumes_list

        Get volumes for an applicationset identified by appsetUid  # noqa: E501
        """
        pass

    def test_device_type1_volume_sets_create(self):
        """Test case for device_type1_volume_sets_create

        Create Application Set for a storage system Primera / Alletra 9K  # noqa: E501
        """
        pass

    def test_device_type1_volume_sets_delete_by_id(self):
        """Test case for device_type1_volume_sets_delete_by_id

        Remove applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type1_volume_sets_edit_by_id(self):
        """Test case for device_type1_volume_sets_edit_by_id

        Edit applicationset identified by {id} from Primera / Alletra 9K identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type1_volume_sets_get_by_id(self):
        """Test case for device_type1_volume_sets_get_by_id

        Get applicationset details for an applicationset identified by appsetUid  # noqa: E501
        """
        pass

    def test_device_type1_volume_sets_list(self):
        """Test case for device_type1_volume_sets_list

        Get all applicationset details for Primera / Alletra 9K  # noqa: E501
        """
        pass

    def test_device_type1_volume_sets_snapshot_create(self):
        """Test case for device_type1_volume_sets_snapshot_create

        Create snapshot for application set identified by {id}  # noqa: E501
        """
        pass

    def test_device_type1action_on_volume_sets(self):
        """Test case for device_type1action_on_volume_sets

        Actions on volume set identified by {id} and {systemId} from Primera / Alletra 9K  # noqa: E501
        """
        pass

    def test_device_type2_action_on_snapshot_collection(self):
        """Test case for device_type2_action_on_snapshot_collection

        Perform offline/online action on  snapshot collections of Nimble / Alletra 6K and associated with volume collection {volumeCollectionId}  in the system identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type2_action_on_volume_collection(self):
        """Test case for device_type2_action_on_volume_collection

        Perform handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type2_action_on_volume_collection_id(self):
        """Test case for device_type2_action_on_volume_collection_id

        Perform demote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type2_actionon_volume_collection(self):
        """Test case for device_type2_actionon_volume_collection

        Perform abort handover action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type2_add_volumes_to_volume_collections(self):
        """Test case for device_type2_add_volumes_to_volume_collections

        Add volumes to Nimble / Alletra 6K volumes collection in system identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type2_create_snapshot_collections(self):
        """Test case for device_type2_create_snapshot_collections

        Create Nimble / Alletra 6K snapshot collection in system identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type2_edit_volume_collection_by_id(self):
        """Test case for device_type2_edit_volume_collection_by_id

        Edit  details of Nimble / Alletra 6K Volume-collections identified by {volumeCollectionId}  # noqa: E501
        """
        pass

    def test_device_type2_get_all_folders(self):
        """Test case for device_type2_get_all_folders

        Get all folders details by Nimble / Alletra 6K  # noqa: E501
        """
        pass

    def test_device_type2_get_all_volume_collections(self):
        """Test case for device_type2_get_all_volume_collections

        Get all volume-collections details by Nimble / Alletra 6K  # noqa: E501
        """
        pass

    def test_device_type2_get_snapshot_collections_by_id(self):
        """Test case for device_type2_get_snapshot_collections_by_id

        Get details of snapshot collection of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId} by {snapshotId}  # noqa: E501
        """
        pass

    def test_device_type2_get_snapshots_by_volume_collection_id(self):
        """Test case for device_type2_get_snapshots_by_volume_collection_id

        Get all snapshot collections' details of Nimble / Alletra 6K Volume collection identified by {volumeCollectionId}  # noqa: E501
        """
        pass

    def test_device_type2_get_volume_collection_by_id(self):
        """Test case for device_type2_get_volume_collection_by_id

        Get details of Nimble / Alletra 6K volume-collections identified by {volumeCollectionId}  # noqa: E501
        """
        pass

    def test_device_type2_promote_action_on_volume_collection(self):
        """Test case for device_type2_promote_action_on_volume_collection

        Perform promote action Nimble / Alletra 6K on a volume collection identified by {volumeCollectionId} in system identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type2_remove_snap_shot_collection(self):
        """Test case for device_type2_remove_snap_shot_collection

        Remove multiple snapshot collections identified by {volumeCollectionId} from Nimble / Alletra 6K  # noqa: E501
        """
        pass

    def test_device_type2_remove_volume_collection_by_id(self):
        """Test case for device_type2_remove_volume_collection_by_id

        Remove Volume-collection identified by {volumeCollectionId} from Nimble / Alletra 6K  # noqa: E501
        """
        pass

    def test_device_type2_remove_volumes_from_volume_collection(self):
        """Test case for device_type2_remove_volumes_from_volume_collection

        Remove volumes from Nimble / Alletra 6K volumes collection in system identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type2_volume_collection_create(self):
        """Test case for device_type2_volume_collection_create

        Create Nimble / Alletra 6K volume collection in system identified by {systemId}  # noqa: E501
        """
        pass

    def test_volumeset_get_by_id(self):
        """Test case for volumeset_get_by_id

        Get volume-set identified by id  # noqa: E501
        """
        pass

    def test_volumeset_get_byvolumeset_id(self):
        """Test case for volumeset_get_byvolumeset_id

        Get volumes identified by volume set id  # noqa: E501
        """
        pass

    def test_volumeset_list(self):
        """Test case for volumeset_list

        Get all volume-sets  # noqa: E501
        """
        pass

    def test_volumeset_list_for_system_by_system_id(self):
        """Test case for volumeset_list_for_system_by_system_id

        Get all volume-sets for a systemId  # noqa: E501
        """
        pass

    def test_volumeset_system_get_by_id(self):
        """Test case for volumeset_system_get_by_id

        Get volume-set identified by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
