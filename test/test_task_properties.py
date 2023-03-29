"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import greenlake_data_services
from greenlake_data_services.model.resource_reference import ResourceReference
from greenlake_data_services.model.task_log_message import TaskLogMessage
from greenlake_data_services.model.task_properties_additional_details import TaskPropertiesAdditionalDetails
from greenlake_data_services.model.task_properties_error import TaskPropertiesError
from greenlake_data_services.model.task_properties_parent_task import TaskPropertiesParentTask
from greenlake_data_services.model.task_properties_source_resource import TaskPropertiesSourceResource
from greenlake_data_services.model.task_recommendations import TaskRecommendations
globals()['ResourceReference'] = ResourceReference
globals()['TaskLogMessage'] = TaskLogMessage
globals()['TaskPropertiesAdditionalDetails'] = TaskPropertiesAdditionalDetails
globals()['TaskPropertiesError'] = TaskPropertiesError
globals()['TaskPropertiesParentTask'] = TaskPropertiesParentTask
globals()['TaskPropertiesSourceResource'] = TaskPropertiesSourceResource
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
