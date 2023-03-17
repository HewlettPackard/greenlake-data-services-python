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


class EncDcsdata(object):
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
        'fw_status': 'str',
        'fw_version': 'str'
    }

    attribute_map = {
        'fw_status': 'fwStatus',
        'fw_version': 'fwVersion'
    }

    def __init__(self, fw_status=None, fw_version=None):  # noqa: E501
        """EncDcsdata - a model defined in OpenAPI"""  # noqa: E501

        self._fw_status = None
        self._fw_version = None
        self.discriminator = None

        if fw_status is not None:
            self.fw_status = fw_status
        if fw_version is not None:
            self.fw_version = fw_version

    @property
    def fw_status(self):
        """Gets the fw_status of this EncDcsdata.  # noqa: E501


        :return: The fw_status of this EncDcsdata.  # noqa: E501
        :rtype: str
        """
        return self._fw_status

    @fw_status.setter
    def fw_status(self, fw_status):
        """Sets the fw_status of this EncDcsdata.


        :param fw_status: The fw_status of this EncDcsdata.  # noqa: E501
        :type: str
        """

        self._fw_status = fw_status

    @property
    def fw_version(self):
        """Gets the fw_version of this EncDcsdata.  # noqa: E501


        :return: The fw_version of this EncDcsdata.  # noqa: E501
        :rtype: str
        """
        return self._fw_version

    @fw_version.setter
    def fw_version(self, fw_version):
        """Sets the fw_version of this EncDcsdata.


        :param fw_version: The fw_version of this EncDcsdata.  # noqa: E501
        :type: str
        """

        self._fw_version = fw_version

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
        if not isinstance(other, EncDcsdata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
