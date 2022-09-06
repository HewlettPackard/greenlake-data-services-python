"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import greenlake_data_services
from greenlake_data_services.model.associated_links import AssociatedLinks
from greenlake_data_services.model.collection_status import CollectionStatus
from greenlake_data_services.model.connection_status import ConnectionStatus
from greenlake_data_services.model.ips import Ips
from greenlake_data_services.model.nimble_array_summary import NimbleArraySummary
globals()['AssociatedLinks'] = AssociatedLinks
globals()['CollectionStatus'] = CollectionStatus
globals()['ConnectionStatus'] = ConnectionStatus
globals()['Ips'] = Ips
globals()['NimbleArraySummary'] = NimbleArraySummary
from greenlake_data_services.model.storage_system_detail import StorageSystemDetail


class TestStorageSystemDetail(unittest.TestCase):
    """StorageSystemDetail unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStorageSystemDetail(self):
        """Test StorageSystemDetail"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StorageSystemDetail()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
