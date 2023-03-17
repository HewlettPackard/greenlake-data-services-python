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


class EnclosureDiskLoop(object):
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
        'alpa': 'int',
        'state': 'STATE'
    }

    attribute_map = {
        'alpa': 'alpa',
        'state': 'state'
    }

    def __init__(self, alpa=None, state=None):  # noqa: E501
        """EnclosureDiskLoop - a model defined in OpenAPI"""  # noqa: E501

        self._alpa = None
        self._state = None
        self.discriminator = None

        if alpa is not None:
            self.alpa = alpa
        if state is not None:
            self.state = state

    @property
    def alpa(self):
        """Gets the alpa of this EnclosureDiskLoop.  # noqa: E501


        :return: The alpa of this EnclosureDiskLoop.  # noqa: E501
        :rtype: int
        """
        return self._alpa

    @alpa.setter
    def alpa(self, alpa):
        """Sets the alpa of this EnclosureDiskLoop.


        :param alpa: The alpa of this EnclosureDiskLoop.  # noqa: E501
        :type: int
        """

        self._alpa = alpa

    @property
    def state(self):
        """Gets the state of this EnclosureDiskLoop.  # noqa: E501


        :return: The state of this EnclosureDiskLoop.  # noqa: E501
        :rtype: STATE
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this EnclosureDiskLoop.


        :param state: The state of this EnclosureDiskLoop.  # noqa: E501
        :type: STATE
        """

        self._state = state

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
        if not isinstance(other, EnclosureDiskLoop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
