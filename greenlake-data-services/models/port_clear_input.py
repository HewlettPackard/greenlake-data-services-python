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


class PortClearInput(object):
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
        'ip_type': 'str'
    }

    attribute_map = {
        'ip_type': 'ipType'
    }

    def __init__(self, ip_type=None):  # noqa: E501
        """PortClearInput - a model defined in OpenAPI"""  # noqa: E501

        self._ip_type = None
        self.discriminator = None

        if ip_type is not None:
            self.ip_type = ip_type

    @property
    def ip_type(self):
        """Gets the ip_type of this PortClearInput.  # noqa: E501

        For RCIP ports, the IP version of the address that needs to be cleared from the port. Either the IPv4 address or IPv6 address or both addresses can be cleared. Possible values: v4,v6,both  # noqa: E501

        :return: The ip_type of this PortClearInput.  # noqa: E501
        :rtype: str
        """
        return self._ip_type

    @ip_type.setter
    def ip_type(self, ip_type):
        """Sets the ip_type of this PortClearInput.

        For RCIP ports, the IP version of the address that needs to be cleared from the port. Either the IPv4 address or IPv6 address or both addresses can be cleared. Possible values: v4,v6,both  # noqa: E501

        :param ip_type: The ip_type of this PortClearInput.  # noqa: E501
        :type: str
        """

        self._ip_type = ip_type

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
        if not isinstance(other, PortClearInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
