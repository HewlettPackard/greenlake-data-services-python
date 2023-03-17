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


class ErrorCount(object):
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
        'correctable': 'int',
        'uncorrectable': 'int'
    }

    attribute_map = {
        'correctable': 'correctable',
        'uncorrectable': 'uncorrectable'
    }

    def __init__(self, correctable=None, uncorrectable=None):  # noqa: E501
        """ErrorCount - a model defined in OpenAPI"""  # noqa: E501

        self._correctable = None
        self._uncorrectable = None
        self.discriminator = None

        if correctable is not None:
            self.correctable = correctable
        if uncorrectable is not None:
            self.uncorrectable = uncorrectable

    @property
    def correctable(self):
        """Gets the correctable of this ErrorCount.  # noqa: E501

        correctable errors  # noqa: E501

        :return: The correctable of this ErrorCount.  # noqa: E501
        :rtype: int
        """
        return self._correctable

    @correctable.setter
    def correctable(self, correctable):
        """Sets the correctable of this ErrorCount.

        correctable errors  # noqa: E501

        :param correctable: The correctable of this ErrorCount.  # noqa: E501
        :type: int
        """

        self._correctable = correctable

    @property
    def uncorrectable(self):
        """Gets the uncorrectable of this ErrorCount.  # noqa: E501

        uncorrectable errors  # noqa: E501

        :return: The uncorrectable of this ErrorCount.  # noqa: E501
        :rtype: int
        """
        return self._uncorrectable

    @uncorrectable.setter
    def uncorrectable(self, uncorrectable):
        """Sets the uncorrectable of this ErrorCount.

        uncorrectable errors  # noqa: E501

        :param uncorrectable: The uncorrectable of this ErrorCount.  # noqa: E501
        :type: int
        """

        self._uncorrectable = uncorrectable

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
        if not isinstance(other, ErrorCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other