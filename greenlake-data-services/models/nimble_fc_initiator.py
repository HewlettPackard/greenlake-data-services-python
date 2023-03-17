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


class NimbleFCInitiator(object):
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
        'alias': 'str',
        'id': 'str',
        'wwpn': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'id': 'id',
        'wwpn': 'wwpn'
    }

    def __init__(self, alias=None, id=None, wwpn=None):  # noqa: E501
        """NimbleFCInitiator - a model defined in OpenAPI"""  # noqa: E501

        self._alias = None
        self._id = None
        self._wwpn = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if id is not None:
            self.id = id
        if wwpn is not None:
            self.wwpn = wwpn

    @property
    def alias(self):
        """Gets the alias of this NimbleFCInitiator.  # noqa: E501

        Alias of the Fibre Channel initiator.  # noqa: E501

        :return: The alias of this NimbleFCInitiator.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this NimbleFCInitiator.

        Alias of the Fibre Channel initiator.  # noqa: E501

        :param alias: The alias of this NimbleFCInitiator.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def id(self):
        """Gets the id of this NimbleFCInitiator.  # noqa: E501

        Unique identifier of the Fibre Channel initiator.  # noqa: E501

        :return: The id of this NimbleFCInitiator.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NimbleFCInitiator.

        Unique identifier of the Fibre Channel initiator.  # noqa: E501

        :param id: The id of this NimbleFCInitiator.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def wwpn(self):
        """Gets the wwpn of this NimbleFCInitiator.  # noqa: E501

        WWPN (World Wide Port Name) of the Fibre Channel initiator.  # noqa: E501

        :return: The wwpn of this NimbleFCInitiator.  # noqa: E501
        :rtype: str
        """
        return self._wwpn

    @wwpn.setter
    def wwpn(self, wwpn):
        """Sets the wwpn of this NimbleFCInitiator.

        WWPN (World Wide Port Name) of the Fibre Channel initiator.  # noqa: E501

        :param wwpn: The wwpn of this NimbleFCInitiator.  # noqa: E501
        :type: str
        """

        self._wwpn = wwpn

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
        if not isinstance(other, NimbleFCInitiator):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other