# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    OpenAPI spec version: 1.2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import greenlake-data-services
from greenlake-data-services.api.performance_templates_api import PerformanceTemplatesApi  # noqa: E501
from greenlake-data-services.rest import ApiException


class TestPerformanceTemplatesApi(unittest.TestCase):
    """PerformanceTemplatesApi unit test stubs"""

    def setUp(self):
        self.api = greenlake-data-services.api.performance_templates_api.PerformanceTemplatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_type2_get_all_performance_policies(self):
        """Test case for device_type2_get_all_performance_policies

        Get all performance-policies details by Nimble / Alletra 6K  # noqa: E501
        """
        pass

    def test_device_type2_get_performance_policy_by_id(self):
        """Test case for device_type2_get_performance_policy_by_id

        Get details of Nimble / Alletra 6K performance-policy identified by {performancePolicyId}  # noqa: E501
        """
        pass

    def test_device_type2_performance_policy_create(self):
        """Test case for device_type2_performance_policy_create

        Create Nimble / Alletra 6K performance policy in a system identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type2_performance_policy_edit(self):
        """Test case for device_type2_performance_policy_edit

        Edit details of Nimble / Alletra 6K performance policy identified by {performancePolicyId}  # noqa: E501
        """
        pass

    def test_device_type2_remove_perf_policy_id(self):
        """Test case for device_type2_remove_perf_policy_id

        Remove performance-policies identified by {performancePolicyId} from Nimble / Alletra 6K  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
