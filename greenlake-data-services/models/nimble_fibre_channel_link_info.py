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


class NimbleFibreChannelLinkInfo(object):
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
        'link_speed': 'str',
        'link_status': 'str',
        'max_link_speed': 'str',
        'operational_status': 'str'
    }

    attribute_map = {
        'link_speed': 'link_speed',
        'link_status': 'link_status',
        'max_link_speed': 'max_link_speed',
        'operational_status': 'operational_status'
    }

    def __init__(self, link_speed=None, link_status=None, max_link_speed=None, operational_status=None):  # noqa: E501
        """NimbleFibreChannelLinkInfo - a model defined in OpenAPI"""  # noqa: E501

        self._link_speed = None
        self._link_status = None
        self._max_link_speed = None
        self._operational_status = None
        self.discriminator = None

        if link_speed is not None:
            self.link_speed = link_speed
        if link_status is not None:
            self.link_status = link_status
        if max_link_speed is not None:
            self.max_link_speed = max_link_speed
        if operational_status is not None:
            self.operational_status = operational_status

    @property
    def link_speed(self):
        """Gets the link_speed of this NimbleFibreChannelLinkInfo.  # noqa: E501

        Speed of the Fibre Channel link.  # noqa: E501

        :return: The link_speed of this NimbleFibreChannelLinkInfo.  # noqa: E501
        :rtype: str
        """
        return self._link_speed

    @link_speed.setter
    def link_speed(self, link_speed):
        """Sets the link_speed of this NimbleFibreChannelLinkInfo.

        Speed of the Fibre Channel link.  # noqa: E501

        :param link_speed: The link_speed of this NimbleFibreChannelLinkInfo.  # noqa: E501
        :type: str
        """

        self._link_speed = link_speed

    @property
    def link_status(self):
        """Gets the link_status of this NimbleFibreChannelLinkInfo.  # noqa: E501

        Status of the Fibre Channel link. Possible values: plat_fc_link_status_reset, plat_fc_link_status_down, plat_fc_link_status_up, plat_fc_link_status_error, plat_fc_link_status_unknown, plat_fc_link_status_not_connected  # noqa: E501

        :return: The link_status of this NimbleFibreChannelLinkInfo.  # noqa: E501
        :rtype: str
        """
        return self._link_status

    @link_status.setter
    def link_status(self, link_status):
        """Sets the link_status of this NimbleFibreChannelLinkInfo.

        Status of the Fibre Channel link. Possible values: plat_fc_link_status_reset, plat_fc_link_status_down, plat_fc_link_status_up, plat_fc_link_status_error, plat_fc_link_status_unknown, plat_fc_link_status_not_connected  # noqa: E501

        :param link_status: The link_status of this NimbleFibreChannelLinkInfo.  # noqa: E501
        :type: str
        """

        self._link_status = link_status

    @property
    def max_link_speed(self):
        """Gets the max_link_speed of this NimbleFibreChannelLinkInfo.  # noqa: E501

        Maximum speed of the Fibre Channel link.  # noqa: E501

        :return: The max_link_speed of this NimbleFibreChannelLinkInfo.  # noqa: E501
        :rtype: str
        """
        return self._max_link_speed

    @max_link_speed.setter
    def max_link_speed(self, max_link_speed):
        """Sets the max_link_speed of this NimbleFibreChannelLinkInfo.

        Maximum speed of the Fibre Channel link.  # noqa: E501

        :param max_link_speed: The max_link_speed of this NimbleFibreChannelLinkInfo.  # noqa: E501
        :type: str
        """

        self._max_link_speed = max_link_speed

    @property
    def operational_status(self):
        """Gets the operational_status of this NimbleFibreChannelLinkInfo.  # noqa: E501

        Operational status of the Fibre Channel link. Possible values: plat_fc_operational_status_admin_offline, plat_fc_operational_status_direct, plat_fc_operational_status_initializing, plat_fc_operational_status_configured, plat_fc_operational_status_fault, plat_fc_operational_status_operational, plat_fc_operational_status_unknown, plat_fc_operational_status_unconfigured  # noqa: E501

        :return: The operational_status of this NimbleFibreChannelLinkInfo.  # noqa: E501
        :rtype: str
        """
        return self._operational_status

    @operational_status.setter
    def operational_status(self, operational_status):
        """Sets the operational_status of this NimbleFibreChannelLinkInfo.

        Operational status of the Fibre Channel link. Possible values: plat_fc_operational_status_admin_offline, plat_fc_operational_status_direct, plat_fc_operational_status_initializing, plat_fc_operational_status_configured, plat_fc_operational_status_fault, plat_fc_operational_status_operational, plat_fc_operational_status_unknown, plat_fc_operational_status_unconfigured  # noqa: E501

        :param operational_status: The operational_status of this NimbleFibreChannelLinkInfo.  # noqa: E501
        :type: str
        """

        self._operational_status = operational_status

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
        if not isinstance(other, NimbleFibreChannelLinkInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other