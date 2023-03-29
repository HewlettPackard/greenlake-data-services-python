"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import greenlake_data_services
from greenlake_data_services.api.controllers_api import ControllersApi  # noqa: E501


class TestControllersApi(unittest.TestCase):
    """ControllersApi unit test stubs"""

    def setUp(self):
        self.api = ControllersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_device_type1_node_batteries_get_by_id(self):
        """Test case for device_type1_node_batteries_get_by_id

        Get details of Primera / Alletra 9K Node Battery identified by {nodeId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_node_batteries_list(self):
        """Test case for device_type1_node_batteries_list

        Get details of Primera / Alletra 9K Node Batteries identified by {nodeId}  # noqa: E501
        """
        pass

    def test_device_type1_node_cards_get_by_id(self):
        """Test case for device_type1_node_cards_get_by_id

        Get details of Primera / Alletra 9K Node Card identified by {nodeId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_node_cards_list(self):
        """Test case for device_type1_node_cards_list

        Get details of Primera / Alletra 9K Node Cards identified by {nodeId}  # noqa: E501
        """
        pass

    def test_device_type1_node_component_performance_statistics_get(self):
        """Test case for device_type1_node_component_performance_statistics_get

        Get component performance statistics details of Primera / Alletra 9K node idenfified by {nodeId}  # noqa: E501
        """
        pass

    def test_device_type1_node_cpus_get_by_id(self):
        """Test case for device_type1_node_cpus_get_by_id

        Get details of Primera / Alletra 9K Node Cpu identified by {nodeId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_node_cpus_list(self):
        """Test case for device_type1_node_cpus_list

        Get details of Primera / Alletra 9K Node Cpus identified by {nodeId}  # noqa: E501
        """
        pass

    def test_device_type1_node_drives_get_by_id(self):
        """Test case for device_type1_node_drives_get_by_id

        Get details of Primera / Alletra 9K Node Drive identified by {nodeId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_node_drives_list(self):
        """Test case for device_type1_node_drives_list

        Get details of Primera / Alletra 9K Node Drives identified by {nodeId}  # noqa: E501
        """
        pass

    def test_device_type1_node_mcus_get_by_id(self):
        """Test case for device_type1_node_mcus_get_by_id

        Get details of Primera / Alletra 9K Node Mcu identified by {nodeId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_node_mcus_list(self):
        """Test case for device_type1_node_mcus_list

        Get details of Primera / Alletra 9K Node Mcus identified by {nodeId}  # noqa: E501
        """
        pass

    def test_device_type1_node_mems_get_by_id(self):
        """Test case for device_type1_node_mems_get_by_id

        Get details of Primera / Alletra 9K Node Memory identified by {nodeId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_node_mems_list(self):
        """Test case for device_type1_node_mems_list

        Get details of Primera / Alletra 9K Node Memories identified by {nodeId}  # noqa: E501
        """
        pass

    def test_device_type1_node_powers_get_by_id(self):
        """Test case for device_type1_node_powers_get_by_id

        Get details of Primera / Alletra 9K Node Power Supply identified by {nodeId} and {id}  # noqa: E501
        """
        pass

    def test_device_type1_node_powers_list(self):
        """Test case for device_type1_node_powers_list

        Get details of Primera / Alletra 9K Node Power Supplies identified by {nodeId}  # noqa: E501
        """
        pass

    def test_device_type1_nodes_get_by_id(self):
        """Test case for device_type1_nodes_get_by_id

        Get details of Primera / Alletra 9K Node identified by {id}  # noqa: E501
        """
        pass

    def test_device_type1_nodes_list(self):
        """Test case for device_type1_nodes_list

        Get details of Primera / Alletra 9K Nodes  # noqa: E501
        """
        pass

    def test_device_type2_controller_halt(self):
        """Test case for device_type2_controller_halt

        Perform halt of Nimble / Alletra 6K controller identified by {controllerId}  # noqa: E501
        """
        pass

    def test_device_type2_get_all_controllers(self):
        """Test case for device_type2_get_all_controllers

        Get all controllers details by Nimble / Alletra 6K  # noqa: E501
        """
        pass

    def test_device_type2_get_controller_by_id(self):
        """Test case for device_type2_get_controller_by_id

        Get details of Nimble / Alletra 6K Controller identified by {controllerId}  # noqa: E501
        """
        pass

    def test_node_powers_locate_pcmbby_id(self):
        """Test case for node_powers_locate_pcmbby_id

        Locate PCBM of Primera / Alletra 9K identified by {id}  # noqa: E501
        """
        pass

    def test_nodes_locate_by_id(self):
        """Test case for nodes_locate_by_id

        Locate node of Primera / Alletra 9K identified by {id}  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
