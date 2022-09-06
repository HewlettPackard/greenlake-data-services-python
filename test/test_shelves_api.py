"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import greenlake_data_services
from greenlake_data_services.api.shelves_api import ShelvesApi  # noqa: E501


class TestShelvesApi(unittest.TestCase):
    """ShelvesApi unit test stubs"""

    def setUp(self):
        self.api = ShelvesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_type1_disks_get_by_id(self):
        """Test case for device_type1_disks_get_by_id

        Get details of Primera / Alletra 9K disk identified by {cageId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_disks_list(self):
        """Test case for device_type1_disks_list

        Get details of Primera / Alletra 9K disks identified by {cageId}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_card_ports_get_by_id(self):
        """Test case for device_type1_enclosure_card_ports_get_by_id

        Get details of Primera / Alletra 9K Enclosure Card Port identified by {enclosureId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_card_ports_list(self):
        """Test case for device_type1_enclosure_card_ports_list

        Get details of Primera / Alletra 9K Enclosure Card Ports identified by {enclosureId}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_cards_get_by_id(self):
        """Test case for device_type1_enclosure_cards_get_by_id

        Get details of Primera / Alletra 9K Enclosure Card identified by {enclosureId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_cards_list(self):
        """Test case for device_type1_enclosure_cards_list

        Get details of Primera / Alletra 9K Enclosure Cards identified by {enclosureId}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_disks_get_by_id(self):
        """Test case for device_type1_enclosure_disks_get_by_id

        Get details of Primera / Alletra 9K Enclosure Disk identified by {enclosureId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_disks_list(self):
        """Test case for device_type1_enclosure_disks_list

        Get details of Primera / Alletra 9K Enclosure Disks identified by {enclosureId}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_expanders_get_by_id(self):
        """Test case for device_type1_enclosure_expanders_get_by_id

        Get details of Primera / Alletra 9K Enclosure Expander identified by {enclosureId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_expanders_list(self):
        """Test case for device_type1_enclosure_expanders_list

        Get details of Primera / Alletra 9K Enclosure Expanders identified by {enclosureId}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_fans_get_by_id(self):
        """Test case for device_type1_enclosure_fans_get_by_id

        Get details of Primera / Alletra 9K Enclosure Fan identified by {enclosureId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_fans_list(self):
        """Test case for device_type1_enclosure_fans_list

        Get details of Primera / Alletra 9K Enclosure Fans identified by {enclosureId}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_powers_get_by_id(self):
        """Test case for device_type1_enclosure_powers_get_by_id

        Get details of Primera / Alletra 9K Enclosure Power identified by {enclosureId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_powers_list(self):
        """Test case for device_type1_enclosure_powers_list

        Get details of Primera / Alletra 9K Enclosure Powers identified by {enclosureId}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_sleds_get_by_id(self):
        """Test case for device_type1_enclosure_sleds_get_by_id

        Get details of Primera / Alletra 9K Enclosure Sled identified by {enclosureId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_enclosure_sleds_list(self):
        """Test case for device_type1_enclosure_sleds_list

        Get details of Primera / Alletra 9K Enclosure Sleds identified by {enclosureId}  # noqa: E501
        """
        pass

    def test_device_type1_enclosures_get_by_id(self):
        """Test case for device_type1_enclosures_get_by_id

        Get details of Primera / Alletra 9K Enclosure identified by {id}  # noqa: E501
        """
        pass

    def test_device_type1_enclosures_list(self):
        """Test case for device_type1_enclosures_list

        Get details of Primera / Alletra 9K Enclosures  # noqa: E501
        """
        pass

    def test_device_type2_activate_shelf(self):
        """Test case for device_type2_activate_shelf

        Activate shelves of a Nimble / Alletra 6K storage system identified by {systemId}  # noqa: E501
        """
        pass

    def test_device_type2_get_all_shelves(self):
        """Test case for device_type2_get_all_shelves

        Get all shelves details by Nimble / Alletra 6K  # noqa: E501
        """
        pass

    def test_device_type2_get_shelf_by_id(self):
        """Test case for device_type2_get_shelf_by_id

        Get details of Nimble / Alletra 6K Shelf identified by {shelfId}  # noqa: E501
        """
        pass

    def test_device_type2_locate_shelf_chassis(self):
        """Test case for device_type2_locate_shelf_chassis

        Locate chassis of Nimble / Alletra 6K shelf identified by {shelfId}  # noqa: E501
        """
        pass

    def test_enclosure_cards_locate_ioby_id(self):
        """Test case for enclosure_cards_locate_ioby_id

        Locate IO Module of Primera / Alletra 9K identified by {id}  # noqa: E501
        """
        pass

    def test_enclosure_powers_locate_pcmby_id(self):
        """Test case for enclosure_powers_locate_pcmby_id

        Locate PCM of Primera / Alletra 9K identified by {id}  # noqa: E501
        """
        pass

    def test_enclosure_sleds_locate_drive_by_id(self):
        """Test case for enclosure_sleds_locate_drive_by_id

        Locate drive of Primera / Alletra 9K identified by {id}  # noqa: E501
        """
        pass

    def test_enclosures_edit_by_id(self):
        """Test case for enclosures_edit_by_id

        Edit details of Primera / Alletra 9K Enclosure identified by {id}  # noqa: E501
        """
        pass

    def test_enclosures_locate_by_id(self):
        """Test case for enclosures_locate_by_id

        Locate enclosure drive of Primera / Alletra 9K identified by {id}  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()