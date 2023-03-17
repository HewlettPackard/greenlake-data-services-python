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


class CapacitySummary(object):
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
        'free': 'int',
        'total': 'int'
    }

    attribute_map = {
        'free': 'free',
        'total': 'total'
    }

    def __init__(self, free=None, total=None):  # noqa: E501
        """CapacitySummary - a model defined in OpenAPI"""  # noqa: E501

        self._free = None
        self._total = None
        self.discriminator = None

        if free is not None:
            self.free = free
        if total is not None:
            self.total = total

    @property
    def free(self):
        """Gets the free of this CapacitySummary.  # noqa: E501

        Total free capacity  # noqa: E501

        :return: The free of this CapacitySummary.  # noqa: E501
        :rtype: int
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this CapacitySummary.

        Total free capacity  # noqa: E501

        :param free: The free of this CapacitySummary.  # noqa: E501
        :type: int
        """

        self._free = free

    @property
    def total(self):
        """Gets the total of this CapacitySummary.  # noqa: E501

        Total used capacity  # noqa: E501

        :return: The total of this CapacitySummary.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CapacitySummary.

        Total used capacity  # noqa: E501

        :param total: The total of this CapacitySummary.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if not isinstance(other, CapacitySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
