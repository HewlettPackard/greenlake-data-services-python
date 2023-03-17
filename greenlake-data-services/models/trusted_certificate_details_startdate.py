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


class TrustedCertificateDetailsStartdate(object):
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
        'ms': 'int',
        'tz': 'str'
    }

    attribute_map = {
        'ms': 'ms',
        'tz': 'tz'
    }

    def __init__(self, ms=None, tz=None):  # noqa: E501
        """TrustedCertificateDetailsStartdate - a model defined in OpenAPI"""  # noqa: E501

        self._ms = None
        self._tz = None
        self.discriminator = None

        if ms is not None:
            self.ms = ms
        if tz is not None:
            self.tz = tz

    @property
    def ms(self):
        """Gets the ms of this TrustedCertificateDetailsStartdate.  # noqa: E501

        time in millisecond  # noqa: E501

        :return: The ms of this TrustedCertificateDetailsStartdate.  # noqa: E501
        :rtype: int
        """
        return self._ms

    @ms.setter
    def ms(self, ms):
        """Sets the ms of this TrustedCertificateDetailsStartdate.

        time in millisecond  # noqa: E501

        :param ms: The ms of this TrustedCertificateDetailsStartdate.  # noqa: E501
        :type: int
        """

        self._ms = ms

    @property
    def tz(self):
        """Gets the tz of this TrustedCertificateDetailsStartdate.  # noqa: E501

        timezone  # noqa: E501

        :return: The tz of this TrustedCertificateDetailsStartdate.  # noqa: E501
        :rtype: str
        """
        return self._tz

    @tz.setter
    def tz(self, tz):
        """Sets the tz of this TrustedCertificateDetailsStartdate.

        timezone  # noqa: E501

        :param tz: The tz of this TrustedCertificateDetailsStartdate.  # noqa: E501
        :type: str
        """

        self._tz = tz

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
        if not isinstance(other, TrustedCertificateDetailsStartdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
