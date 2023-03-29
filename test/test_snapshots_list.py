"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import greenlake_data_services
from greenlake_data_services.model.calendar import Calendar
from greenlake_data_services.model.policy import Policy
from greenlake_data_services.model.primera_application_set_details_initiators_inner import PrimeraApplicationSetDetailsInitiatorsInner
from greenlake_data_services.model.snapshot_tdvvsize import SnapshotTdvvsize
from greenlake_data_services.model.snapshots_list_creation_time import SnapshotsListCreationTime
from greenlake_data_services.model.space import Space
from greenlake_data_services.model.state import STATE
from greenlake_data_services.model.user_allocation_settings_single import UserAllocationSettingsSingle
globals()['Calendar'] = Calendar
globals()['Policy'] = Policy
globals()['PrimeraApplicationSetDetailsInitiatorsInner'] = PrimeraApplicationSetDetailsInitiatorsInner
globals()['STATE'] = STATE
globals()['SnapshotTdvvsize'] = SnapshotTdvvsize
globals()['SnapshotsListCreationTime'] = SnapshotsListCreationTime
globals()['Space'] = Space
globals()['UserAllocationSettingsSingle'] = UserAllocationSettingsSingle
from greenlake_data_services.model.snapshots_list import SnapshotsList


class TestSnapshotsList(unittest.TestCase):
    """SnapshotsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSnapshotsList(self):
        """Test SnapshotsList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SnapshotsList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
