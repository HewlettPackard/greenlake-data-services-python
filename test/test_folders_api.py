"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import greenlake_data_services
from greenlake_data_services.api.folders_api import FoldersApi  # noqa: E501


class TestFoldersApi(unittest.TestCase):
    """FoldersApi unit test stubs"""

    def setUp(self):
        self.api = FoldersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_type2_folder_create(self):
        """Test case for device_type2_folder_create

        Create Nimble / Alletra 6K folder in system identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type2_folder_edit(self):
        """Test case for device_type2_folder_edit

        Edit details of Nimble / Alletra 6K folder identified by {folderId}  # noqa: E501
        """
        pass

    def test_device_type2_get_folder_by_id(self):
        """Test case for device_type2_get_folder_by_id

        Get details of Nimble / Alletra 6K Folders identified by {folderId}  # noqa: E501
        """
        pass

    def test_device_type2_remove_folder_by_id(self):
        """Test case for device_type2_remove_folder_by_id

        Remove Nimble / Alletra 6K folder identified by {folderId}  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
