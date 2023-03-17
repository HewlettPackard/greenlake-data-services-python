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


class SysLocateInput(object):
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
        'locate_enabled': 'bool'
    }

    attribute_map = {
        'locate_enabled': 'locateEnabled'
    }

    def __init__(self, locate_enabled=None):  # noqa: E501
        """SysLocateInput - a model defined in OpenAPI"""  # noqa: E501

        self._locate_enabled = None
        self.discriminator = None

        if locate_enabled is not None:
            self.locate_enabled = locate_enabled

    @property
    def locate_enabled(self):
        """Gets the locate_enabled of this SysLocateInput.  # noqa: E501

        Indicates if the locate beacon should be enabled or not  # noqa: E501

        :return: The locate_enabled of this SysLocateInput.  # noqa: E501
        :rtype: bool
        """
        return self._locate_enabled

    @locate_enabled.setter
    def locate_enabled(self, locate_enabled):
        """Sets the locate_enabled of this SysLocateInput.

        Indicates if the locate beacon should be enabled or not  # noqa: E501

        :param locate_enabled: The locate_enabled of this SysLocateInput.  # noqa: E501
        :type: bool
        """

        self._locate_enabled = locate_enabled

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
        if not isinstance(other, SysLocateInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other