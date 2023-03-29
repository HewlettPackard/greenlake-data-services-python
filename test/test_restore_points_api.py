"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import greenlake_data_services
from greenlake_data_services.api.restore_points_api import RestorePointsApi  # noqa: E501


class TestRestorePointsApi(unittest.TestCase):
    """RestorePointsApi unit test stubs"""

    def setUp(self):
        self.api = RestorePointsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_type2_clone_action_on_snapshot_collections(self):
        """Test case for device_type2_clone_action_on_snapshot_collections

        Perform action clone Nimble / Alletra 6K on a snapshot collection identified by {snapshotCollectionId} in system identified by {systemId}  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
