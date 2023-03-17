# coding: utf-8

"""
    Data Services Cloud Console API

    Data Services Cloud Console API  # noqa: E501

    OpenAPI spec version: 1.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PerfData(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'avg_of1day': 'float',
        'avg_of1hour': 'float',
        'avg_of8hours': 'float',
        'avg_oflatest': 'float'
    }

    attribute_map = {
        'avg_of1day': 'avgOf1day',
        'avg_of1hour': 'avgOf1hour',
        'avg_of8hours': 'avgOf8hours',
        'avg_oflatest': 'avgOflatest'
    }

    def __init__(self, avg_of1day=None, avg_of1hour=None, avg_of8hours=None, avg_oflatest=None):  # noqa: E501
        """PerfData - a model defined in OpenAPI"""  # noqa: E501

        self._avg_of1day = None
        self._avg_of1hour = None
        self._avg_of8hours = None
        self._avg_oflatest = None
        self.discriminator = None

        if avg_of1day is not None:
            self.avg_of1day = avg_of1day
        if avg_of1hour is not None:
            self.avg_of1hour = avg_of1hour
        if avg_of8hours is not None:
            self.avg_of8hours = avg_of8hours
        if avg_oflatest is not None:
            self.avg_oflatest = avg_oflatest

    @property
    def avg_of1day(self):
        """Gets the avg_of1day of this PerfData.  # noqa: E501

        last one day avg data  # noqa: E501

        :return: The avg_of1day of this PerfData.  # noqa: E501
        :rtype: float
        """
        return self._avg_of1day

    @avg_of1day.setter
    def avg_of1day(self, avg_of1day):
        """Sets the avg_of1day of this PerfData.

        last one day avg data  # noqa: E501

        :param avg_of1day: The avg_of1day of this PerfData.  # noqa: E501
        :type: float
        """

        self._avg_of1day = avg_of1day

    @property
    def avg_of1hour(self):
        """Gets the avg_of1hour of this PerfData.  # noqa: E501

        last one hour avg data  # noqa: E501

        :return: The avg_of1hour of this PerfData.  # noqa: E501
        :rtype: float
        """
        return self._avg_of1hour

    @avg_of1hour.setter
    def avg_of1hour(self, avg_of1hour):
        """Sets the avg_of1hour of this PerfData.

        last one hour avg data  # noqa: E501

        :param avg_of1hour: The avg_of1hour of this PerfData.  # noqa: E501
        :type: float
        """

        self._avg_of1hour = avg_of1hour

    @property
    def avg_of8hours(self):
        """Gets the avg_of8hours of this PerfData.  # noqa: E501

        last 8 hours avg data  # noqa: E501

        :return: The avg_of8hours of this PerfData.  # noqa: E501
        :rtype: float
        """
        return self._avg_of8hours

    @avg_of8hours.setter
    def avg_of8hours(self, avg_of8hours):
        """Sets the avg_of8hours of this PerfData.

        last 8 hours avg data  # noqa: E501

        :param avg_of8hours: The avg_of8hours of this PerfData.  # noqa: E501
        :type: float
        """

        self._avg_of8hours = avg_of8hours

    @property
    def avg_oflatest(self):
        """Gets the avg_oflatest of this PerfData.  # noqa: E501

        latest perf data  # noqa: E501

        :return: The avg_oflatest of this PerfData.  # noqa: E501
        :rtype: float
        """
        return self._avg_oflatest

    @avg_oflatest.setter
    def avg_oflatest(self, avg_oflatest):
        """Sets the avg_oflatest of this PerfData.

        latest perf data  # noqa: E501

        :param avg_oflatest: The avg_oflatest of this PerfData.  # noqa: E501
        :type: float
        """

        self._avg_oflatest = avg_oflatest

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PerfData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other