"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import greenlake_data_services
from greenlake_data_services.api.hosts_api import HostsApi  # noqa: E501


class TestHostsApi(unittest.TestCase):
    """HostsApi unit test stubs"""

    def setUp(self):
        self.api = HostsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_type1_get_all_hosts(self):
        """Test case for device_type1_get_all_hosts

        Get details of Primera / Alletra 9K Hosts  # noqa: E501
        """
        pass

    def test_device_type1_get_host_by_id(self):
        """Test case for device_type1_get_host_by_id

        Get details of Primera / Alletra 9K Host identified by {HostId}  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
