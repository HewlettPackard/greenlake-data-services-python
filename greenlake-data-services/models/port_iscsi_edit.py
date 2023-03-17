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


class PortISCSIEdit(object):
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
        'gateway_address': 'str',
        'ip_address': 'str',
        'label': 'str',
        'mtu': 'str',
        'net_mask': 'str',
        'send_target_group_tag': 'int'
    }

    attribute_map = {
        'gateway_address': 'gatewayAddress',
        'ip_address': 'ipAddress',
        'label': 'label',
        'mtu': 'mtu',
        'net_mask': 'netMask',
        'send_target_group_tag': 'sendTargetGroupTag'
    }

    def __init__(self, gateway_address=None, ip_address=None, label=None, mtu=None, net_mask=None, send_target_group_tag=None):  # noqa: E501
        """PortISCSIEdit - a model defined in OpenAPI"""  # noqa: E501

        self._gateway_address = None
        self._ip_address = None
        self._label = None
        self._mtu = None
        self._net_mask = None
        self._send_target_group_tag = None
        self.discriminator = None

        if gateway_address is not None:
            self.gateway_address = gateway_address
        if ip_address is not None:
            self.ip_address = ip_address
        if label is not None:
            self.label = label
        if mtu is not None:
            self.mtu = mtu
        if net_mask is not None:
            self.net_mask = net_mask
        if send_target_group_tag is not None:
            self.send_target_group_tag = send_target_group_tag

    @property
    def gateway_address(self):
        """Gets the gateway_address of this PortISCSIEdit.  # noqa: E501

        Gateway address to edit to  # noqa: E501

        :return: The gateway_address of this PortISCSIEdit.  # noqa: E501
        :rtype: str
        """
        return self._gateway_address

    @gateway_address.setter
    def gateway_address(self, gateway_address):
        """Sets the gateway_address of this PortISCSIEdit.

        Gateway address to edit to  # noqa: E501

        :param gateway_address: The gateway_address of this PortISCSIEdit.  # noqa: E501
        :type: str
        """

        self._gateway_address = gateway_address

    @property
    def ip_address(self):
        """Gets the ip_address of this PortISCSIEdit.  # noqa: E501

        IP address to edit to  # noqa: E501

        :return: The ip_address of this PortISCSIEdit.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this PortISCSIEdit.

        IP address to edit to  # noqa: E501

        :param ip_address: The ip_address of this PortISCSIEdit.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def label(self):
        """Gets the label of this PortISCSIEdit.  # noqa: E501

        label of the port to edit to  # noqa: E501

        :return: The label of this PortISCSIEdit.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PortISCSIEdit.

        label of the port to edit to  # noqa: E501

        :param label: The label of this PortISCSIEdit.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def mtu(self):
        """Gets the mtu of this PortISCSIEdit.  # noqa: E501

        MTU to edit to. Possible Values: \"1500\", \"9000\"  # noqa: E501

        :return: The mtu of this PortISCSIEdit.  # noqa: E501
        :rtype: str
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this PortISCSIEdit.

        MTU to edit to. Possible Values: \"1500\", \"9000\"  # noqa: E501

        :param mtu: The mtu of this PortISCSIEdit.  # noqa: E501
        :type: str
        """

        self._mtu = mtu

    @property
    def net_mask(self):
        """Gets the net_mask of this PortISCSIEdit.  # noqa: E501

        NetMask address to edit to  # noqa: E501

        :return: The net_mask of this PortISCSIEdit.  # noqa: E501
        :rtype: str
        """
        return self._net_mask

    @net_mask.setter
    def net_mask(self, net_mask):
        """Sets the net_mask of this PortISCSIEdit.

        NetMask address to edit to  # noqa: E501

        :param net_mask: The net_mask of this PortISCSIEdit.  # noqa: E501
        :type: str
        """

        self._net_mask = net_mask

    @property
    def send_target_group_tag(self):
        """Gets the send_target_group_tag of this PortISCSIEdit.  # noqa: E501


        :return: The send_target_group_tag of this PortISCSIEdit.  # noqa: E501
        :rtype: int
        """
        return self._send_target_group_tag

    @send_target_group_tag.setter
    def send_target_group_tag(self, send_target_group_tag):
        """Sets the send_target_group_tag of this PortISCSIEdit.


        :param send_target_group_tag: The send_target_group_tag of this PortISCSIEdit.  # noqa: E501
        :type: int
        """

        self._send_target_group_tag = send_target_group_tag

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
        if not isinstance(other, PortISCSIEdit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other