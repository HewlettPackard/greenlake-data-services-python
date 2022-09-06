"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import greenlake_data_services
from greenlake_data_services.model.card_type import CardType
from greenlake_data_services.model.connected_devices import ConnectedDevices
from greenlake_data_services.model.initiator_port import InitiatorPort
from greenlake_data_services.model.manufacturing_single import ManufacturingSingle
from greenlake_data_services.model.partner_port import PartnerPort
from greenlake_data_services.model.port_fc import PortFC
from greenlake_data_services.model.port_ip import PortIP
from greenlake_data_services.model.port_iscsi import PortISCSI
from greenlake_data_services.model.port_position import PortPosition
from greenlake_data_services.model.port_sfp import PortSfp
from greenlake_data_services.model.ports_associated_links import PortsAssociatedLinks
from greenlake_data_services.model.state import STATE
from greenlake_data_services.model.state_description import StateDescription
from greenlake_data_services.model.vlan import Vlan
globals()['CardType'] = CardType
globals()['ConnectedDevices'] = ConnectedDevices
globals()['InitiatorPort'] = InitiatorPort
globals()['ManufacturingSingle'] = ManufacturingSingle
globals()['PartnerPort'] = PartnerPort
globals()['PortFC'] = PortFC
globals()['PortIP'] = PortIP
globals()['PortISCSI'] = PortISCSI
globals()['PortPosition'] = PortPosition
globals()['PortSfp'] = PortSfp
globals()['PortsAssociatedLinks'] = PortsAssociatedLinks
globals()['STATE'] = STATE
globals()['StateDescription'] = StateDescription
globals()['Vlan'] = Vlan
from greenlake_data_services.model.port_details import PortDetails


class TestPortDetails(unittest.TestCase):
    """PortDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPortDetails(self):
        """Test PortDetails"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PortDetails()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
