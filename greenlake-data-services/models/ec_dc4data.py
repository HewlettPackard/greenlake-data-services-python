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


class EcDc4data(object):
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
        'hpl_led': 'LED',
        'split_led': 'LED',
        'system_led': 'LED'
    }

    attribute_map = {
        'hpl_led': 'hplLED',
        'split_led': 'splitLED',
        'system_led': 'systemLED'
    }

    def __init__(self, hpl_led=None, split_led=None, system_led=None):  # noqa: E501
        """EcDc4data - a model defined in OpenAPI"""  # noqa: E501

        self._hpl_led = None
        self._split_led = None
        self._system_led = None
        self.discriminator = None

        if hpl_led is not None:
            self.hpl_led = hpl_led
        if split_led is not None:
            self.split_led = split_led
        if system_led is not None:
            self.system_led = system_led

    @property
    def hpl_led(self):
        """Gets the hpl_led of this EcDc4data.  # noqa: E501


        :return: The hpl_led of this EcDc4data.  # noqa: E501
        :rtype: LED
        """
        return self._hpl_led

    @hpl_led.setter
    def hpl_led(self, hpl_led):
        """Sets the hpl_led of this EcDc4data.


        :param hpl_led: The hpl_led of this EcDc4data.  # noqa: E501
        :type: LED
        """

        self._hpl_led = hpl_led

    @property
    def split_led(self):
        """Gets the split_led of this EcDc4data.  # noqa: E501


        :return: The split_led of this EcDc4data.  # noqa: E501
        :rtype: LED
        """
        return self._split_led

    @split_led.setter
    def split_led(self, split_led):
        """Sets the split_led of this EcDc4data.


        :param split_led: The split_led of this EcDc4data.  # noqa: E501
        :type: LED
        """

        self._split_led = split_led

    @property
    def system_led(self):
        """Gets the system_led of this EcDc4data.  # noqa: E501


        :return: The system_led of this EcDc4data.  # noqa: E501
        :rtype: LED
        """
        return self._system_led

    @system_led.setter
    def system_led(self, system_led):
        """Sets the system_led of this EcDc4data.


        :param system_led: The system_led of this EcDc4data.  # noqa: E501
        :type: LED
        """

        self._system_led = system_led

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
        if not isinstance(other, EcDc4data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other