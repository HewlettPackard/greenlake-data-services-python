"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import greenlake_data_services
from greenlake_data_services.api.host_sets_api import HostSetsApi  # noqa: E501


class TestHostSetsApi(unittest.TestCase):
    """HostSetsApi unit test stubs"""

    def setUp(self):
        self.api = HostSetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_type1_get_all_host_sets(self):
        """Test case for device_type1_get_all_host_sets

        Get details of Primera / Alletra 9K Host Sets  # noqa: E501
        """
        pass

    def test_device_type1_get_host_sets_by_id(self):
        """Test case for device_type1_get_host_sets_by_id

        Get details of Primera / Alletra 9K Host Set identified by {HostSetId}  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
