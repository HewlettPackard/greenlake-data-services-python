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
from greenlake-data-services.api.audit_api import AuditApi  # noqa: E501
from greenlake-data-services.rest import ApiException


class TestAuditApi(unittest.TestCase):
    """AuditApi unit test stubs"""

    def setUp(self):
        self.api = greenlake-data-services.api.audit_api.AuditApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_audit_events_get(self):
        """Test case for audit_events_get

        GET audit-events  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
