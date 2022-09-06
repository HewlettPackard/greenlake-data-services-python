"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import greenlake_data_services
from greenlake_data_services.model.details import Details
from greenlake_data_services.model.sys_associated_links import SysAssociatedLinks
from greenlake_data_services.model.telemetry_status_connectivity_test_time import TelemetryStatusConnectivityTestTime
from greenlake_data_services.model.telemetry_status_last_file_transfer_time import TelemetryStatusLastFileTransferTime
from greenlake_data_services.model.telemetry_status_last_successful_connectivity_test_time import TelemetryStatusLastSuccessfulConnectivityTestTime
globals()['Details'] = Details
globals()['SysAssociatedLinks'] = SysAssociatedLinks
globals()['TelemetryStatusConnectivityTestTime'] = TelemetryStatusConnectivityTestTime
globals()['TelemetryStatusLastFileTransferTime'] = TelemetryStatusLastFileTransferTime
globals()['TelemetryStatusLastSuccessfulConnectivityTestTime'] = TelemetryStatusLastSuccessfulConnectivityTestTime
from greenlake_data_services.model.telemetry_status import TelemetryStatus


class TestTelemetryStatus(unittest.TestCase):
    """TelemetryStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTelemetryStatus(self):
        """Test TelemetryStatus"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TelemetryStatus()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()