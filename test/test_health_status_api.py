"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import greenlake_data_services
from greenlake_data_services.api.health_status_api import HealthStatusApi  # noqa: E501


class TestHealthStatusApi(unittest.TestCase):
    """HealthStatusApi unit test stubs"""

    def setUp(self):
        self.api = HealthStatusApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_type2_get_health_status(self):
        """Test case for device_type2_get_health_status

        Get details of  Nimble / Alletra 6K health status  # noqa: E501
        """
        pass

    def test_device_type2_get_health_status_using_health_id(self):
        """Test case for device_type2_get_health_status_using_health_id

        Get details of  Nimble / Alletra 6K health status identified by {healthStatusId}  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
