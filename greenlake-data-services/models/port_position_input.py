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


class PortPositionInput(object):
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
        'node': 'int',
        'port': 'int',
        'slot': 'int'
    }

    attribute_map = {
        'node': 'node',
        'port': 'port',
        'slot': 'slot'
    }

    def __init__(self, node=None, port=None, slot=None):  # noqa: E501
        """PortPositionInput - a model defined in OpenAPI"""  # noqa: E501

        self._node = None
        self._port = None
        self._slot = None
        self.discriminator = None

        self.node = node
        self.port = port
        self.slot = slot

    @property
    def node(self):
        """Gets the node of this PortPositionInput.  # noqa: E501

        Port position node number  # noqa: E501

        :return: The node of this PortPositionInput.  # noqa: E501
        :rtype: int
        """
        return self._node

    @node.setter
    def node(self, node):
        """Sets the node of this PortPositionInput.

        Port position node number  # noqa: E501

        :param node: The node of this PortPositionInput.  # noqa: E501
        :type: int
        """
        if node is None:
            raise ValueError("Invalid value for `node`, must not be `None`")  # noqa: E501

        self._node = node

    @property
    def port(self):
        """Gets the port of this PortPositionInput.  # noqa: E501

        Port position port number  # noqa: E501

        :return: The port of this PortPositionInput.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this PortPositionInput.

        Port position port number  # noqa: E501

        :param port: The port of this PortPositionInput.  # noqa: E501
        :type: int
        """
        if port is None:
            raise ValueError("Invalid value for `port`, must not be `None`")  # noqa: E501

        self._port = port

    @property
    def slot(self):
        """Gets the slot of this PortPositionInput.  # noqa: E501

        Port position slot number  # noqa: E501

        :return: The slot of this PortPositionInput.  # noqa: E501
        :rtype: int
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this PortPositionInput.

        Port position slot number  # noqa: E501

        :param slot: The slot of this PortPositionInput.  # noqa: E501
        :type: int
        """
        if slot is None:
            raise ValueError("Invalid value for `slot`, must not be `None`")  # noqa: E501

        self._slot = slot

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
        if not isinstance(other, PortPositionInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
