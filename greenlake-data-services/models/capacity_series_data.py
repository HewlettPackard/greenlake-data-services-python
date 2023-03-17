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


class CapacitySeriesData(object):
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
        'timestamp_ms': 'int',
        'usage_mi_b': 'float'
    }

    attribute_map = {
        'timestamp_ms': 'timestampMs',
        'usage_mi_b': 'usageMiB'
    }

    def __init__(self, timestamp_ms=None, usage_mi_b=None):  # noqa: E501
        """CapacitySeriesData - a model defined in OpenAPI"""  # noqa: E501

        self._timestamp_ms = None
        self._usage_mi_b = None
        self.discriminator = None

        if timestamp_ms is not None:
            self.timestamp_ms = timestamp_ms
        if usage_mi_b is not None:
            self.usage_mi_b = usage_mi_b

    @property
    def timestamp_ms(self):
        """Gets the timestamp_ms of this CapacitySeriesData.  # noqa: E501

        epoch timestamp  # noqa: E501

        :return: The timestamp_ms of this CapacitySeriesData.  # noqa: E501
        :rtype: int
        """
        return self._timestamp_ms

    @timestamp_ms.setter
    def timestamp_ms(self, timestamp_ms):
        """Sets the timestamp_ms of this CapacitySeriesData.

        epoch timestamp  # noqa: E501

        :param timestamp_ms: The timestamp_ms of this CapacitySeriesData.  # noqa: E501
        :type: int
        """

        self._timestamp_ms = timestamp_ms

    @property
    def usage_mi_b(self):
        """Gets the usage_mi_b of this CapacitySeriesData.  # noqa: E501

        capacity usage value at particular timestamp  # noqa: E501

        :return: The usage_mi_b of this CapacitySeriesData.  # noqa: E501
        :rtype: float
        """
        return self._usage_mi_b

    @usage_mi_b.setter
    def usage_mi_b(self, usage_mi_b):
        """Sets the usage_mi_b of this CapacitySeriesData.

        capacity usage value at particular timestamp  # noqa: E501

        :param usage_mi_b: The usage_mi_b of this CapacitySeriesData.  # noqa: E501
        :type: float
        """

        self._usage_mi_b = usage_mi_b

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
        if not isinstance(other, CapacitySeriesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
