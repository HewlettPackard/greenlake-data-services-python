"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.1.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import greenlake_data_services
from greenlake_data_services.model.error_response import ErrorResponse
from greenlake_data_services.model.resource_reference import ResourceReference
from greenlake_data_services.model.task_console_reference import TaskConsoleReference
from greenlake_data_services.model.task_log_message import TaskLogMessage
from greenlake_data_services.model.task_recommendations import TaskRecommendations
globals()['ErrorResponse'] = ErrorResponse
globals()['ResourceReference'] = ResourceReference
globals()['TaskConsoleReference'] = TaskConsoleReference
globals()['TaskLogMessage'] = TaskLogMessage
globals()['TaskRecommendations'] = TaskRecommendations
from greenlake_data_services.model.task_properties import TaskProperties


class TestTaskProperties(unittest.TestCase):
    """TaskProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTaskProperties(self):
        """Test TaskProperties"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TaskProperties()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
