"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import greenlake_data_services
from greenlake_data_services.model.led import LED
from greenlake_data_services.model.manufacturing_single import ManufacturingSingle
from greenlake_data_services.model.node_associated_links import NodeAssociatedLinks
from greenlake_data_services.model.nodeuptime import Nodeuptime
from greenlake_data_services.model.state import STATE
globals()['LED'] = LED
globals()['ManufacturingSingle'] = ManufacturingSingle
globals()['NodeAssociatedLinks'] = NodeAssociatedLinks
globals()['Nodeuptime'] = Nodeuptime
globals()['STATE'] = STATE
from greenlake_data_services.model.node_details import NodeDetails


class TestNodeDetails(unittest.TestCase):
    """NodeDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNodeDetails(self):
        """Test NodeDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NodeDetails()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
